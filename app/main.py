import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command.lower() in ["exit 0"]:
            sys.exit(0)
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
