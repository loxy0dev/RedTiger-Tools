from Options.Options import *

import string
import time
import random
import os

TitrePage("Mdp Générator")


caractere = list(string.ascii_letters+string.digits+'AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890...---___')


try:
    nombre = int(input(couleur.RED + "\nNombre de caractère -> " + couleur.RESET))
    time.sleep(0.2)
    fois = int(input(couleur.RED + "\nNombre de Mot de passe a générer -> " + couleur.RESET))
    time.sleep(0.2)
except:
    print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Choisissez un nombre !", couleur.RESET)
    time.sleep(3)
    Reset()



def genenerate_password():
    random.shuffle(caractere)
    password=[]
    for i in range(nombre):
        password.append(random.choice(caractere))
    random.shuffle(password)
    return "".join(password)


print(couleur.RED + "\nVoici les mots de passe que je vous propose:\n" + couleur.RESET)
time.sleep(1)
for n in range(fois):
    time.sleep(0.05)
    print(couleur.CYAN + genenerate_password() + couleur.RESET)


input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
Reset()

os.system("pause")