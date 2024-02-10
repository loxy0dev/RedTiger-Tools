from Options.Options import *

import webbrowser

Title("WebSite RedTiger (site)")

site = website

webbrowser.open_new_tab(site)
print(f"\n{color.RED}[!] | Access to the site {color.CYAN}\"{site}\"" + color.RESET)
time.sleep(3)
Reset()