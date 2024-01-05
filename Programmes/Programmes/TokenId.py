from Options.Options import *

import base64

TitrePage("Token Id")

userid = input(f"{couleur.RED}\nVictime ID -> {couleur.RESET}")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n{couleur.RED}Part One Token: \"{couleur.CYAN}{encodedStr}.{couleur.RED}\"{couleur.RESET}')

Continue()
Reset()