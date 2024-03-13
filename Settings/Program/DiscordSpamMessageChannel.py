from Config.Util import *
from Config.Config import *
import requests
Title("Discord Spam Message Channel")

token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")
channel = input(f"{color.RED}[?] | Channel -> {color.RESET}")
message = input(f"{color.RED}[?] | Message -> {color.RESET}")

number = 0
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
    number += 1
    print(f'{color.RED}[+] | Message Send | Message: "{color.WHITE}{message}{color.RED}" | Channel: "{color.WHITE}{channel}{color.RED}" | Number: "{color.WHITE}{number}{color.RED}"{color.RESET}')
   except:
      ()
