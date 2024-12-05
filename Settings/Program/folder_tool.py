# /Settings/Program/folder_tool.py

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

def main():
    action = input("Do you want to (e)ncrypt or (d)ecrypt a folder? ").strip().lower()
    
    if action not in ['e', 'd']:
        print("Invalid action. Please type 'e' to encrypt or 'd' to decrypt.")
        return

    folder_path = input("Which folder do you want to process? ").strip()
    
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    password = input("Choose your password: ").strip()

    if action == 'e':
        encrypt_folder(folder_path, password)
    elif action == 'd':
        decrypt_folder(folder_path, password)

if __name__ == "__main__":
    main()
