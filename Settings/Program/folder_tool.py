from cryptography.fernet import Fernet
import os

def generate_key(password):
    return Fernet(Fernet.generate_key())

def encrypt_folder(folder_path, password):
    key = generate_key(password)
    fernet = Fernet(key)
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)
        
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    
    print("Folder encrypted.")

def decrypt_folder(folder_path, password):
    key = generate_key(password)
    fernet = Fernet(key)
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as file:
            encrypted = file.read()
        
        decrypted = fernet.decrypt(encrypted)
        
        with open(file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
    
    print("Folder decrypted.")

if __name__ == "__main__":
    action = input("Do you want to (e)ncrypt or (d)ecrypt a folder? ")
    folder_path = input("Enter the folder path: ")
    password = input("Enter a password: ")

    if action.lower() == 'e':
        encrypt_folder(folder_path, password)
    elif action.lower() == 'd':
        decrypt_folder(folder_path, password)
    else:
        print("Invalid action.")
