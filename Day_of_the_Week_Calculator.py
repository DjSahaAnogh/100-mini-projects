def find_day_of_week() -> None:
    date: str = input("Enter the date in the format 'dd/mm/yyyy': ")
    day: int = int(date.split("/")[0])
    month: int = int(date.split("/")[1])
    year: int = int(date.split("/")[2])

    if month < 3:
        month += 12
        year -= 1
    K: int = year % 100 # k is the year of the century
    J: int = year // 100 # j is the century
    h = (day + (13 * (month + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7
    days: list = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(f"The day of the week on {date} is {days[h]}")

if __name__ == "__main__":
    find_day_of_week()
