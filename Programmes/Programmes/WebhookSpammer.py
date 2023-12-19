from Options.Options import *

import requests
import json
import time

TitrePage("Webhook Spammer")

def send_webhook_message(webhook_url, message):
    payload = {'content': message}
    headers = {'Content-Type': 'application/json'}


    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


webhook_url = input(f"{couleur.RED}\nEntrer le lien du Webhook -> {couleur.RESET}")
if webhook_url.lower().startswith("https://discord.com/api/webhooks"):

    message_to_send = input(f"{couleur.RED}Entrer le message -> {couleur.RESET}")

    def repetition_action(nombre_de_repetitions):
     for i in range(1, nombre_de_repetitions + 1):
        try:
            send_webhook_message(webhook_url, message_to_send)
            print(f'{couleur.LIGHTRED_EX}[+] {couleur.RED}Message Envoyé | Message: "{couleur.CYAN}{message_to_send}{couleur.RED}" | Webhook: "{couleur.CYAN}{webhook_url}{couleur.RED}" | n°{i}{couleur.RESET}')
        except:
            print(f'{couleur.LIGHTRED_EX}[X] {couleur.RED}Erreur | Message: "{couleur.CYAN}{message_to_send}{couleur.RED}" | Webhook: "{couleur.CYAN}{webhook_url}{couleur.RED}"{couleur.RESET}')
            time.sleep(1)
else:
    LAPprint(f'\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez mettre un lien valide ! ex: "{couleur.CYAN}https://discord.com/api/webhooks/..{couleur.LIGHTRED_EX}".', couleur.RESET)
    time.sleep(5)
    Reset()
                
try:
        nombre_repetitions = int(input(f"{couleur.RED}Entrez le nombre de répétitions -> {couleur.RESET}"))
        repetition_action(nombre_repetitions)
except:
        LAPprint(f'\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez choisir un nombre !', couleur.RESET)
        Reset()

LAPprint(f"{couleur.RED}\n{nombre_repetitions} message(s) on été distribué avec succès !")
time.sleep(5)
Reset()

        