def collatz_conjecture_sequence():
    n: int = int(input("Enter a positive number: "))
    if n<= 0:
        print("Please enter a positive number.")
        return
    sequence: list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    print(sequence)
if __name__ == "__main__":
    collatz_conjecture_sequence()