def tip() -> None:
    print("Tip calculator.")
    item = int(input("Enter the number of items purchased: "))
    total = 0
    bill_list: list = []
    for i in range(1, item + 1):
        price = float(input(f"Enter the price of item {i}: "))
        bill_list.append(price)
        total += price
    tip = total * 0.15
    print("Bill list: ", bill_list)
    print(f"Total Bill : {total}")
    print(f"Tip        : {tip:.2f}")
    print(f"Total      : {total + tip}")
if __name__ == "__main__":
    tip()