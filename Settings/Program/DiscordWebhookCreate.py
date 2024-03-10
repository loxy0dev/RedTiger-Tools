from Config.Util import *
from Config.Config import *
import requests
import json

Title("Discord Webhook Create")

print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}]{color.RED} -> {color.WHITE}Message Classic
{color.WHITE}[{color.RED}02{color.WHITE}]{color.RED} -> {color.WHITE}Message Embed
""")
try:
    choice = int(input(f"{color.RED}-> {color.RESET}"))
except:
    ErrorChoice()
if choice == 1:
        def send_webhook_message(webhook_url, content):
         payload = {
             'content': content
         }

         headers = {
             'Content-Type': 'application/json'
          }

         response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

         if response.status_code == 204:
             print(f'{color.RED}[!] | Message Send.')
             Continue()
             Reset()
         else:
             print(f'{color.RED}[!] | Message not Send.')
             Continue()
             Reset()


        webhook_url = input(f"\n{color.RED}[?] | URL Webhook -> {color.RESET}")
        if webhook_url.lower().startswith("https://discord.com/api/webhooks"):

            message_content = input(f"{color.RED}[?] | Message -> {color.RESET}")
            send_webhook_message(webhook_url, message_content)
        
        else:
            ErrorUrl()


if choice == 2:

        def send_embed_webhook(webhook_url, embed_content):
            payload = {
            'embeds': [embed_content]
             }

            headers = {
            'Content-Type': 'application/json'
             }

            response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

            if response.status_code == 204:
                 print(f'{color.RED}[!] | Message Send.')
                 Continue()
                 Reset()
            else:
                 print(f'{color.RED}[!] | Message not Send.')
                 Continue()
                 Reset()
    
        webhook_url = input(f"\n{color.RED}[?] | URL Webhook -> {color.RESET}")

        print(f""" {color.RED}
{color.WHITE}[{color.RED}01{color.WHITE}]{color.RED} -> {color.WHITE}Red
{color.WHITE}[{color.RED}02{color.WHITE}]{color.RED} -> {color.WHITE}Orange
{color.WHITE}[{color.RED}03{color.WHITE}]{color.RED} -> {color.WHITE}Yellow
{color.WHITE}[{color.RED}04{color.WHITE}]{color.RED} -> {color.WHITE}Green
{color.WHITE}[{color.RED}05{color.WHITE}]{color.RED} -> {color.WHITE}Blue
{color.WHITE}[{color.RED}06{color.WHITE}]{color.RED} -> {color.WHITE}Magenta
{color.WHITE}[{color.RED}07{color.WHITE}]{color.RED} -> {color.WHITE}White
{color.WHITE}[{color.RED}08{color.WHITE}]{color.RED} -> {color.WHITE}Black 
""")
        try:
            color_input = int(input(f"{color.RED}[?] | Color -> {color.RESET}"))
            if color_input == 1:
                couleure = 0xFF0000  # Rouge
            elif color_input == 2:
                couleure = 0xFFA500  # Orange
            elif color_input == 3:
                couleure = 0xFFFF00  # Jaune
            elif color_input == 4:
                couleure = 0x00FF00  # Vert
            elif color_input == 5:
                couleure = 0x0080FF  # Bleu
            elif color_input == 6:
               couleure = 0x7f00ff  # Violet
            elif color_input == 7: 
                couleure = 0xffffff # Blanc
            elif color_input == 8:
                couleure = 0x000000 # Noir
            else:
                couleure = color_webhook  # Rouge (par défaut)
        except:
            couleure = color_webhook  # Rouge (par défaut)

        embed_content = {
           'title': input(f"{color.RED}[?] | Title ->{color.RESET} "),
           'description': input(f"{color.RED}[?] | Description ->{color.RESET} "),
           'color': couleure,
        }
        send_embed_webhook(webhook_url, embed_content)

else:
        ErrorChoice()