def odd_even(num) -> str:
    return "Even" if num % 2 == 0 else "Odd"
if __name__ == "__main__":
    print("Welcome to Odd or Even Checker")
    user_input: int = int(input("Enter a number: "))
    print(f"The number '{user_input}' is {odd_even(user_input)}")