def tip() -> None:
    print("Tip calculator.")
    item = int(input("Enter the nu,ber of items purchased: "))
    total = 0
    for i in range(1, item + 1):
        price = float(input(f"Enter the price of item {i}: "))
        total += price
    tip = total * 0.15
    print(f"Tip: {tip}")
    print(f"Total: {total + tip}")
if __name__ == "__main__":
    tip()