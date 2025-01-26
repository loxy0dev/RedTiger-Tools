# Copyright (c) RedTiger (https://redtiger.shop)
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
    Slow(f"""{decrypted_banner}
 {BEFORE}01{AFTER}{white} BCRYPT
 {BEFORE}02{AFTER}{white} MD5
 {BEFORE}03{AFTER}{white} SHA-1
 {BEFORE}04{AFTER}{white} SHA-256
 {BEFORE}05{AFTER}{white} PBKDF2 (SHA-256)
 {BEFORE}06{AFTER}{white} Base64 Decode
    """)

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Encryption Method -> {reset}")

    if choice not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        ErrorChoice()

    encrypted_password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Encrypted Password -> {white}")

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {white}"))
    except:
        ErrorNumber()
    
    try:
        characters_number_min = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password Characters Number Min -> {white}"))
    except:
        ErrorNumber()

    try:
        characters_number_max = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password Characters Number Max -> {white}"))
    except:
        ErrorNumber()

    Title(f"Password Decrypted - Encrypted Password: {encrypted_password}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Password cracking by brute force.. (very long depending on the number of characters){reset}")

    password = False
    generated_passwords = set()

    salt = "this_is_a_salt".encode('utf-8')
    all_characters = string.ascii_letters + string.digits + string.punctuation
    all_characters_len = len(all_characters)

    def ErrorDecrypted():
        encryption_map = {
            '1': 'BCRYPT', '2': 'MD5', '3': 'SHA-1', '4': 'SHA-256', '5': 'PBKDF2 (SHA-256)', '6': 'Base64 Decode'
        }
        encryption = encryption_map.get(choice, "Unknown")
        print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} The encryption "{white}{encrypted_password}{red}" is not accepted by "{white}{encryption}{red}".')
        Continue()
        Reset()

    def CheckPassword(password_test):
        try:
            if choice in ['1', '01']:
                return bcrypt.checkpw(password_test.encode('utf-8'), encrypted_password.encode('utf-8'))
            elif choice in ['2', '02']:
                return hashlib.md5(password_test.encode('utf-8')).hexdigest() == encrypted_password
            elif choice in ['3', '03']:
                return hashlib.sha1(password_test.encode('utf-8')).hexdigest() == encrypted_password
            elif choice in ['4', '04']:
                return hashlib.sha256(password_test.encode('utf-8')).hexdigest() == encrypted_password
            elif choice in ['5', '05']:
                return pbkdf2_hmac('sha256', password_test.encode('utf-8'), salt, 100000).hex() == encrypted_password
            elif choice in ['6', '06']:
                return base64.b64decode(encrypted_password.encode('utf-8')).decode('utf-8') == password_test
            return False
        except:
            ErrorDecrypted()

    def GeneratePassword(characters_number_min, characters_number_max):
        return ''.join(random.choice(all_characters) for _ in range(random.randint(characters_number_min, characters_number_max)))

    def TestDecrypted():
        global password
        print(red)
        while not password:
            password_test = GeneratePassword(characters_number_min, characters_number_max)
            if password_test not in generated_passwords:
                generated_passwords.add(password_test)
                if CheckPassword(password_test):
                    password = True
                    time.sleep(0.5)
                    print(f'{BEFORE + current_time_hour() + AFTER} {ADD} Password: {white}{password_test}{reset}')
                    time.sleep(1)
                    Continue()
                    Reset()

    def Request():
        try:
            with ThreadPoolExecutor(max_workers=threads_number) as executor:
                executor.map(lambda _: TestDecrypted(), range(threads_number))
        except Exception as e:
            ErrorNumber()

    while not password:
        Request()

except Exception as e:
    Error(e)
