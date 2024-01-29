import subprocess
import os

os.system("cls")

nom_utilisateur = os.getlogin()
with open('./Programmes/Programmes/Options/NomUtilisateur.txt', 'w') as fichier:
 fichier.write(f"{nom_utilisateur}'s")

with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
 fichier.write("RED")



print("""
			   ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███  
			  ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
			  ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
			  ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
			  ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
			  ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
			    ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
			   ░░   ░    ░    ░ ░  ░      ░       ▒ ░░ ░   ░    ░     ░░   ░ 
 			    ░        ░  ░   ░                 ░        ░    ░  ░   ░     

""")

nom_module = 'selenium'
try:
 import selenium
except:
 subprocess.check_call(['pip', 'install', nom_module]) 
        

nom_module = 'colorama'
try:
 import colorama
except:
 subprocess.check_call(['pip', 'install', nom_module]) 

nom_module = 'time'
try:
 import time
except:
 subprocess.check_call(['pip', 'install', nom_module]) 

nom_module = 'requests'
try:
 import requests
except:
 subprocess.check_call(['pip', 'install', nom_module]) 

nom_module = 'json'
try:
 import json
except:
 subprocess.check_call(['pip', 'install', nom_module]) 

nom_module = 'random'
try:
 import random
except:
 subprocess.check_call(['pip', 'install', nom_module]) 

nom_module = 'string'
try:
 import string
except:
 subprocess.check_call(['pip', 'install', nom_module]) 
    
nom_module = 'ctypes'
try:
 import ctypes
except:
 subprocess.check_call(['pip', 'install', nom_module]) 

nom_module = 'base64'
try:
 import base64
except:
 subprocess.check_call(['pip', 'install', nom_module]) 

nom_module = 'threading'
try:
 import threading
except:
 subprocess.check_call(['pip', 'install', nom_module]) 

from Programmes.Options.Options import Reset

nom_module = 'psutil'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'pyinstaller'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'auto-py-to-exe'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'bs4'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")
        
from Programmes.Options.Options import Reset
Reset()