from Config.Util import *
from Config.Config import *
import requests

Title("Discord Token Joiner")

token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")
invite = input(f"{color.RED}[?] | Server Invitation -> {color.RESET}")

invite_code = invite.split("/")[-1]

try:
    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
    if response.status_code == 200:
        server_name = response.json().get('guild', {}).get('name')
    else:
        server_name = invite
except:
    server_name = invite


print(f"{color.RED}[!] | Server: {color.WHITE}{server_name}")
try:
        headers = {
            'Authorization': token
        }
        response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers)
        
        if response.status_code == 200:
            print(f"{color.RED}[+] | Joined | Invite: \"{color.WHITE}{invite}{color.RED}\" | Token: \"{color.WHITE}{token}{color.RED}\"")
        else:
            print(f"{color.RED}[X] | Error Joined | Invite: \"{color.WHITE}{invite}{color.RED}\" | Token: \"{color.WHITE}{token}{color.RED}\" | Error: \"{color.WHITE}{response.status_code}{color.RED}\"")
except:
       print(f"{color.RED}[+] | Error Joined | Invite: \"{color.WHITE}{invite}{color.RED}\" | Token: \"{color.WHITE}{token}{color.RED}\"")

