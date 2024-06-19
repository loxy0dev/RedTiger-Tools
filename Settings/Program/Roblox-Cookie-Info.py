"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    import requests
    import json
except Exception as e:
   ErrorModule(e)
   
Title("Roblox Cookie Info")

try:
    cookie = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Cookie -> {white}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    try:
        info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
        print(info.json())
        information = json.loads(info.text)
        status = "Valid"
    except:
        status = "Invalid"

    try:
        username_roblox = information['UserName']
    except:
        username_roblox = "None"

    try:
        user_id_roblox = information["UserID"]
    except:
        user_id_roblox = "None"

    try:
        robux_roblox = information["RobuxBalance"]
    except:
        robux_roblox = "None"
    try:
        premium_roblox = information["IsPremium"]
    except:
        premium_roblox = "None"

    try:
        avatar_roblox = information["ThumbnailUrl"]
    except:
        avatar_roblox = "None"

    try:
        builders_club_roblox = information["IsAnyBuildersClubMember"]
    except:
        builders_club_roblox = "None"


    print(f"""
    {INFO_ADD} Status        : {white}{status}{red}
    {INFO_ADD} Username      : {white}{username_roblox}{red}
    {INFO_ADD} Id            : {white}{user_id_roblox}{red}
    {INFO_ADD} Robux         : {white}{robux_roblox}{red}
    {INFO_ADD} Premium       : {white}{premium_roblox}{red}
    {INFO_ADD} Builders Club : {white}{builders_club_roblox}{red}
    {INFO_ADD} Avatar        : {white}{avatar_roblox}{red}
    """)
    Continue()
    Reset()
except Exception as e:
    Error(e)