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
    import random
    import string
    import json
    import requests
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Nitro Generator")

try:
    Slow(discord_banner)
    webhook = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook ? (y/n) -> {reset}")
    if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webhook_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook Url -> {reset}")
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
    except:
        ErrorNumber()

    def send_webhook(url_nitro):
        payload = {
        'embeds': [{
                    'title': f'Nitro Valid !',
                    'description': f"**Nitro:**\n```{url_nitro}```",
                    'color': color_webhook,
                    'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                }],
        'username': username_webhook,
        'avatar_url': avatar_webhook
        }

        headers = {
        'Content-Type': 'application/json'
        }

        requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    def nitro_check():
        code_nitro = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(16)])
        url_nitro = f'https://discord.gift/{code_nitro}'
        response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
        if response.status_code == 200:
            if webhook in ['y']:
                send_webhook(url_nitro)
            print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Status:  {white}Valid{green}  Nitro: {white}{url_nitro}{reset}")
        else:
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Status: {white}Invalid{red} Nitro: {white}{url_nitro}{reset}")
        
    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=nitro_check)
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