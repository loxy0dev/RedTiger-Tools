"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Tool Website")
print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Web Site
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Discord
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Github
{color.WHITE}[{color.RED}04{color.WHITE}] {color.RED}->{color.WHITE} Telegram
""")

try:
    choice = input(f"{color.RED}{INPUT} Site -> {color.RESET}")
    if choice in ['1', '01']:
        site = f"https://{website}"
        webbrowser.open_new_tab(site)
        print(f"{color.RED}{INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()
    if choice in ['2', '02']:
        site = f"https://{discord_server}"
        webbrowser.open_new_tab(site)
        print(f"{color.RED}\n{INFO} Access to the Discord server \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()

    if choice in ['3', '03']:
        site = f"https://{github_tool}"
        webbrowser.open_new_tab(site)
        print(f"{color.RED}{INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()

    if choice in ['4', '04']:
        site = f"https://{telegram}"
        webbrowser.open_new_tab(site)
        print(f"{color.RED}{INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()
except Exception as e:
    Error(e)