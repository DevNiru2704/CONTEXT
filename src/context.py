import sys

def tokenize(line):
    tokens = []

    for part in line.split():
        if part.isdigit():
            tokens.append(("NUMBER", int(part)))
        else:
            tokens.append(("WORD", part))

    return tokens


def run(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        tokens = tokenize(line)

        command_type, command_value = tokens[0]

        if command_type == "WORD" and command_value == "print":
            value_type, value = tokens[1]

            if value_type == "NUMBER":
                print(value)
            else:
                raise Exception("print expects a number")

        else:
            raise Exception(f"Unknown command: {command_value}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python context.py <file.cxt>")
        sys.exit(1)

    run(sys.argv[1])
