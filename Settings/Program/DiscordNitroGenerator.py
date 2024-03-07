from Config.Config import *

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

import random
import string
import json
import requests

Title("Nitro Generator")

webhook = input(f"{color.RED}\n[?] | Webhook ? (y, n) -> {color.RESET}")

if webhook in ['y']:
    webhook_url = input(f"{color.RED}[?] | URL Webhook -> {color.RESET}")

webdriver_path = './Driver/msedgedriver.exe'

edge_options = EdgeOptions()
edge_options.use_chromium = True

edge_service = EdgeService(webdriver_path)

driver = webdriver.Edge(service=edge_service, options=edge_options)

while True:
 
 def generer_caracteres_aleatoires(longueur):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longueur))

 chaine_aleatoire = generer_caracteres_aleatoires(16)

 site_url = f'https://discord.com/gifts/{chaine_aleatoire}'
 driver.get(site_url)

 driver.implicitly_wait(0)

 console = driver.execute_script("return console")

 search_term = 'Unrecognized'
 console_logs = driver.get_log('browser')

 found = False
 for log in console_logs:
    if search_term in log['message']:
        found = True
        break

 if found:
    print(f"{color.RED}[X] | {color.CYAN}{site_url}{color.RED} | Nitro Invalid{color.RESET}")
 else:
  if "1015" in driver.page_source:
    print(f"{color.RED}[X] | {color.CYAN}{site_url}{color.RED} | Error 1015{color.RESET}")
    time.sleep(0.3)
  else:
         if webhook in ['y']:
            def send_embed_webhook(webhook_url, embed_content):
                payload = {
                'embeds': [embed_content],
                'username': username,
                'avatar_url': url,
                'content': message
                 }

                headers = {
            'Content-Type': 'application/json'
             }

                response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
            username = 'Red-Tiger'
            url = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'
            message = site_url
            embed_content = {
           'title': f'Nitro Found !',
           'description': f"**__Nitro:__**\n```{site_url}```",
           'color': color_webhook,
           'footer': {
            "text": "Red-Tiger",
            "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
             }
            }

            send_embed_webhook(webhook_url, embed_content)
            print(f"{color.GREEN}[+] | {color.CYAN}{site_url}{color.GREEN} | Nitro Found{color.RESET}")
         else:
           print(f"{color.GREEN}[+] | {color.CYAN}{site_url}{color.GREEN} | Nitro Found{color.RESET}")
 continue