from datetime import datetime
def grocery() -> None:

    x = datetime.now()
    print(x.strftime("%Y-%m-%d"))
    lis: list = []

    def list_input(lis: list) -> list:
        row_num: int = int(input("Enter the number of items you have to buy: "))
        for i in range(1, row_num + 1):
            item_name: str = input("Write here: ")
            lis.append(item_name)
        return lis

    def ask(lis1) -> None:
        import platform
        import os  

        def save(data):
            base_name = "contact_list"
            counter = 1
            
            if platform.system() == "Windows":
                while os.path.exists(f"{base_name}_{counter}.txt"):
                    counter += 1
                filename = f"{base_name}_{counter}.txt"
            
            else:  # macOS and Linux
                directory = os.path.expanduser("~/Documents/")  # Save in ~/Documents/
                os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
                while os.path.exists(os.path.join(directory, f"{base_name}_{counter}.txt")):
                    counter += 1
                filename = os.path.join(directory, f"{base_name}_{counter}.txt")

            with open(filename, "w") as file:
                file.write(str(data))

            print(f"Data saved to: {filename}")
        choice: int = int(input("1.Show grocery list\n2.Save it.\nAnswer: "))
        if choice == 1:
            print(lis1)
        if choice == 2:
            save(lis1)

    grocery_lis = list_input(lis)
    ask(grocery_lis)


if __name__ == "__main__":
    grocery()