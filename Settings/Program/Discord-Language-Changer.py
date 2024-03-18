from Config.Util import *
from Config.Config import *
import requests
import time
import random
Title("Discord Language Changer")
token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")

headers = {'Authorization': token, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
if r.status_code == 200:
    try:
        amount = int(input(f"{color.RED}[?] | Enter the number of cycles -> {color.RESET}"))
    except:
        ErrorNumber()

    for i in range(amount):
        time.sleep(0.6)
        random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
        setting = {'locale': random_language}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
        print(f"{color.RED}[+] | Language Changed | \"{color.WHITE}{random_language}{color.RED}\"")
        Title(f"Discord Language Changer - Language: {random_language}")
    Title("Discord Language Changer - Finish")
    print(f"{color.RED}[!] | Finish.")
    Continue()
    Reset()
else:
  ErrorToken()