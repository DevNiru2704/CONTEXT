import sys

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


def parse_value(tokens, memory):
    token = tokens.pop(0)

    # Number
    if token.isdigit():
        return int(token)

    # Variable
    if token in memory:
        return memory[token]

    # Function call
    if token in ("add", "subtract", "multiply", "divide"):
        if tokens.pop(0) != "(":
            raise Exception("Expected '('")

        left = parse_value(tokens, memory)

        if tokens.pop(0) != ",":
            raise Exception("Expected ','")

        right = parse_value(tokens, memory)

        if tokens.pop(0) != ")":
            raise Exception("Expected ')'")

        if token == "add":
            return left + right
        if token == "subtract":
            return left - right
        if token == "multiply":
            return left * right
        if token == "divide":
            return left // right

    raise Exception(f"Invalid value: {token}")


def run(filename):
    memory = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        tokens = tokenize(line)

        # let x = <value>
        if tokens[0] == "let":
            var_name = tokens[1]

            if tokens[2] != "=":
                raise Exception("Expected '='")

            value = parse_value(tokens[3:], memory)
            memory[var_name] = value

        # print <value>
        elif tokens[0] == "print":
            value = parse_value(tokens[1:], memory)
            print(value)

        else:
            raise Exception(f"Invalid syntax: {line}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python context.py <file.cxt>")
        sys.exit(1)

    run(sys.argv[1])
