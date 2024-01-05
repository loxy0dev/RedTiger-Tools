from Options.Options import *

import time
import os

TitrePage("Ip Pinger")

hostname = input(couleur.RED + "\nIP -> " + couleur.RESET)

print(couleur.RED + f"\nInformation Ip \"{hostname}\":{couleur.RESET}")
time.sleep(0.5)
response = os.system("ping -n 1 " + hostname)
if response == 0:
    response = 0
    pingstatus = "Network Active"
    LAPprint(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}IP Online." + couleur.RESET)
else:
    pingstatus = "Network Error"
    LAPprint(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}IP Offline." + couleur.RESET)

Continue()
Reset()

os.system("pause")