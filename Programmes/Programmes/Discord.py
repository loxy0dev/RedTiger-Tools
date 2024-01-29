from Options.Options import *

import webbrowser

TitrePage("Serveur Discord (site)")

site = discord

webbrowser.open_new_tab(site)
print(f"{couleur.RED}\n[!] | Access to the Discord server {couleur.CYAN}\"{site}\"" + couleur.RESET)
time.sleep(3)
Reset()