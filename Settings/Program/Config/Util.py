from .Config import *

import colorama
import ctypes
import subprocess
import os
import time
import sys
from datetime import datetime

color_webhook = 0xa80505
color = colorama.Fore

def get_current_datetime():
    now = datetime.now()
    return now.hour, now.minute, now.second, now.year, now.day, now.month

def ModuleInstall(module):
    subprocess.check_call(['pip', 'install', module])

def Title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} | {title}")

def Reset():
    os.system("cls")
    file = 'python ./Settings/Start.py'
    subprocess.run(file, shell=True)

def Clear():
    os.system("cls")

def Exit():
    sys.exit()

def StartProgram(program):
    file = f'python ./Settings/Program/{program}'
    subprocess.run(file, shell=True)

def APprint(texte, delai=0.0000000001):
        for ligne in texte.split('\n'):
          for caractere in ligne:
              print(caractere, end='', flush=True)
              time.sleep(delai)
          print()  
          time.sleep(delai * 0)

def LAPprint(texte, delai=0.03):
        for ligne in texte.split('\n'):
          for caractere in ligne:
              print(caractere, end='', flush=True)
              time.sleep(delai)
          print()  
          time.sleep(delai * 0)

def Continue():
    input(color.RED + f"[!] | Press to continue -> " + color.RESET)
    
def ErrorChoice():
    print(f"{color.RED}[X] | Invalid Choice !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorId():
    print(f"{color.RED}[X] | Invalid ID !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorUrl():
    print(f"{color.RED}[X] | Invalid URL !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorEdge():
    print(f"{color.RED}[X] | Edge not installed or driver not up to date !")
    time.sleep(3)
    Reset()

def ErrorToken():
    print(f"{color.RED}[X] | Invalid Token !", color.RESET)
    time.sleep(3)
    Reset()
    
def ErrorNumber():
    print(f"{color.RED}[X] | Invalid Number !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorWebhook():
    print(f"{color.RED}[X] | Invalid Webhook !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorCookie():
    print(f"{color.RED}[X] | Invalid Cookie !", color.RESET)
    time.sleep(3)
    Reset()
