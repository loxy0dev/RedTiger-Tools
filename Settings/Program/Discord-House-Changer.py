from Config.Util import *
from Config.Config import *
import requests

Title("Discord House Changer")

print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Bravery
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Brilliance
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Balance
""")

house = input(f"{color.RED}-> {color.RESET}").lstrip("0")
token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")

validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
if validityTest.status_code != 200:
    ErrorToken()
else:
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    if house in ["1", "01"]: payload = {'house_id': 1}
    elif house in ["2", "02"]: payload = {'house_id': 2}
    elif house in ["3", "03"]: payload = {'house_id': 3}
    else:
        ErrorChoice()
    r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    if r.status_code == 204:
        print(f"{color.RED}[!] | Hypesquad house changed.")
        Continue()
        Reset()
    else:
        print(f"{color.RED}[X] | Hypesquad house has not changed.")