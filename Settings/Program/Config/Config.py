import colorama
import ctypes
import subprocess
import os
import time
import sys

name_tool = "Red Tiger"
version_tool = "2.2.0"
coding_tool = "Python"
language_tool = "EN"
creator = "FluzyTeck"
discord_server = "discord.gg/eWNQ46jqdC"
website = "red-tiger.000webhostapp.com/accueil.html"
github_tool = "github.com/fluzyteck/RedTiger"
color_webhook = 0xa80505
color = colorama.Fore


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
    print(f"{color.RED}[!] | Invalid Choice !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorId():
    print(f"{color.RED}[!] | Invalid ID !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorUrl():
    print(f"{color.RED}[!] | Invalid URL !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorToken():
    print(f"{color.RED}[!] | Invalid Token !", color.RESET)
    time.sleep(3)
    Reset()
    
def ErrorNumber():
    print(f"{color.RED}[!] | Invalid Number !", color.RESET)
    time.sleep(3)
    Reset()
