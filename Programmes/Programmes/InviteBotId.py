from Options.Options import *

import webbrowser
import time

TitrePage("Invite Bot Id")

try:
 IdBot = int(input(f"{couleur.RED}\nID du bot -> {couleur.RESET}"))
except:
 print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez mettre un ID valide !", couleur.RESET)  
 time.sleep(3)
 Reset()

URLBot = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'

print(f"{couleur.RED}\nVoici l'URL pour inviter le bot: \"{couleur.CYAN}{URLBot}{couleur.RED}\"{couleur.RESET}")

choix = input(f"\n{couleur.RED}Voulez-vous ouvrir une page internet ? (y, n) -> {couleur.RESET}")
if choix in ['y']:
    webbrowser.open_new_tab(URLBot)
    print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Une page internet a était ouvert avec le lien \"{couleur.CYAN}{URLBot}{couleur.RED}\"." + couleur.RESET)
    input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
    Reset()
else:
    input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
    Reset()
