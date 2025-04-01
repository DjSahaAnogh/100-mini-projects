def search() -> None:
    file_name = input("Enter the file's name: ")
    with open(file_name, "r") as file:
        text = file.read().splitlines()
    search_term = input("Type here to search: ")
    results = [line for line in text if search_term in line]
    if results:
        print("Results found:")
        for line in results:
            print(line)
    else:
        print("No results found.")

if __name__ == "__main__":
    search()