from Options.Options import *

import webbrowser

Title("Invite Bot Id")

try:
 IdBot = int(input(f"\n{color.RED}[?] | ID bot -> {color.RESET}"))
except:
 ErrorId()

URLBot = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'

print(f"{color.RED}[!] | URL bot: \"{color.CYAN}{URLBot}{color.RED}\"{color.RESET}")

choix = input(f"{color.RED}[?] | Open the Internet ? (y, n) -> {color.RESET}")
if choix in ['y']:
    webbrowser.open_new_tab(URLBot)
    Continue()
    Reset()
else:
    Continue()
    Reset()
