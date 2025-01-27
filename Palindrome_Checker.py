def palindrome_checker(word: str) -> bool:
    return word == word[::-1]
if __name__ == "__main__":
    print("Welcome to Palindrome Checker")
    user_input: str = input("Enter a word: ")
    if palindrome_checker(user_input):
        print(f"The word '{user_input}' is a palindrome")
    else:
        print(f"The word '{user_input}' is not a palindrome")