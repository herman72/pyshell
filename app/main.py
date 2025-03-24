import shutil
import sys
import os

def main():
    input_path = os.environ.get("PATH", "")
    input_path = input_path.split(":") if input_path else []
    builtin = ["exit", "type", "echo"]
    try:
        while True:
            sys.stdout.write("$ ")
            sys.stdout.flush()  # Ensure the prompt is displayed immediately

            # Wait for user input
            command = input()
            match command.split():
                case ["echo", *args]:
                    print(*args)
                case ["exit", "0"]:
                    sys.exit(0)
                case ["type", arg]:
                    if arg in builtin:
                        print(f"{arg} is a shell builtin")
                    elif path := shutil.which(arg):
                        print(f"{arg} is {path}")
                    else:
                        print(f"{arg}: not found")
                case [arg1, arg2]:
                    print(shutil.which(arg1))
                    print("helloowwww")
                    print(shutil.which(arg2))
                    if (path1 := shutil.which(arg1)):
                        # execute arg1 with arg2 as argument
                        os.execv(path1, [arg1, arg2])
                    else:
                        print(f"{command}: command not found")
                    
            # if command.lower() in ["exit 0"]:
            #     sys.exit(0)
            # elif command.lower() in ["exit 1"]:
            #     sys.exit(1)
            # elif command.lower().split()[0] == "echo":
            #     print(" ".join(command.split()[1:]))
            # elif command.lower().split()[0] == "type":
            #     if command.lower().split()[1] in ["exit", "type", "echo"]:
            #         print(f"{command.split()[1]} is a shell builtin")
                
            #     elif input_path is not None:
        
            #         for path in input_path:
            #             if os.path.exists(f"{path}/{command.split()[1]}"):
            #                 print(f"{command.split()[1]} is {path}/{command.split()[1]}")
            #                 is_found = True
            #                 break
            #         if not is_found:
            #             print(f"{command.split()[1]}: not found")
            #     else:
            #         print(f"{command.split()[1]}: not found")
            # else:
            #     print(f"{command}: command not found")
    except KeyboardInterrupt:
        print("\nExiting shell...")
        sys.exit(0)

if __name__ == "__main__":
    main()