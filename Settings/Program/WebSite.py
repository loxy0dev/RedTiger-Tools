from Config.Config import *

import webbrowser
Title("Web Site")
print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Site Web
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Discord Server 
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} GitHub Tool
""")

choice = input(f"{color.RED}-> {color.RESET}")
if choice in ['1', '01']:
    site = f"https://{website}"
    webbrowser.open_new_tab(site)
    print(f"\n{color.RED}[!] | Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()
if choice in ['2', '02']:
    site = f"https://{discord_server}"
    webbrowser.open_new_tab(site)
    print(f"{color.RED}\n[!] | Access to the Discord server \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()

if choice in ['3', '03']:
    site = f"https://{github_tool}"
    webbrowser.open_new_tab(site)
    print(f"\n{color.RED}[!] | Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
    Continue()
    Reset()