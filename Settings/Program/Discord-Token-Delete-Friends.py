from Config.Util import *
from Config.Config import *
import requests
import threading

Title("Discord Token Delete Friends")

token = input(f"{color.RED}\n{INPUT} Token -> {color.RESET}")
r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
if r.status_code == 200:
    pass
else:
    ErrorToken()
def DeleteFriends(friends, token):
    for friend in friends:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers={'Authorization': token})
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Delete{color.RED} | User: {color.WHITE}{friend['user']['username']}#{friend['user']['discriminator']}")
        except Exception as e:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error: {e}{color.RED}")

if not requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token, 'Content-Type': 'application/json'}).json():
    print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error{color.RED}")

processes = []
friend_id = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token, 'Content-Type': 'application/json'}).json()
if not friend_id:
    print(f"{INFO} No friends found.")

for friend in [friend_id[i:i+3] for i in range(0, len(friend_id), 3)]:
    t = threading.Thread(target=DeleteFriends, args=(friend, token))
    t.start()
    processes.append(t)
for process in processes:
    process.join()
Continue()
Reset()