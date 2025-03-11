def exchange():
    while True:
        user_input: str = input("Availlable excange rates: \n1. USD to BDT\n2. BDT to USD\n3. USD to EUR\n4. EUR to USD\n5. USD to GBP\n6. GBP to USD\nEnter your choice: ")
        try:
            if user_input == "1":
                usd: float = float(input("Enter the amount of USD: "))
                bdt: float = usd * 121.50
                print(f"{usd} USD = {bdt:.2f} BDT")
                break
            elif user_input == "2":
                bdt: float = float(input("Enter the amount of BDT: "))
                usd: float = bdt / 121.50
                print(f"{bdt} BDT = {usd:.2f} USD")
                break
            elif user_input == "3":
                usd: float = float(input("Enter the amount of USD: "))
                eur: float = usd * 1.089
                print(f"{usd} USD = {eur:.2f} EUR")
                break
            elif user_input == "4":
                eur: float = float(input("Enter the amount of EUR: "))
                usd: float = eur / 1.089
                print(f"{eur} EUR = {usd:.2f} USD")
                break
            elif user_input == "5":
                usd: float = float(input("Enter the amount of USD: "))
                gbp: float = usd * 1.291
                print(f"{usd} USD = {gbp:.2f} GBP")
                break
            elif user_input == "6":
                gbp: float = float(input("Enter the amount of GBP: "))
                usd: float = gbp / 1.291
                print(f"{gbp} GBP = {usd:.2f} USD")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    exchange()