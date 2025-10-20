import random
def pass_lenght() -> int:
    while True: 
        try:
            length: int = int(input("Enter the length of password: "))
            return length
        except ValueError:
            print("Please enter a valid number")
            continue
def pass_generator(pass_len: int) -> str:
    caps_letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters: str = "abcdefghijklmnopqrstuvwxyz"
    digits: str = "0123456789"
    symbols: str = "!@#$%^&*()_+"
    password: str = random.choice(caps_letters) + random.choice(small_letters) + random.choice(digits) + random.choice(symbols)
    if pass_len-4 == 0:
        password_list: list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)
        return password
    elif pass_len - 4 < 0:
        print("Password length must be at least 4 characters to include all character types.")
        return ""
    else:
        for i in range(pass_len - 4):
            password += random.choice(caps_letters + small_letters + digits + symbols)
        password_list: list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)
        return password
if __name__ == "__main__":
    length: int = pass_lenght()
    password: str = pass_generator(length)
    print(f"Your generated password is: {password}")