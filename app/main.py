import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        
        if command.lower() in ["exit"]:
            sys.exit(0)
        if command.lower().split()[0] in ["echo"]:
            # print("/n")
            print(f"{" ".join(command.split()[1:])}")
        if command.lower().split()[0] in ["type"]:
            if command.lower().split()[1] in ["echo", "exit", "type"]:
                print(f"{command.lower().split()[1]} is a shell builtin")
            else:
                print(f"{command.lower().split()[1]}: not found")
        if command.lower().split()[0] not in ["echo", "exit", "type"]:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
