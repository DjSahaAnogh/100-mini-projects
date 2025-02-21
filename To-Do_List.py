from datetime import datetime
import os

def to_do() -> None:
    x = datetime.now()
    print(x.strftime("%Y-%m-%d %H:%M"))
    lis: list = []

    def list_input(lis: list) -> list:
        row_num: int = int(input("Enter the number of task you have at hand: "))
        for i in range(1, row_num + 1):
            task_name: str = input("Write here: ")
            lis.append(task_name)
        return lis

    def ask(lis1) -> None:
        def save(data):
            base_name = "data"
            counter = 1
            while os.path.exists(f"{base_name}_{counter}.txt"):
                counter += 1
            filename = f"{base_name}_{counter}.txt"
            with open(filename, "w") as file:
                file.write(str(data))

        choice: int = int(input("1.Show to-do list\n2.Save it.\nAnswer: "))
        if choice == 1:
            print(lis1)
        if choice == 2:
            save(lis1)

    to_do_lis = list_input(lis)
    ask(to_do_lis)
if __name__ == "__main__":
    to_do()