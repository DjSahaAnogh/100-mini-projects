def fibonacci() -> int:
    n: int = int(input("The number of terms: "))
    x: int = 0
    y: int = 1
    print(x)
    for i in range(1, n):
        x , y = y, (x+y)
        print(x)
if __name__ == "__main__":
    fibonacci()