from Config.Util import *
from Config.Config import *
Title("Roblox User Info")
import requests

user_id = input(f"\n{INPUT} ID -> {color.RESET}")
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
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Username       : {color.WHITE}{username}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Id             : {color.WHITE}{userid}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Display Name   : {color.WHITE}{display_name}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Description    : {color.WHITE}{description}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Created        : {color.WHITE}{created_at}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Banned         : {color.WHITE}{is_banned}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} External Name  : {color.WHITE}{external_app_display_name}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Verified Badge : {color.WHITE}{has_verified_badge}{color.RED}
""")
    Continue()
    Reset()
except:
       ErrorId()