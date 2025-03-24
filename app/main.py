import sys
import os

def main():
    input_path = os.environ.get("PATH", "")
    input_path = input_path.split(":") if input_path else []
    
    try:
        while True:
            sys.stdout.write("$ ")
            sys.stdout.flush()  # Ensure the prompt is displayed immediately

            is_found = False
            # Wait for user input
            command = input()
            if command.lower() in ["exit 0"]:
                sys.exit(0)
            elif command.lower() in ["exit 1"]:
                sys.exit(1)
            elif command.lower().split()[0] == "echo":
                print(" ".join(command.split()[1:]))
            elif command.lower().split()[0] == "type":
                if command.lower().split()[1] in ["exit", "type", "echo"]:
                    print(f"{command.split()[1]} is a shell builtin")
                
                elif input_path is not None:
        
                    for path in input_path:
                        if os.path.exists(f"{path}/{command.split()[1]}"):
                            print(f"{command.split()[1]} is {path}/{command.split()[1]}")
                            is_found = True
                            break
                    if not is_found:
                        print(f"{command.split()[1]}: not found")
                else:
                    print(f"{command.split()[1]}: not found")
            else:
                print(f"{command}: command not found")
    except KeyboardInterrupt:
        print("\nExiting shell...")
        sys.exit(0)

if __name__ == "__main__":
    main()