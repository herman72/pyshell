import sys

def main():
    try:
        while True:
            sys.stdout.write("$ ")
            # sys.stdout.flush()  # Ensure the prompt is displayed immediately

            # Wait for user input
            command = input()
            print(f"{command}: command not found")
    except KeyboardInterrupt:
        print("\nExiting shell...")

if __name__ == "__main__":
    main()