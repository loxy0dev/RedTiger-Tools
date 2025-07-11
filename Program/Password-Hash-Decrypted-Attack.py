# Copyright (c) RedTiger 
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import bcrypt
    import hashlib
    import random
    import string
    from concurrent.futures import ThreadPoolExecutor
    import time
    import base64
    from hashlib import pbkdf2_hmac
except Exception as e:
    ErrorModule(e)

Title(f"Password Decrypted")

try:
    def ErrorDecrypted():
        encryption_map = {
            '1': 'BCRYPT', '2': 'MD5', '3': 'SHA-1', '4': 'SHA-256', '5': 'PBKDF2 (SHA-256)', '6': 'Base64 Decode'
        }
        encryption = encryption_map.get(choice, "Unknown")
        print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} The encryption "{white + encrypted_password + red}" is not accepted by "{white + encryption + red}".')
        Continue()
        Reset()

    def CheckPassword(password_test):
        global salt
        try:
            methods = {
                '1': lambda pwd: bcrypt.checkpw(pwd.encode('utf-8'), encrypted_password.encode('utf-8')),
                '2': lambda pwd: hashlib.md5(pwd.encode('utf-8')).hexdigest() == encrypted_password,
                '3': lambda pwd: hashlib.sha1(pwd.encode('utf-8')).hexdigest() == encrypted_password,
                '4': lambda pwd: hashlib.sha256(pwd.encode('utf-8')).hexdigest() == encrypted_password,
                '5': lambda pwd: pbkdf2_hmac('sha256', pwd.encode('utf-8'), salt, 100000).hex() == encrypted_password,
                '6': lambda pwd: base64.b64decode(encrypted_password.encode('utf-8')).decode('utf-8') == pwd
            }
            return methods.get(choice, lambda _: False)(password_test)
        except:
            ErrorDecrypted()
    
    def RandomCharacter():
        global password, salt
        try:
            threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {white}"))
            characters_number_min = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password Characters Number Min -> {white}"))
            characters_number_max = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password Characters Number Max -> {white}"))
        except:
            ErrorNumber()

        password = False
        generated_passwords = set()
        salt = "this_is_a_salt".encode('utf-8')
        all_characters = string.ascii_letters + string.digits + string.punctuation

        def GeneratePassword():
            return ''.join(random.choices(all_characters, k=random.randint(characters_number_min, characters_number_max)))
        
        def TestDecrypted():
            global password
            while not password:
                password_test = GeneratePassword()
                if password_test not in generated_passwords:
                    generated_passwords.add(password_test)
                    if CheckPassword(password_test):
                        password = True
                        time.sleep(0.5)
                        print(f'{BEFORE + current_time_hour() + AFTER} {ADD} Password: {white + password_test + reset}')
                        time.sleep(1)
                        Continue()
                        Reset()

        def Request():
            try:
                with ThreadPoolExecutor(max_workers=threads_number) as executor:
                    executor.map(lambda _: TestDecrypted(), range(threads_number))
            except Exception:
                ErrorNumber()

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Brute force password cracking in progress.. (It can be long){reset}")
        while not password:
            Request()

    def WorldList():
        path_folder_worldlist = os.path.join(tool_path, "2-Input", "WorldList")
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Add more list in folder: {white + path_folder_worldlist}")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Password cracking by world list in progress.. (It can be long){reset}")
        
        for file in os.listdir(path_folder_worldlist):
            try:
                file_path = os.path.join(path_folder_worldlist, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if CheckPassword(line.strip()):
                            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Password: {white + line.strip() + reset}")
                            Continue()
                            Reset()
                            return
            except:
                pass
        
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The entire world list has been checked and no passwords match.")
        Continue()
        Reset()
        
    Slow(f"""{decrypted_banner}
 {BEFORE}01{AFTER + white} BCRYPT
 {BEFORE}02{AFTER + white} MD5
 {BEFORE}03{AFTER + white} SHA-1
 {BEFORE}04{AFTER + white} SHA-256
 {BEFORE}05{AFTER + white} PBKDF2 (SHA-256)
 {BEFORE}06{AFTER + white} Base64 Decode
    """)
    
    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Method -> {reset}")

    if choice not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        ErrorChoice()

    encrypted_password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Encrypted Password -> {white}")
    Title(f"Password Decrypted - Encrypted Password: {encrypted_password}")

    print(f"""
 {BEFORE}01{AFTER + white} Random Character
 {BEFORE}02{AFTER + white} World List
 """)

    method = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Brute Force Method -> {white}")

    if method in ["01", "1"]:
        RandomCharacter()
    elif method in ["02", "2"]:
        WorldList()
    else:
        ErrorChoice()

except Exception as e:
    Error(e)
