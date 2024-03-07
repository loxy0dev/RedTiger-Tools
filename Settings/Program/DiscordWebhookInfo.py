from Config.Config import *

import requests

Title("Webhook Info")

def obtenir_informations_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(webhook_url, headers=headers)

    if response.status_code == 200:
        webhook_info = response.json()
        LAPprint(f"{color.RED}\nInformation Webhook:")

        print(f"{color.YELLOW}Webhook ID      : {color.CYAN}", webhook_info['id'])
        print(f"{color.YELLOW}Webhook Token   : {color.CYAN}", webhook_info['token'])
        print(f"{color.YELLOW}Webhook Name    : {color.CYAN}", webhook_info['name'])
        print(f"{color.YELLOW}Webhook Avatar  : {color.CYAN}", webhook_info['avatar'])
        print(f"{color.YELLOW}Webhook Type    : {color.CYAN}", "bot" if webhook_info['type'] == 1 else "webhook utilisateur")
        print(f"{color.YELLOW}Channel ID      : {color.CYAN}", webhook_info['channel_id'])
        print(f"{color.YELLOW}Server ID       : {color.CYAN}", webhook_info['guild_id'])
        
        if 'user' in webhook_info:
            user_info = webhook_info['user']

            LAPprint(f"{color.RED}\nUser information associated with the Webhook:")

            print(f"{color.YELLOW}ID          : {color.CYAN}", user_info['id'])
            print(f"{color.YELLOW}Name        : {color.CYAN}", user_info['username'])
            print(f"{color.YELLOW}DisplayName : {color.CYAN}", user_info['global_name'])
            print(f"{color.YELLOW}Number      : {color.CYAN}", user_info['discriminator'])
            print(f"{color.YELLOW}Avatar      : {color.CYAN}", user_info['avatar'])
            print(f"{color.YELLOW}Flags       : {color.CYAN}", user_info['flags'], " Publique:", user_info['public_flags'])
            print(f"{color.YELLOW}Nitro       : {color.CYAN}", user_info['premium_type'])
            print(f"{color.YELLOW}Color       : {color.CYAN}", user_info['accent_color'])
            print(f"{color.YELLOW}Decoration  : {color.CYAN}", user_info['avatar_decoration_data'])
            print(f"{color.YELLOW}Banner      : {color.CYAN}", user_info['banner_color'])
        else:
            print("\nNone.")

    else:
        print(f"None.")

try:
 webhook_url = input(f"{color.RED}\n[?] | Webhook -> {color.RESET}")
 obtenir_informations_webhook(webhook_url)
except:
 ErrorUrl()
Continue()
Reset()