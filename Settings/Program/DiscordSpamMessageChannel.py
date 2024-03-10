from Config.Util import *
from Config.Config import *
import requests


token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")
channel = input(f"{color.RED}[?] | Channel -> {color.RESET}")
message = input(f"{color.RED}[?] | Message -> {color.RESET}")

def send_message():
    requests.post(
            f"https://discord.com/api/channels/{channel}/messages",
            data={'content': message},
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Authorization': token
            }
        )
    print(f'{color.RED}[+] | Message Send | Message: "{color.WHITE}{message}{color.RED}" | Channel: "{color.WHITE}{channel}{color.RED}" {color.RESET}')

while True:
    send_message()
