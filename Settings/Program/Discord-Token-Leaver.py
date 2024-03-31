from Config.Util import *
from Config.Config import *
import requests
import threading

Title("Discord Token Leaver")

token = input(f"{color.RED}\n{INPUT} Token -> {color.RESET}")
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