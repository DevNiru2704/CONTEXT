import sys

# -----------------------
# AST Node Definitions
# -----------------------

class NumberNode:
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
            if char in "(),=":
                tokens.append(char)

    if current:
        tokens.append(current)

    return tokens


# -----------------------
# Parser
# -----------------------

def parse_value(tokens):
    token = tokens.pop(0)

    # Number
    if token.isdigit():
        return NumberNode(int(token))

    # Variable
    if token.isidentifier():
        return VariableNode(token)

    raise Exception(f"Invalid value: {token}")


def parse_expression(tokens):
    token = tokens.pop(0)

    if token in ("add", "subtract", "multiply", "divide"):
        if tokens.pop(0) != "(":
            raise Exception("Expected '('")

        left = parse_expression(tokens)

        if tokens.pop(0) != ",":
            raise Exception("Expected ','")

        right = parse_expression(tokens)

        if tokens.pop(0) != ")":
            raise Exception("Expected ')'")

        return BinaryOpNode(token, left, right)

    # fallback to value
    tokens.insert(0, token)
    return parse_value(tokens)


# -----------------------
# Interpreter
# -----------------------

def evaluate(node, memory):
    if isinstance(node, NumberNode):
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

    raise Exception("Unknown AST node")


# -----------------------
# Runner
# -----------------------

def run(filename):
    memory = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        tokens = tokenize(line)

        # let x = <expression>
        if tokens[0] == "let":
            var_name = tokens[1]
            if tokens[2] != "=":
                raise Exception("Expected '='")

            expr = parse_expression(tokens[3:])
            memory[var_name] = evaluate(expr, memory)

        # print <expression>
        elif tokens[0] == "print":
            expr = parse_expression(tokens[1:])
            print(evaluate(expr, memory))

        else:
            raise Exception(f"Invalid syntax: {line}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python context.py <file.cxt>")
        sys.exit(1)

    run(sys.argv[1])
