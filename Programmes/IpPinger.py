#Module
import shutil, os
import time
import subprocess
import ctypes
import colorama
from random import *

#Options
from Options.Options import version, nom, codage, language, createur, discord, couleur, Reset, LAPprint, APprint, TitrePage

#Titre de la page
TitrePage("Red-Tiger | Ip Pinger")

hostname = input(couleur.RED + "\nIP -> " + couleur.RESET)

print(couleur.RED + f"\nInformation de l'ip \"{hostname}\":{couleur.RESET}")
time.sleep(0.5)
response = os.system("ping -n 1 " + hostname)
if response == 0:
    response = 0
    pingstatus = "Network Active"
    LAPprint(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}L'IP est en ligne.\n" + couleur.RESET)
else:
    pingstatus = "Network Error"
    LAPprint(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}L'IP est hors ligne.\n" + couleur.RESET)

input(couleur.RED + "Fais entrer pour continuer -> " + couleur.RESET)
Reset()

os.system("pause")