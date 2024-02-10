from Options.Options import *

import string
import time
import random
import os

Title("Password Générator")


caractere = list(string.ascii_letters+string.digits+'AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890...---___')


try:
    nombre = int(input(color.RED + "\n[?] | Character Number -> " + color.RESET))
    time.sleep(0.2)
    fois = int(input(color.RED + "[?] | Generate Number -> " + color.RESET))
    time.sleep(0.2)
except:
    ErrorNumber()



def genenerate_password():
    random.shuffle(caractere)
    password=[]
    for i in range(nombre):
        password.append(random.choice(caractere))
    random.shuffle(password)
    return "".join(password)


print(color.RED + "\nPassword Generate:" + color.RESET)
time.sleep(1)
for n in range(fois):
    time.sleep(0.05)
    print(color.CYAN + genenerate_password() + color.RESET)

print("")
Continue()
Reset()

os.system("pause")