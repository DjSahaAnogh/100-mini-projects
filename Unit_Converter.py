def get_input() -> None:
    while True:
        try:
            convert: str = input("What do you want to convert into(Mass, Lenght, Volume)?: ")
            if convert == "Mass":
                from_mass: str = input("Enter the unit you want to convert from(g, kg, t, US t, UK t, oz, lb): ")
                to_mass: str = input("Enter the unit you want to convert to(g, kg, t, US t, UK t, oz, lb): ")
                mass: float = float(input("Enter the value you want to convert: "))
                if from_mass in ["g", "kg", "t", "US t", "UK t", "oz", "lb"] and to_mass in ["g", "kg", "t", "US t", "UK t", "oz", "lb"]:
                    print(mass_convertion(from_mass, to_mass, mass))
                    break
                else:
                    print("Invalid input")
            elif convert == "Lenght":
                from_lenght: str = input("Enter the unit you want to convert from(cm, m, km, in, ft, yd, mi): ")
                to_lenght: str = input("Enter the unit you want to convert to(cm, m, km, in, ft, yd, mi): ")
                lenght: float = float(input("Enter the value you want to convert: "))
                if from_lenght in ["cm", "m", "km", "in", "ft", "yd", "mi"] and to_lenght in ["cm", "m", "km", "in", "ft", "yd", "mi"]:
                    lenght_convertion(from_lenght, to_lenght, lenght)
                    break
                else:
                    print("Invalid input")
            elif convert == "Volume":
                from_volume: str = input("Enter the unit you want to convert from(ml, l, m3, in3, ft3, yd3, gal, qt): ")
                to_volume: str = input("Enter the unit you want to convert to(ml, l, m3, in3, ft3, yd3, gal, qt): ")
                volume: float = float(input("Enter the value you want to convert: "))
                if from_volume in ["ml", "l", "m3", "in3", "ft3", "yd3", "gal", "qt"] and to_volume in ["ml", "l", "m3", "in3", "ft3", "yd3", "gal", "qt"]:
                    result = volume_convertion(from_volume, to_volume, volume)
                    print(result)
                    break
                else:
                    print("Invalid input")
        except ValueError:
            print("Please enter a valid number")
def mass_convertion(from_mass: str, to_mass: str, mass: float) -> float:
    conversion_factors = {
        "g": 1,
        "kg": 1000,
        "t": 1000000,
        "US t": 907185,
        "UK t": 1016047,
        "oz": 28.35,
        "lb": 453.592
    }
    
    if from_mass in conversion_factors and to_mass in conversion_factors:
        result: float = mass * conversion_factors[from_mass] / conversion_factors[to_mass]
        return f"{result:.8f} {to_mass}"
    else:
        return mass

def lenght_convertion(from_lenght: str, to_lenght: str, lenght: float) -> float:
    conversion_factors = {
        "mm": 1,
        "cm": 10,
        "m": 1000,
        "km": 1000000,
        "in": 25.4,
        "ft": 304.8,
        "yd": 914.4,
        "mi": 1609344
    }
    
    if from_lenght in conversion_factors and to_lenght in conversion_factors:
        result: float = lenght * conversion_factors[from_lenght] / conversion_factors[to_lenght]
        return f"{result:.8f} {to_lenght}"
    else:
        return lenght

def volume_convertion(from_volume: str, to_volume: str, volume: float) -> float:
    conversion_factors = {
        "ml": 1,
        "l": 1000,
        "m3": 1000000,
        "in3": 16.387,
        "ft3": 28316.8,
        "yd3": 764554.858,
        "gal": 3785.41,
        "qt": 946.353
    }
    
    if from_volume in conversion_factors and to_volume in conversion_factors:
        result: float = volume * conversion_factors[from_volume] / conversion_factors[to_volume]
        return f"{result:.8f} {to_volume}"
    else:
        return volume
if __name__ == "__main__":
    print("Unit Converter \nIt can convert Mass, Lenght and Volume. \nPlease enter the unit you want to convert from and to according to the format in which the units are written.")
    get_input()