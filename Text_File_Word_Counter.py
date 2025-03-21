filename: str = input("Enter the name of the file: ")
with open(filename, "r") as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    print(f"Word count: {word_count}")