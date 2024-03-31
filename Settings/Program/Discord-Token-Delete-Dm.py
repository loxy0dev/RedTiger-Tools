from Config.Util import *
from Config.Config import *
import requests
import threading
Title("Discord Token Delete Dm")

token = input(f"{color.RED}\n{INPUT} Token -> {color.RESET}")
r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
if r.status_code == 200:
    pass
else:
    ErrorToken()

def DmDeleter(token, channels):
    for channel in channels:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'], headers={'Authorization': token})
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Delete{color.RED} | Channel: {color.WHITE}{channel['id']}")
        except Exception as e:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error: {e}{color.RED}")

processes = []
channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
if not channel_id:
    print(f"{INFO} No Dm found.")
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