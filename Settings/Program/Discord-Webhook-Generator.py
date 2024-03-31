from Config.Util import *
from Config.Config import *
import string
import requests
import json
import random
import threading
Title("Discord Webhook Generator")

webhook = input(f"{color.RED}\n{INPUT} Webhook ? (y/n) -> {color.RESET}")
if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
    webhook_url = input(f"{color.RED}{INPUT} Webhook URL -> {color.RESET}")
    try:
        if webhook_url.lower().startswith("https://discord.com/api/webhooks"):
            pass
        else:
            ErrorWebhook()
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
                'description': f"**__Webhook:__**\n```{webhook_test_url}```",
                'color': color_webhook,
                'footer': {
                "text": username_webhook,
                "icon_url": avatar_webhook,
                }
                }
                send_webhook(embed_content)
                print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Webhook: {color.WHITE}{webhook_test_code}{color.GREEN}")
            else:
                print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Webhook: {color.WHITE}{webhook_test_code}{color.GREEN}")
        else:
            print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Status: {color.WHITE}Invalid{color.RED} | Webhook: {color.WHITE}{webhook_test_code}{color.RED}")
    except:
        print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Status: {color.WHITE}Error{color.RED} | Webhook: {color.WHITE}{webhook_test_code}{color.RED}")

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
