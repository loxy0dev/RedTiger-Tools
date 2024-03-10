from Config.Util import *
from Config.Config import *
import requests
import time
from itertools import cycle

Title("Discord Theme Changer")
token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")

headers = {'Authorization': token, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
if r.status_code == 200:
    try:
        amount = int(input(f"{color.RED}[?] | Enter the number of cycles -> {color.RESET}"))
    except:
        ErrorNumber()
            
    modes = cycle(["light", "dark"])
    for i in range(amount):
        theme = next(modes)
        print(f"{color.RED}[+] | Theme Changed | \"{color.WHITE}{theme}{color.RED}\"")
        Title(f"Discord Theme Changer - Theme: {theme}")
        time.sleep(0.5)
        setting = {'theme': theme}
        requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
    Title("Discord Theme Changer - Finish")
    print(f"{color.RED}[!] | Finish.")
    Continue()
    Reset()
else:
    ErrorToken()