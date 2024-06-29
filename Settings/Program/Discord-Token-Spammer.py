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
   
Title("Discord Token Spammer")

try:
    print()
    token = Choice1TokenDiscord()
    channel = input(f"{color.RED}{INPUT} Channel Spam Id -> {color.RESET}")
    message = input(f"{color.RED}{INPUT} Spam Message -> {color.RESET}")
    message_len = len(message)
    if message_len > 10:
        message_sensur = message[:10]
        message_sensur = message_sensur + "..."
    else:
        message_sensur = message
    try:
        threads_number = int(input(f"{INPUT} Threads Number (recommended: 2, 4) -> {color.RESET}"))
    except:
        ErrorNumber()

    def spam():
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
            print(f"{green}[{white}{current_time_hour()}{green}] {GEN_VALID} Message: {color.WHITE}{message_sensur}{color.GREEN} | Channel: {color.WHITE}{channel}{color.GREEN} | Status: {color.WHITE}Send{color.GREEN}")
        except:
            print(f"{red}[{white}{current_time_hour()}{red}] {GEN_INVALID} Message: {color.WHITE}{message_sensur}{color.RED} | Channel: {color.WHITE}{channel}{color.RED} | Status: {color.WHITE}Error {response.status_code}{color.RED}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=spam)
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