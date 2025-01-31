def word() -> None:
    text: str = input("Enter a sentence: ")
    words: list = text.split(" ")
    print(f"Number of words: {len(words)}")
if __name__ == "__main__":
    print("Word Counter")
    word()