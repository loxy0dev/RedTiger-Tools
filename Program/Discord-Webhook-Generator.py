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
    import string
    import requests
    import json
    import random
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Webhook Generator")

try:
    webhook = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook ? (y/n) -> {reset}")
    if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webhook_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
        if CheckWebhook(webhook_url) == False:
            ErrorWebhook()

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
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

    def webhook_check():
        first = ''.join([str(random.randint(0, 9)) for _ in range(19)])
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([68])))
        webhook_test_code = f"{first}/{second}"
        webhook_test_url = f"https://discord.com/api/webhooks/{webhook_test_code}"

        try:
            response = requests.head(webhook_test_url)
            if response.status_code == 200:
                if webhook in ['y']:
                    embed_content = {
                    'title': f'Webhook Valid !',
                    'description': f"**Webhook:**\n```{webhook_test_url}```",
                    'color': color_webhook,
                    'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                    }
                    send_webhook(embed_content)
                    print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Status:  {white}Valid{green}  Webhook: {white}{webhook_test_code}{green}")
                else:
                    print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Status:  {white}Valid{green}  Webhook: {white}{webhook_test_code}{green}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Status: {white}Invalid{red} Webhook: {white}{webhook_test_code}{red}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Status: {white}Error{red} Webhook: {white}{webhook_test_code}{red}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=webhook_check)
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