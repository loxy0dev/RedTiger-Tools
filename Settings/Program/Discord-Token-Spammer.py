from Config.Util import *
from Config.Config import *
import requests
Title("Discord Token Spammer")

token = input(f"{color.RED}\n{INPUT} Token -> {color.RESET}")
channel = input(f"{color.RED}{INPUT} Channel Id -> {color.RESET}")
message = input(f"{color.RED}{INPUT} Message -> {color.RESET}")

while True:
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
        print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Send{color.RED} | Message: {color.WHITE}{message}{color.RED} | Channel: {color.WHITE}{channel}{color.RED}")
    except:
        print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error{color.RED} | Message: {color.WHITE}{message}{color.RED} | Channel: {color.WHITE}{channel}{color.RED}")
