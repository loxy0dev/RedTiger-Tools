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
except Exception as e:
   ErrorModule(e)
   

Title("Discord Webhook Info")

try:
    def info_webhook(webhook_url):
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.get(webhook_url, headers=headers)
        webhook_info = response.json()

        webhook_id = webhook_info.get('id', "None")
        webhook_token = webhook_info.get('token', "None")
        webhook_name = webhook_info.get('name', "None")
        webhook_avatar = webhook_info.get('avatar', "None")
        webhook_type = "bot" if webhook_info.get('type') == 1 else "webhook utilisateur"
        channel_id = webhook_info.get('channel_id', "None")
        guild_id = webhook_info.get('guild_id', "None")

        Slow(f"""
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} ID         : {white}{webhook_id}{red}
 {INFO_ADD} Token      : {white}{webhook_token}{red}
 {INFO_ADD} Name       : {white}{webhook_name}{red}
 {INFO_ADD} Avatar     : {white}{webhook_avatar}{red}
 {INFO_ADD} Type       : {white}{webhook_type}{red}
 {INFO_ADD} Channel ID : {white}{channel_id}{red}
 {INFO_ADD} Server ID  : {white}{guild_id}{red}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

        if 'user' in webhook_info:
            user_info = webhook_info['user']
            
            user_id = user_info.get('id', "None")
            username = user_info.get('username', "None")
            display_name = user_info.get('global_name', "None")
            discriminator = user_info.get('discriminator', "None")
            user_avatar = user_info.get('avatar', "None")
            user_flags = user_info.get('flags', "None")
            accent_color = user_info.get('accent_color', "None")
            avatar_decoration = user_info.get('avatar_decoration_data', "None")
            banner_color = user_info.get('banner_color', "None")

            Slow(f"""{red}User information associated with the Webhook:
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} ID          : {white}{user_id}{red}
 {INFO_ADD} Name        : {white}{username}{red}
 {INFO_ADD} DisplayName : {white}{display_name}{red}
 {INFO_ADD} Number      : {white}{discriminator}{red}
 {INFO_ADD} Avatar      : {white}{user_avatar}{red}
 {INFO_ADD} Flags       : {white}{user_flags} Publique: {user_flags}{red}
 {INFO_ADD} Color       : {white}{accent_color}{red}
 {INFO_ADD} Decoration  : {white}{avatar_decoration}{red}
 {INFO_ADD} Banner      : {white}{banner_color}{red}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    """)

    webhook_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {color.RESET}")
    if CheckWebhook(webhook_url) == False:
        ErrorWebhook()
    info_webhook(webhook_url)
    Continue()
    Reset()
except Exception as e:
    Error(e)