from Options.Options import *

import webbrowser

TitrePage("Invite Bot Id")

try:
 IdBot = int(input(f"{couleur.RED}\nID bot -> {couleur.RESET}"))
except:
 ErreurId()

URLBot = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'

print(f"{couleur.RED}\nURL bot: \"{couleur.CYAN}{URLBot}{couleur.RED}\"{couleur.RESET}")

choix = input(f"\n{couleur.RED}Open the Internet ? (y, n) -> {couleur.RESET}")
if choix in ['y']:
    webbrowser.open_new_tab(URLBot)
    Continue()
    Reset()
else:
    Continue()
    Reset()
