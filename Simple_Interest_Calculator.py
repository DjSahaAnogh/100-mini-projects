def interst() -> None:
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time period: "))
    print(f"Simple Interest: {p*r*t/100}")
    print(f"Total Amount: {p + p*r*t/100}")
if __name__ == "__main__":
    print("Simple Interest Calculator")
    interst()