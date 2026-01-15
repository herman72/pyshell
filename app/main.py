import sys


def main():
    try:
        while True:
            sys.stdout.write("$ ")
            sys.stdout.flush()  # Ensure the prompt is displayed immediately

            # Wait for user input
            command = input()
            if command.lower() in ["exit 0"]:
                sys.exit(0)
            elif command.lower() in ["exit 1"]:
                sys.exit(1)
            elif command.lower() in ["exit"]:
                sys.exit(0)
            elif command.lower().split()[0] == "echo":
                print(" ".join(command.split()[1:]))
            elif command.lower().split()[0] == "type":
                if command.lower().split()[1] in ["exit", "type", "echo"]:
                    print(f"{command.split()[1]} is a shell builtin")
                else:
                    print(f"{command.split()[1]}: not found")
            else:
                print(f"{command}: command not found")
    except KeyboardInterrupt:
        print("\nExiting shell...")
        sys.exit(0)

if __name__ == "__main__":
    main()
