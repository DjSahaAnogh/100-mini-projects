def caps() -> None:
    text: str = input("Enter a paragraph: ")
    text = text.split(". ")
    for i in range(len(text)):
        text[i] = text[i].capitalize()
    text = ". ".join(text)
    print(text)

if __name__ == "__main__":
    caps()