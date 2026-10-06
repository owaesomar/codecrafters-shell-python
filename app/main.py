import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        if user_input == "exit":
            break
        print(f"{user_input}: command not found")
        continue

if __name__ == "__main__":
    main()
