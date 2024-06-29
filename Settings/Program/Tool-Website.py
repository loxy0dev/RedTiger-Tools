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
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Tool Website")
print(f"""
{white}[{red}01{white}] {red}->{white} Web Site
{white}[{red}02{white}] {red}->{white} Discord
{white}[{red}03{white}] {red}->{white} Github
{white}[{red}04{white}] {red}->{white} Telegram
""")

try:
    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Site -> {color.RESET}")
    if choice in ['1', '01']:
        site = f"https://{website}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()
    if choice in ['2', '02']:
        site = f"https://{discord_server}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the Discord server \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()

    if choice in ['3', '03']:
        site = f"https://{github_tool}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()

    if choice in ['4', '04']:
        site = f"https://{telegram}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()
except Exception as e:
    Error(e)