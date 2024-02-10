from Options.Options import *

import requests
import json
import time

Title("Webhook Create")

print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Message Classic
{color.LIGHTRED_EX}[02]{color.RED} -> Message Embed
""")
choix = int(input(f"[->] {color.RESET}"))
try:
    
    if choix == 1:
        choix = 1
        def send_webhook_message(webhook_url, content):
         payload = {
             'content': content
         }

         headers = {
             'Content-Type': 'application/json'
          }

         response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

         if response.status_code == 204:
             LAPprint(f'\n{color.RED}[!] | {color.LIGHTRED_EX}Message Send.')
             time.sleep(5)
             Reset()
         else:
             LAPprint(f'\n{color.RED}[!] | {color.LIGHTRED_EX}Message not Send.')
             time.sleep(5)
             Reset()


        webhook_url = input(f"{color.RED}URL Webhook -> {color.RESET}")
        if webhook_url.lower().startswith("https://discord.com/api/webhooks"):

            message_content = input(f"{color.RED}\nMessage -> {color.RESET}")
            send_webhook_message(webhook_url, message_content)
        
        else:
            ErrorUrl()


    if choix == 2:
        choix = 2

        def send_embed_webhook(webhook_url, embed_content):
            payload = {
            'embeds': [embed_content]
             }

            headers = {
            'Content-Type': 'application/json'
             }

            response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

            if response.status_code == 204:
               LAPprint(f'\n{color.RED}[!] | {color.LIGHTRED_EX}Message Send.')
               time.sleep(5)
               Reset()
            else:
             LAPprint(f'\n{color.RED}[!] | {color.LIGHTRED_EX}Message not Send.')
             time.sleep(5)
             Reset()
    
        webhook_url = input(f"{color.RED}\n[?] | URL Webhook -> {color.RESET}")

        print(f""" {color.RED}
{color.LIGHTRED_EX}[01]{color.RED} -> Red
{color.LIGHTRED_EX}[02]{color.RED} -> Orange
{color.LIGHTRED_EX}[03]{color.RED} -> Yellow
{color.LIGHTRED_EX}[04]{color.RED} -> Green
{color.LIGHTRED_EX}[05]{color.RED} -> Blue
{color.LIGHTRED_EX}[06]{color.RED} -> Magenta
{color.LIGHTRED_EX}[07]{color.RED} -> White
{color.LIGHTRED_EX}[08]{color.RED} -> Black 
""")
        try:
            couleur_input = int(input(f"{color.RED}[?] | Color -> {color.RESET}"))
            if couleur_input == 1:
                couleure = 0xFF0000  # Rouge
            elif couleur_input == 2:
                couleure = 0xFFA500  # Orange
            elif couleur_input == 3:
                couleure = 0xFFFF00  # Jaune
            elif couleur_input == 4:
                couleure = 0x00FF00  # Vert
            elif couleur_input == 5:
                couleure = 0x0080FF  # Bleu
            elif couleur_input == 6:
               couleure = 0x7f00ff  # Violet
            elif couleur_input == 7: 
                couleure = 0xffffff # Blanc
            elif couleur_input == 8:
                couleure = 0x000000 # Noir
            else:
                couleure = color_webhook  # Rouge (par défaut)
        except:
            couleure = color_webhook  # Rouge (par défaut)

        embed_content = {
           'title': input(f"{color.RED}[?] | Title ->{color.RESET} "),
           'description': input(f"{color.RED}[?] | Description ->{color.RESET} "),
           'color': couleure,
           'footer': {
                "text": "Red-Tiger",
                "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
                    }
        }
        send_embed_webhook(webhook_url, embed_content)

    else:
        ErrorChoice
except ValueError as e:
    ErrorChoice