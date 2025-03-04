def code() -> str:
    text: str = input("Enter the text you want to code: ")
    shift: int = int(input("Enter the shift: "))
    result: str =""
    for i in range(len(text)):
        if text[i].isalpha():
            shift_base: int = ord("A") if text[i].isupper() else ord("a")
            result += chr((ord(text[i]) - shift_base + shift) % 26 + shift_base)
        else:
            result += text[i]
    return result

if __name__ == "__main__":
    print(code())