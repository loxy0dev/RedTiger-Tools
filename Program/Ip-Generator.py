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
    import random
except Exception as e:
   ErrorModule(e)
   
Title("Ip Generator")

import concurrent.futures
import random
import subprocess
import sys
import requests
import json
import threading

try:
    webhook = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook ? (y/n) -> {reset}")
    if webhook.lower() in ['y', 'yes']:
        webhook_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
    except ValueError:
        ErrorNumber()

    def SendWebhook(embed_content):
        payload = {
            'embeds': [embed_content],
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }

        headers = {'Content-Type': 'application/json'}

        try:
            requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        except requests.RequestException as e:
            print(f"{BEFORE + current_time_hour() + AFTER} Error sending webhook: {e}{reset}")

    number_valid = 0
    number_invalid = 0

    def IpCheck():
        global number_valid, number_invalid
        ip = ".".join(str(random.randint(1, 255)) for _ in range(4))

        try:
            if sys.platform.startswith("win"):
                result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=0.1)
            elif sys.platform.startswith("linux"):
                result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=0.1)
            else:
                ErrorPlateform()

            if result.returncode == 0:
                number_valid += 1
                if webhook.lower() == 'y':
                    embed_content = {
                        'title': 'Ip Valid !',
                        'description': f"**Ip:**\n```{ip}```",
                        'color': color_webhook,
                        'footer': {
                            "text": username_webhook,
                            "icon_url": avatar_webhook,
                        }
                    }
                    SendWebhook(embed_content)
                print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{green} Status:  {white}Valid{green}  Ip: {white}{ip}{green}")
            else:
                number_invalid += 1
                print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{red} Status: {white}Invalid{red} Ip: {white}{ip}{red}")
        except Exception:
            number_invalid += 1
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{red} Status: {white}Invalid{red} Ip: {white}{ip}{red}")
        Title(f"Ip Generator - Invalid: {number_invalid} - Valid: {number_valid}")

    def Request():
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=threads_number) as executor:
                executor.map(lambda _: IpCheck(), range(threads_number))
        except Exception as e:
            ErrorNumber()

    while True:
        Request()

except Exception as e:
    Error(e)

