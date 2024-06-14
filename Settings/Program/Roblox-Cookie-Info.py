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
    cookie = input(f"{color.RED}\n{INPUT} Cookie -> {color.WHITE}")
    print(f"{color.RED}{WAIT} Information Recovery..{reset}")
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
    {white}[{red}+{white}]{red} Status        : {white}{status}{red}
    {white}[{red}+{white}]{red} Username      : {white}{username_roblox}{red}
    {white}[{red}+{white}]{red} Id            : {white}{user_id_roblox}{red}
    {white}[{red}+{white}]{red} Robux         : {white}{robux_roblox}{red}
    {white}[{red}+{white}]{red} Premium       : {white}{premium_roblox}{red}
    {white}[{red}+{white}]{red} Builders Club : {white}{builders_club_roblox}{red}
    {white}[{red}+{white}]{red} Avatar        : {white}{avatar_roblox}{red}
    """)
    Continue()
    Reset()
except Exception as e:
    Error(e)