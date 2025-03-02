def binary2decimal() -> None:
    while True:
        binar: str = input("Enter a binary number: ")
        def is_binary(binar: str) -> bool:
            for i in binar:
                if i not in "01":
                    return False
            return True
        decimal: int = 0
        if is_binary(binar) == False:
            print("Invalid binary number")
        else:
            for i in range(len(binar)):
                decimal += int(binar[i]) * 2 ** (len(binar) - i - 1)
            print(f"Decimal equivalent of {binar} is {decimal}")
            break
    if input("Do you want to convert another binary number? (y/n): ") == "y":
        binary2decimal()

if __name__ == "__main__":
    binary2decimal()