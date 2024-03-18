from Config.Util import *
from Config.Config import *
import requests
import time

Title("Discord Status Changer")

token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")
try:
    statue_number = int(input(f"{color.RED}[?] | How many statues do you want to cycle (max 4) -> {color.RESET}"))
except:
    ErrorNumber()

try:
    times = int(input(f"{color.RED}[?] | Time between each change in seconds (Recommended time: 5) -> {color.RESET}"))
except:
    ErrorNumber()

statues = []

headers = {'Authorization': token, 'Content-Type': 'application/json'}

if statue_number >= 1 and statue_number <= 4:
    for loop in range(0, statue_number):
        choice = str(input(f"{color.RED}[?] | Choose Custom Status {loop+1} -> {color.RESET}"))
        statues.append(choice)
else:
    ErrorNumber()

while True:
    for i in range(len(statues)):
        CustomStatus = {"custom_status": {"text": statues[i]}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
            print(f"{color.RED}[+] | Status changed | {color.WHITE}{statues[i]}{color.RED}")
            Title(f"Discord Status Changer - Status: {statues[i]}")
            i += 1
            time.sleep(times)
        except Exception as e:
            print(f"{color.RED}[X] | Error | \"{color.WHITE}{e}{color.RED}\"")
            time.sleep(times)