import os  
import platform
def contact_app():
    print("Welcome to the Contact App")
    pairs = input("Enter key-value pairs (comma-separated, like name:John,age:25): ")
    contact_dic : dict = {key: value for key, value in (pair.split(":") for pair in pairs.split(","))}
    def save(data):
        base_name = "contact_list"
        counter = 1
        
        if platform.system() == "Windows":
            while os.path.exists(f"{base_name}_{counter}.txt"):
                counter += 1
            filename = f"{base_name}_{counter}.txt"
        
        else:  # macOS and Linux
            directory = os.path.expanduser("~/Documents/")  # Save in ~/Documents/
            os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
            while os.path.exists(os.path.join(directory, f"{base_name}_{counter}.txt")):
                counter += 1
            filename = os.path.join(directory, f"{base_name}_{counter}.txt")

        with open(filename, "w") as file:
            file.write(str(data))

        print(f"Data saved to: {filename}")
    save(contact_dic)
    print("Contact saved successfully")
    print("Thank you for using the Contact App")
if __name__ == "__main__":
    contact_app()