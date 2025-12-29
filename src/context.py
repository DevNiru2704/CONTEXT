import sys

# -----------------------
# AST Nodes
# -----------------------

class NumberNode:
    def __init__(self, value):
        self.value = value

class BooleanNode:
    def __init__(self, value):
        self.value = value

class VariableNode:
    def __init__(self, name):
        self.name = name

class BinaryOpNode:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class IfNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


# -----------------------
# Lexer
# -----------------------

def tokenize(line):
    tokens = []
    current = ""

    for char in line:
        if char.isalnum() or char == "_":
            current += char
        else:
            if current:
                tokens.append(current)
                current = ""
            if char in "(),=:": 
                tokens.append(char)

    if current:
        tokens.append(current)

    return tokens


# -----------------------
# Parser
# -----------------------

def parse_expression(tokens):
    token = tokens.pop(0)

    # Function calls FIRST
    if token in (
        "add", "subtract", "multiply", "divide",
        "equals", "greater", "less", "greater_equal"
    ):
        if tokens.pop(0) != "(":
            raise Exception("Expected '('")

        left = parse_expression(tokens)

        if tokens.pop(0) != ",":
            raise Exception("Expected ','")

        right = parse_expression(tokens)

        if tokens.pop(0) != ")":
            raise Exception("Expected ')'")

        return BinaryOpNode(token, left, right)

    # Number
    if token.isdigit():
        return NumberNode(int(token))

    # Variable
    if token.isidentifier():
        return VariableNode(token)

    raise Exception(f"Invalid expression: {token}")



# -----------------------
# Interpreter
# -----------------------

def evaluate(node, memory):
    if isinstance(node, NumberNode):
        return node.value

    if isinstance(node, BooleanNode):
        return node.value

    if isinstance(node, VariableNode):
        if node.name not in memory:
            raise Exception(f"Undefined variable: {node.name}")
        return memory[node.name]

    if isinstance(node, BinaryOpNode):
        left = evaluate(node.left, memory)
        right = evaluate(node.right, memory)

        if node.op == "add":
            return left + right
        if node.op == "subtract":
            return left - right
        if node.op == "multiply":
            return left * right
        if node.op == "divide":
            return left // right

        if node.op == "equals":
            return left == right
        if node.op == "greater":
            return left > right
        if node.op == "less":
            return left < right

    raise Exception("Unknown node")


def run(filename):
    memory = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line:
            i += 1
            continue

        tokens = tokenize(line)

        # let x = <expression>
        if tokens[0] == "let":
            var_name = tokens[1]
            expr = parse_expression(tokens[3:])
            memory[var_name] = evaluate(expr, memory)

        # print <expression>
        elif tokens[0] == "print":
            expr = parse_expression(tokens[1:])
            print(evaluate(expr, memory))

        # if <condition>:
        elif tokens[0] == "if":
            condition = parse_expression(tokens[1:-1])

            i += 1
            body_line = lines[i].lstrip()
            body_tokens = tokenize(body_line)

            if evaluate(condition, memory):
                if body_tokens[0] == "print":
                    expr = parse_expression(body_tokens[1:])
                    print(evaluate(expr, memory))

        else:
            raise Exception(f"Invalid syntax: {line}")

        i += 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python context.py <file.cxt>")
        sys.exit(1)

    run(sys.argv[1])
