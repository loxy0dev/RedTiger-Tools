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
    import requests
    import json
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Webhook Spammer")

try:
    webhook_url = input(f"{color.RED}\n{INPUT} Webhook URL -> {color.RESET}")
    CheckWebhook(webhook_url)
    message = input(f"{color.RED}{INPUT} Message -> {color.RESET}")

    try:
        threads_number = int(input(f"{INPUT} Threads Number -> {color.RESET}"))
    except:
        ErrorNumber()

    def send_webhook():
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            'content': message,
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }
        try:
            response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Message: {color.WHITE}{message}{color.GREEN} | Status: {color.WHITE}Send{color.GREEN}")
        except:
            print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Message: {color.WHITE}{message}{color.RED} | Status: {color.WHITE}Rate Limit{color.RED}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=send_webhook)
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