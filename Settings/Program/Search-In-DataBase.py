from Config.Util import *
from Config.Config import *

Title("Search DataBase")

folder_database_relative = "./DataBase"
folder_database = os.path.abspath(folder_database_relative)

print(f"""
{INFO} Add DataBase to the "{white}{folder_database_relative}{red}" folder.
{INFO} If you don't have a DataBase you can get one on the Discord Server "{white}{discord_server}{red}\".""")
search = input(f"\n{INPUT} Search -> {reset}")

print(f"{WAIT} Search in DataBase..")

try:
    files_searched = 0
    def check(folder):
        global files_searched
        results_found = False
        for element in os.listdir(folder):
            chemin_element = os.path.join(folder, element)
            if os.path.isdir(chemin_element):
                check(chemin_element) 
            elif os.path.isfile(chemin_element): 
                try:
                    with open(chemin_element, 'r', encoding='utf-8') as file:
                        line_number = 0 
                        files_searched += 1
                        Title(f"Search DataBase - {files_searched} file search..")
                        for line in file:
                            line_number += 1
                            if search in line:
                                results_found = True
                                line_info = line.strip().replace(search, f"{color.YELLOW}{search}{white}")
                                print(f"""{red}
- File   : {white}{element}{red}
- Line   : {white}{line_number}{red}
- Result : {white}{line_info}""")
                except UnicodeDecodeError:
                    try:
                        with open(chemin_element, 'r', encoding='latin-1') as file:
                            files_searched += 1
                            line_number = 0 
                            Title(f"Search DataBase - {files_searched} file search..")
                            for line in file:
                                line_number += 1
                                if search in line:
                                    results_found = True
                                    line_info = line.strip().replace(search, f"{color.YELLOW}{search}{white}")
                                    print(f"""{red}
- File   : {white}{element}{red}
- Line   : {white}{line_number}{red}
- Result : {white}{line_info}""")
                    except Exception as e:
                        print(f"{ERROR} Error reading file \"{white}{element}{red}\": {white}{e}")
                except Exception as e:
                    print(f"{ERROR} Error reading file \"{white}{element}{red}\": {white}{e}")
        return results_found

    results_found = check(folder_database)
    if not results_found:
        print(f"{INFO} No result found for \"{white}{search}{red}\".")

    print(f"{INFO} Total files searched: {white}{files_searched}")

except Exception as e:
    print(f"{ERROR} Error during search: {white}{e}")

Continue()
Reset()
