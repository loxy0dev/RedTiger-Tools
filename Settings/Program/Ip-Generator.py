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
    import random
    import threading

except Exception as e:
   ErrorModule(e)
   
Title("Ip Generator")

try:
    webhook = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook ? (y/n) -> {reset}")
    if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webhook_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
        CheckWebhook(webhook_url)

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

    number_valid = 0
    number_invalid = 0
    def ip_check():
        global number_valid, number_invalid
        number_1 = random.randint(1, 255)
        number_2 = random.randint(1, 255)
        number_3 = random.randint(1, 255)
        number_4 = random.randint(1, 255)
        ip = f"{number_1}.{number_2}.{number_3}.{number_4}"

        try:
            if sys.platform.startswith("win"):
                result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=0.1)
            elif sys.platform.startswith("linux"):
                result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=0.1)

            if result.returncode == 0:
                number_valid += 1
                if webhook in ['y']:

                    embed_content = {
                    'title': f'Ip Valid !',
                    'description': f"**Ip:**\n```{ip}```",
                    'color': color_webhook,
                    'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                    }
                    send_webhook(embed_content)
                    print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{green} Status:  {white}Valid{green}  Ip: {white}{ip}{green}")
                else:
                    print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{green} Status:  {white}Valid{green}  Ip: {white}{ip}{green}")
                
            else:
                number_invalid += 1
                print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{red} Status: {white}Invalid{red} Ip: {white}{ip}{red}")
        except:
            number_invalid += 1
            print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Logs: {white}{number_invalid} invalid - {number_valid} valid{red} Status: {white}Invalid{red} Ip: {white}{ip}{red}")
        Title(f"Ip Generator - Invalid: {number_invalid} - Valid: {number_valid}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=ip_check)
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