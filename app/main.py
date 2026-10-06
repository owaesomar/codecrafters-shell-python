import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")
    user_input = input()
    if user_input == "xyz":
        print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
