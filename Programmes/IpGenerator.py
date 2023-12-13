#Module
import shutil, os
import time
import colorama
import requests
import time
import json
import subprocess
from random import *
import random

#Options
from Options.Options import version, nom, codage, language, createur, discord, couleur, Reset, LAPprint, APprint, TitrePage

#Titre de la page
TitrePage("Red-Tiger | Ip Générator + Chekeur")

def send_embed_webhook(webhook_url, embed_content):
                payload = {
                'embeds': [embed_content]
                 }

                headers = {
            'Content-Type': 'application/json'
             }

                response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

webhook = input(f"{couleur.RED}\nVoulez-vous annoncer une Ip valable avec un Webhook ? (y, n) -> {couleur.RESET}")
if webhook in ['y']:
    webhook_url = input(f"{couleur.RED}\nEntrez le lien du Webhook -> {couleur.RESET}")
def ping_ip(ip_address, nombre):

    try:
        # Utilisation de subprocess pour appeler la commande ping
        result = subprocess.run(['ping', '-n', '1', ip_address], capture_output=True, text=True, timeout=2)
        
        
        if webhook in ['y']:
            if result.returncode == 0:
             print(f"{couleur.GREEN}[+] | {couleur.CYAN}{ip_address}{couleur.GREEN} | Ip Trouvé (en ligne) | Tentative n°{nombre}{couleur.RESET}")
             embed_content = {
           'title': f'Ip Trouvé, tentative n°{nombre}',
           'description': f"**__Ip en ligne:__**\n```{ip_address}```\nIl se peut que l'ip ne sois plus en ligne d'ici là.",
           'color': 0xf00020,
           'footer': {
            "text": "Red-Tiger",
            "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
             }
            }

             send_embed_webhook(webhook_url, embed_content)


            else:
                  print(f"{couleur.RED}[X] | {couleur.CYAN}{ip_address}{couleur.RED} | Ip Fausse (non en ligne) | Tentative n°{nombre}{couleur.RESET}")
        if webhook in ['n']:
             if result.returncode == 0:
                print(f"{couleur.GREEN}[+] | {couleur.CYAN}{ip_address}{couleur.GREEN} | Ip Trouvé (en ligne) | Tentative n°{nombre}{couleur.RESET}")
             else:
                  print(f"{couleur.RED}[X] | {couleur.CYAN}{ip_address}{couleur.RED} | Ip Fausse (non en ligne) | Tentative n°{nombre}{couleur.RESET}")
             

    except subprocess.TimeoutExpired:
        print(f"{couleur.RED}[X] | {couleur.CYAN}{ip_address}{couleur.RED} | Ip Fausse (non en ligne) | Tentative n°{nombre}{couleur.RESET}")
nombre = 0
while True:
    nombre_random1 = random.randint(1, 200)
    nombre_random2 = random.randint(1, 200) 
    nombre_random3 = random.randint(1, 100) 
    nombre_random4 = random.randint(1, 100)
    
    nombre += 1
    ip = f'{nombre_random1}.{nombre_random2}.{nombre_random3}.{nombre_random4}'

    # Appel de la fonction ping_ip avec l'adresse IP spécifiée
    ping_ip(ip, nombre)
    TitrePage(f"Red-Tiger | Ip Générator + Chekeur | Tentative n°{nombre}")

    # Ajouter une petite pause pour ne pas inonder le réseau
    time.sleep(1)