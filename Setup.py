# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

import sys
import os

print("\nInstalling the python modules required for the RedTiger Tool:")

if sys.platform.startswith("win"):
    "WINDOWS"
    os.system("python.exe -m pip install --upgrade pip")
    os.system("pip install --upgrade pip")
    os.system("pip install --upgrade pip setuptools wheel")
    os.system("pip install bcrypt")
    os.system("pip install deep-translator")
    os.system("pip install dnspython")
    os.system("pip install time")
    os.system("pip install selenium")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install json")
    os.system("pip install random")
    os.system("pip install string")
    os.system("pip install ctypes")
    os.system("pip install base64")
    os.system("pip install threading")
    os.system("pip install psutil")
    os.system("pip install bs4")
    os.system("pip install webbrowser")
    os.system("pip install itertools")
    os.system("pip install phonenumbers")
    os.system("pip install discord")
    os.system("pip install discord.py")
    os.system("pip install PyQt5")
    os.system("pip install PyQtWebEngine")
    os.system("pip install pytube")
    os.system("pip install cryptography")
    os.system("pip install pycryptodome")
    os.system("pip install pywin32")
    print("Finish.")
    os.system("python RedTiger.py")

elif sys.platform.startswith("linux"):
    "LINUX"
    os.system("python.exe -m pip3 install --upgrade pip")
    os.system("pip3 install --upgrade pip")
    os.system("pip3 install --upgrade pip setuptools wheel")
    os.system("pip3 install bcrypt")
    os.system("pip3 install deep-translator")
    os.system("pip3 install dnspython")
    os.system("pip3 install time")
    os.system("pip3 install selenium")
    os.system("pip3 install colorama")
    os.system("pip3 install requests")
    os.system("pip3 install json")
    os.system("pip3 install random")
    os.system("pip3 install string")
    os.system("pip3 install ctypes")
    os.system("pip3 install base64")
    os.system("pip3 install threading")
    os.system("pip3 install psutil")
    os.system("pip3 install bs4")
    os.system("pip3 install webbrowser")
    os.system("pip3 install itertools")
    os.system("pip3 install phonenumbers")
    os.system("pip3 install discord")
    os.system("pip3 install discord.py")
    os.system("pip3 install PyQt5")
    os.system("pip3 install PyQtWebEngine")
    os.system("pip3 install pytube")
    os.system("pip3 install cryptography")
    os.system("pip3 install pycryptodome")
    os.system("pip3 install pywin32")
    print("Finish.")
    os.system("python3 RedTiger.py")
