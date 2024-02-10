from Options.Options import *

import base64

Title("Token Id")

userid = input(f"{color.RED}\n[?] | Victime ID -> {color.RESET}")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n{color.RED}Part One Token: \"{color.CYAN}{encodedStr}.{color.RED}\"{color.RESET}')

Continue()
Reset()