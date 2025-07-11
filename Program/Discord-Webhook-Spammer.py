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
    import json
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Webhook Spammer")

try:
    webhook_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
    if CheckWebhook(webhook_url) == False:
        ErrorWebhook()
    message = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Message -> {reset}")

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
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
            print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Message: {white}{message}{color.GREEN} Status: {white}Send{color.GREEN}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Message: {white}{message}{red} Status: {white}Rate Limit{red}")

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