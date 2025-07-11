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
    import rarfile
    import pyzipper
    import string
    import tkinter
    from tkinter import filedialog
    from concurrent.futures import ThreadPoolExecutor
except Exception as e:
    ErrorModule(e)

Title(f"Password Zip Cracked Attack")

try:
    def ChooseZipRarFile():
        try:
            print(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Enter the path to the .zip or .rar file -> {reset}")
            if sys.platform.startswith("win"):
                root = tkinter.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))
                root.withdraw()
                root.attributes('-topmost', True)
                file = filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} - Choose an icon (.zip / .rar)", filetypes=[("ZIP/RAR files", "*.zip;*.rar"), ("ZIP files", "*.zip"), ("RAR files", "*.rar")])
            elif sys.platform.startswith("linux"):
                file = filedialog.askopenfilename(title=f"{name_tool} {version_tool} - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} File path: {white + file}")
            return file
        except:
            return input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter the path to the .zip or .rar file -> {reset}")

    def CountEncryptedFiles(file):
        count = 0
        try:
            if file.lower().endswith('.zip'):
                with pyzipper.AESZipFile(file) as archive:
                    for filename in archive.namelist():
                        try:
                            archive.extract(filename, pwd=b'wrongpassword')  
                        except RuntimeError: 
                            count += 1
            elif file.lower().endswith('.rar'):
                with rarfile.RarFile(file) as archive:
                    for filename in archive.namelist():
                        try:
                            archive.extract(filename, pwd='wrongpassword')  
                        except rarfile.BadPassword:  
                            count += 1
            return count
        except:
            return count
        
    def CheckPassword(file, password_test):
        global password_found
        try:
            if file.lower().endswith('.zip'):
                with pyzipper.AESZipFile(file) as archive:
                    for filename in archive.namelist():
                        try:
                            archive.extract(filename, pwd=password_test.encode())
                            password_found += 1
                            print(f'{BEFORE + current_time_hour() + AFTER} {ADD} File: {white + filename} {red}Password: {white + password_test + reset}')
                        except:
                            pass
            elif file.lower().endswith('.rar'):
                with rarfile.RarFile(file) as archive:
                    for filename in archive.namelist():
                        try:
                            archive.extract(filename, pwd=password_test.encode())
                            password_found += 1
                            print(f'{BEFORE + current_time_hour() + AFTER} {ADD} File: {white + filename} {red}Password: {white + password_test + reset}')
                        except:
                            pass
            return password_found > 0
        except:
            return False

    def RandomCharacter(count):
        global generated_passwords, password_found
        try:
            threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
            characters_number_min = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password Characters Number Min -> {reset}"))
            characters_number_max = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password Characters Number Max -> {reset}"))
        except:
            ErrorNumber()

        generated_passwords = set()
        password_found = 0
        all_characters = string.ascii_letters + string.digits + string.punctuation

        def GeneratePassword():
            return ''.join(random.choice(all_characters) for _ in range(random.randint(characters_number_min, characters_number_max)))

        def TestCracked():
            global generated_passwords, password_found
            while password_found < count:
                password_test = GeneratePassword()
                if password_test not in generated_passwords:
                    generated_passwords.add(password_test)
                    if CheckPassword(file, password_test):
                        if password_found == count:
                            Continue()
                            Reset()

        def Request():
            with ThreadPoolExecutor(max_workers=threads_number) as executor:
                executor.map(lambda _: TestCracked(), range(threads_number))

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Brute force password cracking in progress.. (It can be long){reset}")
        while password_found < count:
            Request()

    def WorldList():
        global password_found
        path_folder_worldlist = os.path.join(tool_path, "2-Input", "WorldList")
        files = [f for f in os.listdir(path_folder_worldlist) if os.path.isfile(os.path.join(path_folder_worldlist, f))]
        password_found = 0
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Add more list in folder: {white + path_folder_worldlist}")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Password cracking by world list in progress.. (It can be long){reset}")

        for file_list in files:
            try:
                with open(os.path.join(path_folder_worldlist, file_list), 'r', encoding='utf-8') as f:
                    for line in f:
                        if CheckPassword(file, line.strip()):
                            if password_found == count:
                                Continue()
                                Reset()
            except:
                pass

        if not password_found:
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The entire world list has been checked and no passwords match.")
            Continue()
            Reset()

    Slow(decrypted_banner)
    file = ChooseZipRarFile()
    
    count = CountEncryptedFiles(file)
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Number of files protected by password: {white + str(count)}")
    if count == 0:
        Continue()
        Reset()

    Title(f"Password Zip Cracked Attack - File: {file}")

    print(f"""
 {BEFORE}01{AFTER + white} Random Character
 {BEFORE}02{AFTER + white} World List
 """)

    method = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Method -> {white}")

    if method in ["01", "1"]:
        RandomCharacter(count)
    elif method in ["02", "2"]:
        WorldList()
    else:
        ErrorChoice()

except Exception as e:
    Error(e)

