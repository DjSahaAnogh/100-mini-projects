def leap_year() -> None:
    year = int(input("Enter the year: "))
    if year % 4 == 0:
        print(f"The year {year} is a Leap Year.")
    else:
        print(f"The year {year} is not a Leap Year.")
if __name__ == "__main__":
    leap_year()