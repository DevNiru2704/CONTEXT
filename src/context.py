import sys

def tokenize(line):
    tokens = []

    for part in line.split():
        if part.isdigit():
            tokens.append(("NUMBER", int(part)))
        elif part == "=":
            tokens.append(("EQUALS", part))
        else:
            tokens.append(("WORD", part))

    return tokens


def run(filename):
    memory = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        tokens = tokenize(line)

        # Variable declaration: let x = 10
        if (
            tokens[0] == ("WORD", "let") and
            tokens[1][0] == "WORD" and
            tokens[2] == ("EQUALS", "=") and
            tokens[3][0] == "NUMBER"
        ):
            var_name = tokens[1][1]
            value = tokens[3][1]
            memory[var_name] = value

        # Print statement: print x OR print 10
        elif tokens[0] == ("WORD", "print"):
            value_type, value = tokens[1]

            if value_type == "NUMBER":
                print(value)
            elif value_type == "WORD":
                if value not in memory:
                    raise Exception(f"Undefined variable: {value}")
                print(memory[value])
            else:
                raise Exception("Invalid print argument")

        else:
            raise Exception(f"Invalid syntax: {line}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python context.py <file.cxt>")
        sys.exit(1)

    run(sys.argv[1])
