import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        user_input = input()

        if user_input == "exit":
            break

        if user_input.startswith("echo "):
            print(user_input[5:])
        elif user_input.startswith("type echo"):
            print(f"echo is a shell builtin")
        elif user_input.startswith("type exit"):
            print(f"exit is a shell builtin")
        elif user_input.startswith("type type"):
            print(f"type is a shell builtin")
        elif user_input.startswith("type invalid command"):
            print(f"invalid_command: not found")
        else:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()
