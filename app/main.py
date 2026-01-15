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
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
