from Config.Util import *
from Config.Config import *
import requests
import json
import random
import threading
Title("Ip Generator")

webhook = input(f"{color.RED}\n{INPUT} Webhook ? (y/n) -> {color.RESET}")
if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
    webhook_url = input(f"{color.RED}{INPUT} Webhook URL -> {color.RESET}")
    try:
        response = requests.head(webhook_url)
        if response.status_code != 200:
            ErrorWebhook()
        else:
            print(f"{color.RED}{INFO} Webhook Valid.")
    except:
        ErrorWebhook()

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

def ip_check():
    number_1 = random.randint(1, 200)
    number_2 = random.randint(1, 200)
    number_3 = random.randint(1, 200)
    number_4 = random.randint(1, 200)
    ip = f"{number_1}.{number_2}.{number_3}.{number_4}"

    try:
        result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            if webhook in ['y']:
                embed_content = {
                'title': f'Ip Valid !',
                'description': f"**__Ip:__**\n```{ip}```",
                'color': color_webhook,
                'footer': {
                "text": username_webhook,
                "icon_url": avatar_webhook,
                }
                }
                send_webhook(embed_content)
                print(f"{GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Ip: {color.WHITE}{ip}{color.GREEN}")
            else:
                print(f"{GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Ip: {color.WHITE}{ip}{color.GREEN}")
        else:
            print(f"{GEN_INVALID} Status: {color.WHITE}Invalid{color.RED} | Ip: {color.WHITE}{ip}{color.RED}")
    except:
        print(f"{GEN_INVALID} Status: {color.WHITE}Invalid{color.RED} | Ip: {color.WHITE}{ip}{color.RED}")

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