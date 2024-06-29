# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token House Changer")

try:
    print()
    token = Choice1TokenDiscord()
    print(f"""
    {color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Bravery
    {color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Brilliance
    {color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Balance
    """)

    house = input(f"{color.RED}{INPUT} House -> {color.RESET}").lstrip("0")

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
            print(f"{color.RED}{INFO} Hypesquad house changed.")
            Continue()
            Reset()
        else:
            print(f"{color.RED}{ERROR} Hypesquad house has not changed.")
except Exception as e:
    Error(e)