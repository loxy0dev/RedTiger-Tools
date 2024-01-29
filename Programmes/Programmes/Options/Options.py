import colorama
import ctypes
import subprocess
import os
import time

nom = "Red-Tiger"
version = "v1.9.7"
codage = "Python"
language = "EN"
createur = "Fluzypro"
discord = "https://discord.gg/eWNQ46jqdC"
siteweb = "https://red-tiger.000webhostapp.com/accueil.html"
nom_utilisateur = open('./Programmes/Programmes/Options/NomUtilisateur.txt', 'r').read()
theme = open('./Programmes/Programmes/Options/Theme.txt', 'r').read()

couleur = colorama.Fore



def TitrePage(title):
    ctypes.windll.kernel32.SetConsoleTitleW(f"Red-Tiger {version} | {title}")



def Reset():
    os.system("cls")
    fichier = 'python ./Programmes/Start.py'
    subprocess.run(fichier, shell=True)



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
    input(couleur.RED + f"[!] | Press to continue -> " + couleur.RESET)
    
def ErreurChoix():
    print(f"{couleur.RED}[!] | There is no choice !", couleur.RESET)
    time.sleep(3)
    Reset()

def ErreurId():
    print(f"{couleur.RED}[!] | Invalid ID !", couleur.RESET)
    time.sleep(3)
    Reset()

def ErreurUrl():
    print(f"{couleur.RED}[!] | Invalid URL !", couleur.RESET)
    time.sleep(3)
    Reset()
    
def ErreurNombre():
    print(f"{couleur.RED}[!] | Invalid Number !", couleur.RESET)
    time.sleep(3)
    Reset()
