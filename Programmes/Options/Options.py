import os
import time
import subprocess
import ctypes
import colorama
import random
from random import *
import string
import requests
import time
import json
import sys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

nom = "Red-Tiger"
version = "v1.9.1"
codage = "Python"
language = "France"
createur = "Fluzypro"
discord = "https://discord.gg/VufERBgv9k"
nom_utilisateur = open('./Programmes/Options/NomUtilisateur.txt', 'r').read()

couleur = colorama.Fore



def TitrePage(title):
    ctypes.windll.kernel32.SetConsoleTitleW(f"Red-Tiger {version} | {title}")



def Reset():
    try:
         os.system("cls")
         fichier = 'python ./Start.py'
         subprocess.run(fichier, shell=True)

    except:
        result = subprocess.run(['./Start.exe'], check=False)

        if result.returncode == 0:
            print(couleur.RED + f"\n[ERREUR] | {couleur.LIGHTRED_EX}Veuillez relancer !\n" + couleur.RESET)
    
    else:
        result = subprocess.run(['./Start.exe'], check=False)

        if result.returncode == 0:
            print(couleur.RED + f"\n[ERREUR] | {couleur.LIGHTRED_EX}Veuillez relancer !\n" + couleur.RESET)



def ResetS():
    try:
         os.system("cls")
         fichier = 'python Start.py'
         subprocess.run(fichier, shell=True)

    except:
        result = subprocess.run(['Start.exe'], check=False)

        if result.returncode == 0:
            print(couleur.RED + f"\n[ERREUR] | {couleur.LIGHTRED_EX}Veuillez relancer !\n" + couleur.RESET)
    
    else:
        result = subprocess.run(['Start.exe'], check=False)

        if result.returncode == 0:
            print(couleur.RED + f"\n[ERREUR] | {couleur.LIGHTRED_EX}Veuillez relancer !\n" + couleur.RESET)



def APprint(texte, delai=0.002):
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