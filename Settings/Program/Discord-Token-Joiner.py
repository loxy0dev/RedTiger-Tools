from Config.Util import *
from Config.Config import *
import requests

Title("Discord Token Joiner")

token = input(f"{color.RED}\n{INPUT} Token -> {color.RESET}")
invite = input(f"{color.RED}{INPUT} Server Invitation -> {color.RESET}")

invite_code = invite.split("/")[-1]

try:
    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
    if response.status_code == 200:
        server_name = response.json().get('guild', {}).get('name')
    else:
        server_name = invite
except:
    server_name = invite

try:
        headers = {
            'Authorization': token
        }
        response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers)
        
        if response.status_code == 200:
            print(f"\n{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Joined{color.RED} | Server: {color.WHITE}{server_name}{color.RED}\n")
        else:
            print(f"\n{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {response.status_code}{color.RED} | Server: {color.WHITE}{server_name}{color.RED}\n")
except:
    print(f"\n{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error{color.RED} | Server: {color.WHITE}{server_name}{color.RED}\n")

Continue()
Reset()