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

number_valid = 0
number_invalid = 0
file_txt_relative = "./1-File-Output/IpGenerator/Ip-Valid.txt"
file_txt = os.path.abspath(file_txt_relative)
def ip_check():
    global number_valid, number_invalid
    number_1 = random.randint(1, 255)
    number_2 = random.randint(1, 255)
    number_3 = random.randint(1, 255)
    number_4 = random.randint(1, 255)
    ip = f"{number_1}.{number_2}.{number_3}.{number_4}"

    try:
        result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=0.1)
        if result.returncode == 0:
            number_valid += 1
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
                print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Logs: {color.WHITE}{number_invalid} invalid - {number_valid} valid{color.RED} | Status:  {color.WHITE}Valid{color.GREEN}  | Ip: {color.WHITE}{ip}{color.GREEN}")
            else:
                print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Logs: {color.WHITE}{number_invalid} invalid - {number_valid} valid{color.RED} | Status:  {color.WHITE}Valid{color.GREEN}  | Ip: {color.WHITE}{ip}{color.GREEN}")
            
            with open(file_txt, 'a') as f:
                f.write(f"[{current_time_day_hour()}] | Ip Valid: {ip}\n")
        else:
            number_invalid += 1
            print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Logs: {color.WHITE}{number_invalid} invalid - {number_valid} valid{color.RED} | Status: {color.WHITE}Invalid{color.RED} | Ip: {color.WHITE}{ip}{color.RED}")
    except:
        number_invalid += 1
        print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Logs: {color.WHITE}{number_invalid} invalid - {number_valid} valid{color.RED} | Status: {color.WHITE}Invalid{color.RED} | Ip: {color.WHITE}{ip}{color.RED}")
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