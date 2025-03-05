import random
def fate() -> None:
    nums: list = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Your fate number: ", random.choice(nums))
    def tell_fate() -> None:
        while True:
            user_input: str = input("Enter your fate number: ")
            if user_input == "1":
                print("You will be rich!")
                break
            elif user_input == "2":
                print("You will be poor!")
                break
            elif user_input == "3":
                print("You will be happy!")
                break
            elif user_input == "4":
                print("You will be sad!")
                break
            elif user_input == "5":
                print("You will be successful!")
                break
            elif user_input == "6":
                print("You will face great challenges!")
                break
            elif user_input == "7":
                print("You will be loved!")
                break
            elif user_input == "8":
                print("You will be in good health!")
                break
            else:
                print("Invalid input!")
    tell_fate()

if __name__ == "__main__":
    fate()