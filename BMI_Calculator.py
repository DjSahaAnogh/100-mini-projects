def bmi() -> None:
    while True:
        try:
            height: float = float(input("Enter your height in m: "))
            weight: float = float(input("Enter your weight in kg: "))
            if height <= 0 or weight <= 0:
                print("Invalid input. Please enter a positive number.")
            else:
                bmi = weight / (height ** 2)
                print(f"Your BMI is {bmi:.2f}")
                if bmi < 18.5:
                    print("You are underweight.")
                    break
                elif bmi < 25:
                    print("You are normal weight.")
                    break
                elif bmi < 30:
                    print("You are overweight.")
                    break
                else:
                    print("You are obese.")
                    break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    bmi()