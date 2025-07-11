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
    import json
except Exception as e:
   ErrorModule(e)
   
Title("Roblox Cookie Info")

try:
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Selected User-Agent: {white + user_agent}")
    cookie = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Cookie -> {white}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    try:
        response = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers, cookies={".ROBLOSECURITY": cookie})
        api = json.loads(response.text)
        status = "Valid"
        username_roblox = api.get('UserName', "None")
        user_id_roblox = api.get("UserID", "None")
        robux_roblox = api.get("RobuxBalance", "None")
        premium_roblox = api.get("IsPremium", "None")
        avatar_roblox = api.get("ThumbnailUrl", "None")
        builders_club_roblox = api.get("IsAnyBuildersClubMember", "None")
    except:
        status = "Invalid"
        username_roblox = "None"
        user_id_roblox = "None"
        robux_roblox = "None"
        premium_roblox = "None"
        avatar_roblox = "None"
        builders_club_roblox = "None"
        
    print(f"""
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} Status        : {white}{status}{red}
 {INFO_ADD} Username      : {white}{username_roblox}{red}
 {INFO_ADD} Id            : {white}{user_id_roblox}{red}
 {INFO_ADD} Robux         : {white}{robux_roblox}{red}
 {INFO_ADD} Premium       : {white}{premium_roblox}{red}
 {INFO_ADD} Builders Club : {white}{builders_club_roblox}{red}
 {INFO_ADD} Avatar        : {white}{avatar_roblox}{red}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    """)
    Continue()
    Reset()
except Exception as e:
    Error(e)