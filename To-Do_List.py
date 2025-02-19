from datetime import datetime
def to_do() ->None:
    x = datetime.now()
    print(x.strftime("%Y-%m-%d %H:%M"))
    choice: int = int(input("Show list-1, Make list-2: "))
    lis: list = []
    def list_input(lis: list) -> list:
            row_num: int = int(input("Enter the number of task u have at hand: "))
            for i in range(1, row_num+1):
                task_name: str = input("Write here: ")
                lis.append(task_name)
            return lis
    if choice == 2:
        list_input(lis)
    elif choice == 1:
         pass
to_do()