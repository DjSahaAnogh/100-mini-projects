import random

# Load words from the file
with open("words.txt", "r") as file:
    words: list = file.readlines()

def game() -> None:
    word: str = random.choice(words).strip().upper()  # Pick a random word and convert to uppercase
    word_len: int = len(word)
    
    letters_list: list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    guessed_letters: list = []
    
    guess: str = "-" * word_len
    guess_list: list = list(guess)
    attempts: int = 0

    while attempts < 5:  # Loop until 5 incorrect attempts
        print("\n" + guess)
        print(f"You have {5 - attempts} attempts left.")
        print(f"Letters you have guessed: {guessed_letters}")
        print(f"Letters you haven't guessed: {letters_list}")

        user_guess = input("Enter a letter: ").upper()

        if user_guess in guessed_letters or user_guess not in letters_list:
            print("You already guessed that letter or it's invalid. Try again.")
            continue
        
        guessed_letters.append(user_guess)
        letters_list.remove(user_guess)

        if user_guess in word:
            for i in range(word_len):
                if word[i] == user_guess:
                    guess_list[i] = user_guess
            guess = "".join(guess_list)
        else:
            attempts += 1  # Increase attempts only if the letter is incorrect

        if "-" not in guess:  # Player wins
            print("\nYou win!")
            print(f"The word was {word}")
            return

    print("\nYou lose!")  # If loop ends, player loses
    print(f"The word was {word}")

if __name__ == "__main__":
    game()
