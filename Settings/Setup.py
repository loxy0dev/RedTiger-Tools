import subprocess
import os

os.system("cls")

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
try:
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

        nom_module = 'psutil'
        try:
         import psutil
        except:
         subprocess.check_call(['pip', 'install', nom_module])


        nom_module = 'bs4'
        try:
         import bs4
        except:
         subprocess.check_call(['pip', 'install', nom_module])

        nom_module = 'webbrowser'
        try:
         import webbrowser
        except:
         subprocess.check_call(['pip', 'install', nom_module])

        nom_module = 'itertools'
        try:
         from itertools import cycle
        except:
         subprocess.check_call(['pip', 'install', nom_module])

        from Program.Config.Util import Reset
        Reset()
except:
        print("[X] | Python is not installed with the \"PATH\" option !!")
        os.system("pause")