from Config.Util import *
from Config.Config import *
import requests

Title("Discord Webhook Info")

def obtenir_informations_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(webhook_url, headers=headers)

    if response.status_code == 200:
        webhook_info = response.json()
        print(f"{color.RED}\nInformation Webhook:")

        print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} ID      : {color.WHITE}", webhook_info['id'])
        print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Token   : {color.WHITE}", webhook_info['token'])
        print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Name    : {color.WHITE}", webhook_info['name'])
        print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar  : {color.WHITE}", webhook_info['avatar'])
        print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Type    : {color.WHITE}", "bot" if webhook_info['type'] == 1 else "webhook utilisateur")
        print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Channel ID      : {color.WHITE}", webhook_info['channel_id'])
        print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server ID       : {color.WHITE}", webhook_info['guild_id'])

        print(f"{color.RED}\nUser information associated with the Webhook:")
        if 'user' in webhook_info:
            user_info = webhook_info['user']

            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} ID          : {color.WHITE}", user_info['id'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Name        : {color.WHITE}", user_info['username'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} DisplayName : {color.WHITE}", user_info['global_name'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Number      : {color.WHITE}", user_info['discriminator'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar      : {color.WHITE}", user_info['avatar'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Flags       : {color.WHITE}", user_info['flags'], " Publique:", user_info['public_flags'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Nitro       : {color.WHITE}", user_info['premium_type'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Color       : {color.WHITE}", user_info['accent_color'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Decoration  : {color.WHITE}", user_info['avatar_decoration_data'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Banner      : {color.WHITE}", user_info['banner_color'])
            print("")
        else:
            print("\nNone.")

    else:
        print(f"\nNone.")

try:
 webhook_url = input(f"{color.RED}\n[?] | Webhook -> {color.RESET}")
 obtenir_informations_webhook(webhook_url)
except:
 ErrorUrl()
Continue()
Reset()