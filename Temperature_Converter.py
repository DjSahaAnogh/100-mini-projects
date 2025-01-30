def tum_conver() -> float:
    print("You can do the following conversions: \n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius \n3. Celsius to Kelvin\n4. Kelvin to Celsius\n5. Fahrenheit to Kelvin\n6. Kelvin to Fahrenheit")
    temp: float = float(input("Enter the temperature: "))
    from_temp: str = input("Enter the number of the conversion you want to do: ")
    to_temp: str = input("Enter the number of the conversion you want to do: ")
    if from_temp == "Celsius":
        if to_temp == "Fahrenheit":
            return str((temp * 9/5) + 32) + f" {to_temp}"
        elif to_temp == "Kelvin":
            return str(temp + 273.15) + f" {to_temp}"    
    elif from_temp == "Fahrenheit":
        if to_temp == "Celsius":
            return str((temp - 32) * 5/9) + f" {to_temp}"
        elif to_temp == "Kelvin":
            return str((temp - 32) * 5/9) + 273.15 + f" {to_temp}"
    elif from_temp == "Kelvin":
        if to_temp == "Celsius":
            return str(temp - 273.15) + f" {to_temp}"
        elif to_temp == "Fahrenheit":
            return str((temp - 273.15) * 9/5 + 32) + f" {to_temp}"
    else:
        return temp
if __name__ == "__main__":
    print("Temperature Converter")
    print(f"Converted tempreture: {tum_conver()}")    