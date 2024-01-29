from Options.Options import *

import string
import time
import random
import os

TitrePage("Password Générator")


caractere = list(string.ascii_letters+string.digits+'AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890...---___')


try:
    nombre = int(input(couleur.RED + "\n[?] | Character Number -> " + couleur.RESET))
    time.sleep(0.2)
    fois = int(input(couleur.RED + "[?] | Generate Number -> " + couleur.RESET))
    time.sleep(0.2)
except:
    ErreurNombre()



def genenerate_password():
    random.shuffle(caractere)
    password=[]
    for i in range(nombre):
        password.append(random.choice(caractere))
    random.shuffle(password)
    return "".join(password)


print(couleur.RED + "\nPassword Generate:" + couleur.RESET)
time.sleep(1)
for n in range(fois):
    time.sleep(0.05)
    print(couleur.CYAN + genenerate_password() + couleur.RESET)

print("")
Continue()
Reset()

os.system("pause")