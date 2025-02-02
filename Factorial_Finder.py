def factorial_iterative():
    while True:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number")
            return
        result = 1
        for i in range(1, num + 1):
            result *= i  # Multiply result by each number from 1 to n
        print(f"Factorial of {num} is {result}")
        break
if __name__ == "__main__":
    factorial_iterative()