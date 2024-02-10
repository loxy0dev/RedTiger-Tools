import colorama
import ctypes
import subprocess
import os
import time
import sys

name_tool = "Red-Tiger"
version_tool = "v1.9.8"
coding_tool = "Python"
language_tool = "EN"
creator = "Fluzypro"
discord = "https://discord.gg/eWNQ46jqdC"
website = "https://red-tiger.000webhostapp.com/accueil.html"
username_user = open('./Programmes/Programmes/Options/NomUtilisateur.txt', 'r').read()
theme = open('./Programmes/Programmes/Options/Theme.txt', 'r').read()
color_webhook = 0xa80505
color = colorama.Fore



def Title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(f"Red-Tiger {version_tool} | {title}")


def Reset():
    os.system("cls")
    fichier = 'python ./Programmes/Start.py'
    subprocess.run(fichier, shell=True)

def Clear():
    os.system("cls")

def Exit():
    sys.exit()


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
    print(f"{color.RED}[!] | There is no choice !", color.RESET)
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
    
def ErrorNumber():
    print(f"{color.RED}[!] | Invalid Number !", color.RESET)
    time.sleep(3)
    Reset()
