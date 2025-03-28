import csv
import platform
import os

def read_csv() -> None:
    filename = input("Enter the name of the file you want to read: ")

    # Read CSV file properly
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)  # Convert to list of lists

    def extract_data(data, indices):
        extracted_data = []
        for row in data[1:]:  # Skip header row
            extracted_data.append([row[i] for i in indices])
        return extracted_data
    
    def write_to_csv(header, extracted_data):
        count = 1  # Start file numbering
        base_filename = "extracted_data"

        # Determine OS-specific file path
        if platform.system() == "Windows":
            output_filename = f"{base_filename}{count}.csv"
            while os.path.exists(output_filename):  # Ensure unique filename
                count += 1
                output_filename = f"{base_filename}{count}.csv"
        else:  # macOS / Linux
            directory = os.path.expanduser("~/Documents/")  # Save in ~/Documents/
            os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
            output_filename = os.path.join(directory, f"{base_filename}{count}.csv")
            
            while os.path.exists(output_filename):  # Ensure unique filename
                count += 1
                output_filename = os.path.join(directory, f"{base_filename}{count}.csv")

        # Debugging: Print where the file is being saved
        print(f"Saving file to: {output_filename}")

        # Write extracted data to the CSV file
        try:
            with open(output_filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)  # Write column headers
                writer.writerows(extracted_data)  # Write data
            
            print(f"✅ Extracted data saved to: {output_filename}")
        except Exception as e:
            print(f"❌ Error writing file: {e}")

    def ask():
        header = data[0]  # First row contains column names
        print("\nAvailable columns:", ", ".join(header))  # Display headers to the user

        question = input("Do you want to extract data? (yes/no): ").strip().lower()
        if question == "yes":
            column_names = input("Enter the column names you want to extract (comma-separated): ").split(',')
            column_names = [col.strip() for col in column_names]  # Remove extra spaces

            # Get column indices
            indices = [header.index(col) for col in column_names if col in header]

            if not indices:
                print("❌ No valid columns found! Please enter correct column names.")
                return

            extracted = extract_data(data, indices)
            write_to_csv(column_names, extracted)

    ask()

if __name__ == '__main__':
    read_csv()
