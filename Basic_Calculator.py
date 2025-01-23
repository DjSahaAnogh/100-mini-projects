def add(a: int, b: int) -> int:
    return a + b
def sub(a: int, b: int) -> int:
    return a - b
def mul(a: int, b: int) -> int:
    return a * b
def div(a: int, b: int) -> int:
    return a / b
def mod(a: int, b: int) -> int:
    return a % b
def power(a: int, b: int) -> int:
    return a ** b
def floor_div(a: int, b: int) -> int:
    return a // b
def get_input() -> None:
    try:
        num1: int = int(input("Enter first number: "))
        num2: int = int(input("Enter second number: "))
        operators: str = input("Enter operator(+, -, *, /, %, //, ^): ")
        return num1, num2, operators
    except ValueError:
        print("Please enter a valid number")
        return get_input()
if __name__ == "__main__":
    while True:
        num1, num2, operators = list(get_input())
        if operators == "+":
            print(add(num1, num2))
            break
        elif operators == "-":
            print(sub(num1, num2))
            break
        elif operators == "*":
            print(mul(num1, num2))
            break
        elif operators == "/":
            if num2 == 0:
                print("Division by zero is not allowed")
                break
            print(div(num1, num2))
            break
        elif operators == "%":
            if num2 == 0:
                print("Division by zero is not allowed")
            print(mod(num1, num2))
            break
        elif operators == "^":
            print(power(num1, num2))
            break
        elif operators == "//":
            if num2 == 0:
                print("Division by zero is not allowed")
            print(floor_div(num1, num2))
            break
        else:
            print("Invalid operator")