import colorama
import ctypes
import subprocess
import os
import time

nom = "Red-Tiger"
version = "v1.9.3"
codage = "Python"
language = "France"
createur = "Fluzypro"
discord = "https://discord.gg/eWNQ46jqdC"
nom_utilisateur = open('./Programmes/Programmes/Options/NomUtilisateur.txt', 'r').read()

couleur = colorama.Fore



def TitrePage(title):
    ctypes.windll.kernel32.SetConsoleTitleW(f"Red-Tiger {version} | {title}")



def Reset():
 try:
    os.system("cls")
    fichier = 'python ./Programmes/Start.py'
    subprocess.run(fichier, shell=True)
 except:
     print(couleur.RED + f"\n[ERREUR] | {couleur.LIGHTRED_EX}Veuillez relancer !\n" + couleur.RESET)



def APprint(texte, delai=0.001):
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