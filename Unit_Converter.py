def get_input() -> None:
    while True:
        try:
            convert: str = input("What do you want to convert into(Mass, Lenght, Volume)?: ")
            if convert == "Mass":
                from_mass: str = input("Enter the unit you want to convert from(g, kg, t, US t, UK t, oz, lb): ")
                to_mass: str = input("Enter the unit you want to convert to(g, kg, t, US t, UK t, oz, lb): ")
                mass: float = float(input("Enter the value you want to convert: "))
                if from_mass in ["g", "kg", "t", "US t", "UK t", "oz", "lb"] and to_mass in ["g", "kg", "t", "US t", "UK t", "oz", "lb"]:
                    mass_convertion(from_mass, to_mass, mass)
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
                from_volume: str = input("Enter the unit you want to convert from(g, kg, t, US t, UK t, oz, lb): ")
                to_volume: str = input("Enter the unit you want to convert to(g, kg, t, US t, UK t, oz, lb): ")
                volume: float = float(input("Enter the value you want to convert: "))
                if from_volume in ["g", "kg", "t", "US t", "UK t", "oz", "lb"] and to_volume in ["g", "kg", "t", "US t", "UK t", "oz", "lb"]:
                    volume_convertion(from_volume, to_volume, volume)
                    break
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a valid number")
def mass_convertion(from_mass: str, to_mass: str, mass: float) -> float:
    pass
def lenght_convertion(from_lenght: str, to_lenght: str, lenght: float) -> float:
    pass
def volume_convertion(from_volume: str, to_volume: str, volume: float) -> float:
    pass
if __name__ == "__main__":
    get_input()