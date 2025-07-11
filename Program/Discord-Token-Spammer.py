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
   
Title("Discord Token Spammer")

try:

    def spammer(token, message):
        try:
            response = requests.post(
                f"https://discord.com/api/channels/{channel}/messages",
                data={'content': message},
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                    'Authorization': token
                }
            )
            response.raise_for_status()
            print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Message: {white}{message_sensur}{green} Channel: {white}{channel}{green} Status: {white}Send{green}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Message: {white}{message_sensur}{red} Channel: {white}{channel}{red} Status: {white}Error {response.status_code}{red}")


    Slow(discord_banner)
    token = Choice1TokenDiscord()
    channel = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Channel Spam Id -> {reset}")
    message = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Spam Message -> {reset}")
    message_len = len(message)
    if message_len > 10:
        message_sensur = message[:10]
        message_sensur = message_sensur + "..."
    else:
        message_sensur = message
        
    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number (recommended: 2, 4) -> {reset}"))
    except:
        ErrorNumber()

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=spammer, args=(token, message))
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        request()
except Exception as e:
    Error(e)