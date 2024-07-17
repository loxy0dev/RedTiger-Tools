# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
    ErrorModule(e)

Title("Obfuscator Tool (Paid)")

try:
    print(f"{INFO} The Obfuscator tool is a tool that makes any Python script undetectable by antivirus and makes the code unreadable")
    print(f"{INFO} The tool is paid and can be purchased on discord\n")
    webbrowser.open_new_tab(f"https://{discord_server}")
    Continue()
    Reset()
except Exception as e:
    Error(e)