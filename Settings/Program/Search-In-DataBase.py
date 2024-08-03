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

Title("Search DataBase")

try:
    folder_database_relative = "./2-Input/DataBase"
    folder_database = os.path.abspath(folder_database_relative)

    print(f"""
{BEFORE + current_time_hour() + AFTER} {INFO} Add DataBase to the "{white}{folder_database_relative}{red}" folder.
{BEFORE + current_time_hour() + AFTER} {INFO} If you don't have a DataBase you can get one on the Discord Server "{white}{discord_server}{red}\".""")
    search = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Search -> {reset}")

    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in DataBase..")

    def TitleSearch(files_searched, element):
        Title(f"Search DataBase | Total: {files_searched} | File: {element}")

    try:
        files_searched = 0

        def check(folder):
            global files_searched
            results_found = False
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in {white}{folder}")
            for element in os.listdir(folder):
                chemin_element = os.path.join(folder, element)
                if os.path.isdir(chemin_element):
                    check(chemin_element)
                elif os.path.isfile(chemin_element):
                    try:
                        with open(chemin_element, 'r', encoding='utf-8') as file:
                            line_number = 0
                            files_searched += 1
                            TitleSearch(files_searched, element)
                            for line in file:
                                line_number += 1
                                if search in line:
                                    results_found = True
                                    line_info = line.strip().replace(search, f"{color.YELLOW}{search}{white}")
                                    print(f"""{red}
- Folder : {white}{folder}{red}
- File   : {white}{element}{red}
- Line   : {white}{line_number}{red}
- Result : {white}{line_info}
    """)
                    except UnicodeDecodeError:
                        try:
                            with open(chemin_element, 'r', encoding='latin-1') as file:
                                files_searched += 1
                                line_number = 0
                                TitleSearch(files_searched, element)
                                for line in file:
                                    line_number += 1
                                    if search in line:
                                        results_found = True
                                        line_info = line.strip().replace(search, f"{color.YELLOW}{search}{white}")
                                        print(f"""{red}
- Folder : {white}{folder}{red}
- File   : {white}{element}{red}
- Line   : {white}{line_number}{red}
- Result : {white}{line_info}
    """)
                        except Exception as e:
                            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error reading file \"{white}{element}{red}\": {white}{e}")
                    except Exception as e:
                        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error reading file \"{white}{element}{red}\": {white}{e}")
            return results_found

        results_found = check(folder_database)
        if not results_found:
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No result found for \"{white}{search}{red}\".")

        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Total files searched: {white}{files_searched}")

    except Exception as e:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during search: {white}{e}")

    Continue()
    Reset()
except Exception as e:
    Error(e)