from Options.Options import *

import webbrowser

TitrePage("Site RedTiger (site)")

site = siteweb

webbrowser.open_new_tab(site)
print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Access to the site {couleur.CYAN}\"{site}\"" + couleur.RESET)
time.sleep(3)
Reset()