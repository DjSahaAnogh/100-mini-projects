import random
def get_num() -> int:
    return random.randint(1, 10)
if "__main__" == __name__:
    num: int = get_num()
    print("Welcome to the Number Guessing Game! \nThe computer will generate a rando number from 1 to 10 and you have to guess it. \nYou wll have 5 chances to guess. Best of luck!!")
    chances: int = 5
    while chances != 0:
        try: 
            guess: int = int(input("Enter you guess: "))
            user_input = True
        except ValueError:
            print("please enter a valid input!!")
            user_input = False
        if user_input:
            if guess != num:
                if guess > num:
                    print("Too high!")
                else:
                    print("Too low!")
                chances -= 1
                print(f"You have {chances} chances left.")
            else:
                print(f"Congratulations! You guessed it right in {5 - chances} chances!!")
                break
    if chances == 0:
        print(f"Sorry! You lost. The number was {num}.")