from Config.Util import *
from Config.Config import *
import webbrowser

Title("Discord Invite Bot To Id")

try:
 IdBot = int(input(f"\n{color.RED}[?] | ID bot -> {color.RESET}"))
except:
 ErrorId()

URLBot = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'

print(f"{color.RED}[!] | URL bot: \"{color.WHITE}{URLBot}{color.RED}\"{color.RESET}")

choice = input(f"{color.RED}[?] | Open the Internet ? (y, n) -> {color.RESET}")
if choice in ['y', 'Y', 'Yes', 'yes']:
    webbrowser.open_new_tab(URLBot)
    Continue()
    Reset()
else:
    Continue()
    Reset()
