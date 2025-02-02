import math

def prime_num() -> None:
    try:
        num = int(input("Enter a number: "))
        if num <= 1:
            print(f"{num} is not a prime number.")
            return
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                return
        
        print(f"{num} is a prime number.")
    
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":  
    print("Prime Number Checker")
    prime_num()
