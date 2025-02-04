def max_num() -> int:
    num_list: list = input("Enter the numbers separated by space: ").split(" ")
    num_list = [int(i) for i in num_list]
    num_list.sort()
    return f"The largest number is {num_list[-1]}"
if __name__ == "__main__":
    print(max_num())