def name() -> str:
    user_input = input("Enter your name: ")
    words: list = user_input.split()
    first_letter: list = [word[0].upper() for word in words]
    return ".".join(first_letter)
if __name__ == "__main__":
    print(name())