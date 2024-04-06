from Config.Util import *
from Config.Config import *
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

import random
import string
import json
import requests
import threading

Title("Discord Nitro Generator")

webhook = input(f"{color.RED}\n{INPUT} Webhook ? (y/n) -> {color.RESET}")
if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
    webhook_url = input(f"{color.RED}{INPUT} Webhook URL -> {color.RESET}")
    CheckWebhook(webhook_url)

print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Chrome
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Firefox
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Edge (recommend)
""")
choice = input(f"{INPUT} Browser -> {color.RESET}")

try:
    if choice == '1':
        navigator = "Chrome"
        print(f"{color.RED}{INFO} {navigator} Starting..{color.RESET}")
        driver = webdriver.Chrome()
        print(f"{color.RED}{INFO} {navigator} Ready !{color.RESET}")

    elif choice == '2':
        navigator = "Firefox"
        print(f"{color.RED}{INFO} {navigator} Starting..{color.RESET}")
        driver = webdriver.Firefox()
        print(f"{color.RED}{INFO} {navigator} Ready !{color.RESET}")

    elif choice == '3':
        navigator = "Edge"
        print(f"{color.RED}{INFO} {navigator} Starting..{color.RESET}")
        driver = webdriver.Edge()
        print(f"{color.RED}{INFO} {navigator} Ready !{color.RESET}")
    else:
        ErrorChoice()
except:
    print(f"{color.RED}{ERROR} {navigator} not installed or driver not update.")
    Continue()
    Reset()


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

def nitro_check():
    code_nitro = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(16)])
    url_nitro = f'https://discord.gifts/{code_nitro}'

    driver.get(url_nitro)
    driver.implicitly_wait(0)
    console = driver.execute_script("return console")
    search_term = 'Unrecognized'
    console_logs = driver.get_log('browser')
 
    found = False
    for log in console_logs:
        if search_term in log['message']:
            found = True
            break

    if found:
        print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Status:  {color.WHITE}Invalid{color.RED}   | Nitro: {color.WHITE}{url_nitro}{color.RED}{reset}")
    else:
        if "1015" in driver.page_source:
            print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Status: {color.WHITE}Error 1015{color.RED} | Nitro: {color.WHITE}{url_nitro}{color.RED}{reset}")
            time.sleep(0.3)
        else:
            if webhook in ['y']:
                embed_content = {
                'title': f'Nitro Valid !',
                'description': f"**__Nitro:__**\n```{url_nitro}```",
                'color': color_webhook,
                'footer': {
                "text": username_webhook,
                "icon_url": avatar_webhook,
                }
                }
                send_webhook(embed_content)
                print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Nitro: {color.WHITE}{url_nitro}{color.GREEN}{reset}")
            else:
                print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Status:  {color.WHITE}Valid{color.GREEN}  | Nitro: {color.WHITE}{url_nitro}{color.GREEN}{reset}")

while True:
    nitro_check() 