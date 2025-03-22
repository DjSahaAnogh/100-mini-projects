from cryptography.fernet import Fernet

def generate_key() -> None:
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()  # Load the secret key
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()  # Read file content

    encrypted_data = cipher.encrypt(file_data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)
    print(f"File '{filename}' encrypted successfully!")

def decrypt_file(filename):
    key = load_key()  # Load the secret key
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)  # Decrypt the content

    original_filename = filename.replace(".enc", "")  # Remove .enc extension
    with open(original_filename, "wb") as file:
        file.write(decrypted_data)  # Save decrypted data

    print(f"File '{filename}' decrypted successfully!")

if __name__ == "__main__":
    generate_key()
    # encrypt_file("contact_list_1.txt")
    # decrypt_file("contact_list_1.txt.enc")  # Decrypt the file