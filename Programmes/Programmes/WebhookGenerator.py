from Options.Options import *

import requests
import json
import string
import random

TitrePage("Webhook Générator + Checker")

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
username = 'Red-Tiger'
url = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'


choixwebhook = input(f"{couleur.RED}\n[?] | Webhook ? (y, n) -> {couleur.RESET}")
if choixwebhook in ['y']:
    webhook_url = input(f"{couleur.RED}\n[?] | URL Webhook -> {couleur.RESET}")

def send_webhook_message(webhook_url_Essai, content):
         payload = {
             'content': content
         }

         headers = {
             'Content-Type': 'application/json'
          }

         response = requests.post(webhook_url_Essai, data=json.dumps(payload), headers=headers)

         if response.status_code == 204:
          if choixwebhook in ['y']:
            print(f"{couleur.GREEN}[+] | {couleur.CYAN}{webhook_partie_variable}{couleur.GREEN} | Webhook Found | n°{nombre}{couleur.RESET}")

            embed_content = {
           'title': f'Webhook Found, Tests n°{nombre}',
           'description': f"**URL Webhook:__**\n```{webhook_url_Essai}```",
           'color': 0xf00020,
           'footer': {
            "text": "Red-Tiger",
            "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
             }
            }
            send_embed_webhook(webhook_url, embed_content, username, url)
          else:
                print(f"{couleur.GREEN}[+] | {couleur.CYAN}{webhook_partie_variable}{couleur.GREEN} | Webhook Found | n°{nombre}{couleur.RESET}")

         else:
             print(f"{couleur.RED}[X] | {couleur.CYAN}{webhook_partie_variable}{couleur.RED} | Webhook Invalid | n°{nombre}{couleur.RESET}")

nombre = 0
while True:
    nombre += 1
    
    chiffres = ''.join(random.choices(string.digits, k=18))
    caracteres = ''.join(random.choices(string.ascii_letters + string.digits, k=64))

    webhook_partie_variable = f'{chiffres}/{caracteres}'

    webhook_url_Essai = f'https://discord.com/api/webhooks/{webhook_partie_variable}'

    message_content = 'Webhook found By Red Tiger'

    send_webhook_message(webhook_url_Essai, message_content)
    TitrePage(f"Ip Générator + Checker | Tests n°{nombre}")