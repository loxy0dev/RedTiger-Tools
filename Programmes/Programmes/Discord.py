from Options.Options import *

import webbrowser

Title("Server Discord (site)")

site = discord

webbrowser.open_new_tab(site)
print(f"{color.RED}\n[!] | Access to the Discord server {color.CYAN}\"{site}\"" + color.RESET)
time.sleep(3)
Reset()