import random
def scramble():
    word = input("Enter a word: ")
    word = list(word)
    random.shuffle(word)
    print("".join(word))
    print("Tell your firends to unscramble the word")
    user_input = input("Enter the unscrambled word: ")
    if user_input == word:
        print("Correct")
    else:
        print("Incorrect")
    print(f"The correct word is: {word}")
    print("Happy Coding")
if __name__ == "__main__":
    scramble()