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
except Exception as e:
   ErrorModule(e)
   

Title("Discord Webhook Info")

try:
    def info_webhook(webhook):
            headers = {
                'Content-Type': 'application/json',
            }

            response = requests.get(webhook_url, headers=headers)
            webhook_info = response.json()
            print(f"{color.RED}\nInformation Webhook:")

            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} ID      : {color.WHITE}", webhook_info['id'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Token   : {color.WHITE}", webhook_info['token'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Name    : {color.WHITE}", webhook_info['name'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar  : {color.WHITE}", webhook_info['avatar'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Type    : {color.WHITE}", "bot" if webhook_info['type'] == 1 else "webhook utilisateur")
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Channel ID : {color.WHITE}", webhook_info['channel_id'])
            print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server ID  : {color.WHITE}", webhook_info['guild_id'])

            print(f"{color.RED}\nUser information associated with the Webhook:")
            if 'user' in webhook_info:
                user_info = webhook_info['user']

                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} ID          : {color.WHITE}", user_info['id'])
                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Name        : {color.WHITE}", user_info['username'])
                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} DisplayName : {color.WHITE}", user_info['global_name'])
                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Number      : {color.WHITE}", user_info['discriminator'])
                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar      : {color.WHITE}", user_info['avatar'])
                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Flags       : {color.WHITE}", user_info['flags'], " Publique:", user_info['public_flags'])
                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Color       : {color.WHITE}", user_info['accent_color'])
                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Decoration  : {color.WHITE}", user_info['avatar_decoration_data'])
                print(f"{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Banner      : {color.WHITE}", user_info['banner_color'])
                print("")
            else:
                print("\nNone.")


    webhook_url = input(f"{color.RED}\n{INPUT} Webhook URL -> {color.RESET}")
    CheckWebhook(webhook_url)
    info_webhook(webhook_url)
    Continue()
    Reset()
except Exception as e:
    Error(e)