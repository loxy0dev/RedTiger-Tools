from Options.Options import *

import requests
import json
import time

TitrePage("Virus Create")

choix = input(f"{couleur.RED}\nVoulez vous le convertir en .exe ? -> {couleur.RESET}")
if choix in ['y']:
 