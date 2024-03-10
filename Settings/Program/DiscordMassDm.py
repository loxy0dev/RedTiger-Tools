from Config.Util import *
from Config.Config import *
import requests
import threading
from colorama import Fore
Title("Discord Mass Dm")

def MassDM(token_discord, channels, Message):
    for channel in channels:
        for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
            try:
                requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers={'Authorization': token_discord}, data={"content": f"{Message}"})
                print(f'{color.RED}[+] | Message Send | User: \"{color.WHITE}{user}{color.RED}\"')
                Title(f"Discord Mass Dm - {user}")
            except Exception as e:
                print(f'{color.RED}[X] | Message not Send | Error: \"{color.WHITE}{e}{color.RED}\"')

token_discord = input(f"{color.RED}\n[?] | Token -> {color.RESET}")
validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})
if validityTest.status_code != 200:
    ErrorToken()
try:
 message = str(input(f"{color.RED}[?] | Message -> {color.RESET}"))
except:
    ()
processes = []

channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord}).json()
if not channelIds:
    ()
for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
    t = threading.Thread(target=MassDM, args=(token_discord, channel, message))
    t.start()
    processes.append(t)
for process in processes:
    process.join()
Title("Discord Mass Dm - Finish")
print(f"{color.RED}[!] | Finish.")
Continue()
Reset()