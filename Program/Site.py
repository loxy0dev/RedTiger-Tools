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
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Site")

print(f"""
 {BEFORE}01{AFTER}{white} GunsLol
 {BEFORE}02{AFTER}{white} Github
 {BEFORE}03{AFTER}{white} Telegram
""")

try:
    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Site -> {reset}")
    if choice in ['1', '01']:
        site = f"https://{gunslol}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{white}{site}{red}\"" + reset)
        Continue()
        Reset()

    if choice in ['2', '02']:
        site = f"https://{github_tool}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{white}{site}{red}\"" + reset)
        Continue()
        Reset()

    if choice in ['3', '03']:
        site = f"https://{telegram}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{white}{site}{red}\"" + reset)
        Continue()
        Reset()
except Exception as e:
    Error(e)