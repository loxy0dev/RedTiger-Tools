from Config.Util import *
from Config.Config import *
import requests
import time

Title("Discord Token Status Changer")

token = input(f"{color.RED}\n{INPUT} Token -> {color.RESET}")
try:
    statue_number = int(input(f"{color.RED}{INPUT} How many statues do you want to cycle (max 4) -> {color.RESET}"))
except:
    ErrorNumber()

statues = []

headers = {'Authorization': token, 'Content-Type': 'application/json'}

if statue_number >= 1 and statue_number <= 4:
    for loop in range(0, statue_number):
        choice = str(input(f"{color.RED}{INPUT} Custom Status {loop+1} -> {color.RESET}"))
        statues.append(choice)
else:
    ErrorNumber()

while True:
    for i in range(len(statues)):
        CustomStatus = {"custom_status": {"text": statues[i]}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{statues[i]}{color.RED}")
            i += 1
            time.sleep(5)
        except Exception as e:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{statues[i]}{color.RED}")
            time.sleep(5)