from Config.Util import *
from Config.Config import *
import requests
import time
import random
Title("Discord Token Language Changer")

token = input(f"{color.RED}\n{INPUT} Token -> {color.RESET}")

headers = {'Authorization': token, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
if r.status_code == 200:
    try:
        amount = int(input(f"{color.RED}{INPUT} Enter the number of cycles -> {color.RESET}"))
    except:
        ErrorNumber()

    for i in range(amount):
        try:
            time.sleep(0.6)
            random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
            setting = {'locale': random_language}
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Language: {color.WHITE}{random_language}{color.RED}")
        except:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status:  {color.WHITE}Error{color.RED}  | Language: {color.WHITE}{random_language}{color.RED}")
    print(f"\n{color.RED}{INFO} Finish.")
    Continue()
    Reset()
else:
  ErrorToken()