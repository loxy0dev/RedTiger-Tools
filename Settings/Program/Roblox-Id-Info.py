from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   
   
Title("Roblox User Info")

try:
    user_id = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} ID -> {color.RESET}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    try:

        response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        api = response.json()

        userid = api.get('id', "None")
        display_name = api.get('displayName', "None")
        username = api.get('name', "None")
        description = api.get('description', "None")
        created_at = api.get('created', "None")
        is_banned = api.get('isBanned', "None")
        external_app_display_name = api.get('externalAppDisplayName', "None")
        has_verified_badge = api.get('hasVerifiedBadge', "None")

        print(f"""
    {INFO_ADD} Username       : {white}{username}{red}
    {INFO_ADD} Id             : {white}{userid}{red}
    {INFO_ADD} Display Name   : {white}{display_name}{red}
    {INFO_ADD} Description    : {white}{description}{red}
    {INFO_ADD} Created        : {white}{created_at}{red}
    {INFO_ADD} Banned         : {white}{is_banned}{red}
    {INFO_ADD} External Name  : {white}{external_app_display_name}{red}
    {INFO_ADD} Verified Badge : {white}{has_verified_badge}{red}
    """)
        Continue()
        Reset()
    except:
        ErrorId()
except Exception as e:
    Error(e)
