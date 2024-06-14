"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   
   
Title("Roblox User Info")

try:
    user_id = input(f"\n{INPUT} ID -> {color.RESET}")
    print(f"{color.RED}{WAIT} Information Recovery..{reset}")
    try:

        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        user_info = user_info_response.json()

        try:
            userid = user_info['id']
        except:
            userid = "None"
        
        try:
            display_name = user_info['displayName']
        except:
            display_name = "None"
        
        try:
            username = user_info['name']
        except:
            username = "None"

        try:
            description = user_info['description']
        except:
            description = "None"

        try:
            created_at = user_info['created']
        except:
            created_at = "None"
        
        try:
            is_banned = user_info['isBanned']
        except:
            is_banned = "None"
        
        try:
            external_app_display_name = user_info['externalAppDisplayName']
        except:
            external_app_display_name = "None"

        try:
            has_verified_badge = user_info['hasVerifiedBadge']
        except:
            has_verified_badge = "None"

        print(f"""
    {white}[{red}+{white}]{red} Username       : {white}{username}{red}
    {white}[{red}+{white}]{red} Id             : {white}{userid}{red}
    {white}[{red}+{white}]{red} Display Name   : {white}{display_name}{red}
    {white}[{red}+{white}]{red} Description    : {white}{description}{red}
    {white}[{red}+{white}]{red} Created        : {white}{created_at}{red}
    {white}[{red}+{white}]{red} Banned         : {white}{is_banned}{red}
    {white}[{red}+{white}]{red} External Name  : {white}{external_app_display_name}{red}
    {white}[{red}+{white}]{red} Verified Badge : {white}{has_verified_badge}{red}
    """)
        Continue()
        Reset()
    except:
        ErrorId()
except Exception as e:
    Error(e)