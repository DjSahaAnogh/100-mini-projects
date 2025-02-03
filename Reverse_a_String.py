def str_revers() -> str:
    text: str = input("Enter you string: ")
    new_str: str = text[::-1]
    return f"The reversed string is: '{new_str}'"
if __name__ == "__main__":
    print(str_revers())