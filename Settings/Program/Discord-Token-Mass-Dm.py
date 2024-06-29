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
   

Title("Discord Token Mass Dm")

try:
    def MassDM(token_discord, channels, Message):
        for channel in channels:
            for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
                try:
                    requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers={'Authorization': token_discord}, data={"content": f"{Message}"})
                    print(f'{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Send{color.RED} | User: {color.WHITE}{user}{color.RED}')

                except Exception as e:
                    print(f'{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error: {e}{color.RED}')

    print()
    token_discord = Choice1TokenDiscord()
    validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        ErrorToken()
    try:
        message = str(input(f"{color.RED}{INPUT} Message -> {color.RESET}"))
    except:
        pass
    processes = []

    try:
        repetition = int(input(f"{color.RED}{INPUT} Number of Repetitions -> {color.RESET}"))
    except:
        ErrorNumber()

    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord}).json()

    number = 0
    for i in range(repetition):
        number += 1
        if not channelIds:
            ()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = threading.Thread(target=MassDM, args=(token_discord, channel, message))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        print(f"{color.RED}{INFO} Finish n°{number}.")
        time.sleep(0.5)
        

    Continue()
    Reset()
except Exception as e:
    Error(e)