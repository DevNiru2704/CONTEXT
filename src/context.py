import sys

def run(filename:str):
    with open(filename,'r') as file:
        lines=file.readlines()
    for line in lines:
        line.strip()

        if not line:
            continue
        parts=line.split()
        command=parts[0]

        if command=="print":
            value=parts[1]
            print(value)
        else:
            raise Exception(f"Unknown command: {command}")

if __name__ == '__main__':
    if len(sys.argv)<2:
        print("Usage: print context.py <filename.ctxt>")
        sys.exit(1)
    run(sys.argv[1])