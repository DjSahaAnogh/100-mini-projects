def vowel() -> None:
    text: list = list(input("Enter a text: "))
    vowels: list = ['a', 'e', 'i', 'o', 'u']
    count: int = 0
    for i in text:
        if i in vowels:
            count += 1
    print(f"Number of vowels in the text: {count}")
if __name__ == "__main__":
    vowel()