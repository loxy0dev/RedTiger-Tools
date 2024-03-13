from Config.Util import *
from Config.Config import *
import requests
import json
import string
import random

Title("Discord Webhook Generator")

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


choixwebhook = input(f"{color.RED}\n[?] | Webhook (y/n) -> {color.RESET}")
if choixwebhook in ['y', 'Y','Yes','yes']:
    webhook_url = input(f"{color.RED}[?] | URL Webhook -> {color.RESET}")

def send_webhook_message(webhook_url_Essai):
         response = requests.head(webhook_url_Essai)
         if response.status_code == 200:
          if choixwebhook in ['y']:
            print(f"{color.GREEN}[+] | Webhook Found | {color.WHITE}{webhook_partie_variable}{color.RESET}")

            embed_content = {
           'title': f'Webhook Found !',
           'description': f"**URL Webhook:__**\n```{webhook_url_Essai}```",
           'color': color_webhook,
           'footer': {
            "text": "Red Tiger",
            "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
             }
            }
            send_embed_webhook(webhook_url, embed_content, username, url)
          else:
                print(f"{color.GREEN}[+] | Webhook Found | {color.WHITE}{webhook_partie_variable}{color.RESET}")

         else:
             print(f"{color.RED}[X] | Webhook Invalid | {color.WHITE}{webhook_partie_variable}{color.RESET}")


while True:
    
    chiffres = ''.join(random.choices(string.digits, k=18))
    caracteres = ''.join(random.choices(string.ascii_letters + string.digits, k=64))

    webhook_partie_variable = f'{chiffres}/{caracteres}'

    webhook_url_Essai = f'https://discord.com/api/webhooks/{webhook_partie_variable}'

    send_webhook_message(webhook_url_Essai)
    Title(f"Webhook Generator | Webhook: {webhook_url_Essai}")