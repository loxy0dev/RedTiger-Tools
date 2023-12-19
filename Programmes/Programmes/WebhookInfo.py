from Options.Options import *

import requests

TitrePage("Webhook Info")

def obtenir_informations_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(webhook_url, headers=headers)

    if response.status_code == 200:
        webhook_info = response.json()
        LAPprint(f"{couleur.RED}Informations du Webhook :\n")

        print(f"{couleur.YELLOW}Webhook ID      : {couleur.CYAN}", webhook_info['id'])
        print(f"{couleur.YELLOW}Webhook Token   : {couleur.CYAN}", webhook_info['token'])
        print(f"{couleur.YELLOW}Webhook Nom     : {couleur.CYAN}", webhook_info['name'])
        print(f"{couleur.YELLOW}Webhook Avatar  : {couleur.CYAN}", webhook_info['avatar'])
        print(f"{couleur.YELLOW}Webhook Type    : {couleur.CYAN}", "bot" if webhook_info['type'] == 1 else "webhook utilisateur")
        print(f"{couleur.YELLOW}Salon ID        : {couleur.CYAN}", webhook_info['channel_id'])
        print(f"{couleur.YELLOW}Serveur ID      : {couleur.CYAN}", webhook_info['guild_id'])
        
        if 'user' in webhook_info:
            user_info = webhook_info['user']

            LAPprint(f"{couleur.RED}\nInformations de l'utilisateur associé au Webhook :")

            print(f"{couleur.YELLOW}Utilisateur ID          : {couleur.CYAN}", user_info['id'])
            print(f"{couleur.YELLOW}Utilisateur Nom         : {couleur.CYAN}", user_info['username'])
            print(f"{couleur.YELLOW}Utilisateur Pseudo      : {couleur.CYAN}", user_info['global_name'])
            print(f"{couleur.YELLOW}Utilisateur Nombre      : {couleur.CYAN}", user_info['discriminator'])
            print(f"{couleur.YELLOW}Utilisateur Avatar      : {couleur.CYAN}", user_info['avatar'])
            print(f"{couleur.YELLOW}Utilisateur Flags       : {couleur.CYAN}", user_info['flags'], " Publique:", user_info['public_flags'])
            print(f"{couleur.YELLOW}Utilisateur Nitro       : {couleur.CYAN}", user_info['premium_type'])
            print(f"{couleur.YELLOW}Utilisateur Couleur     : {couleur.CYAN}", user_info['accent_color'])
            print(f"{couleur.YELLOW}Utilisateur Decoration  : {couleur.CYAN}", user_info['avatar_decoration_data'])
            print(f"{couleur.YELLOW}Utilisateur Baniere     : {couleur.CYAN}", user_info['banner_color'])
        else:
            print("\nAucune information sur l'utilisateur associé (peut être un webhook bot).")

    else:
        print(f"Erreur lors de la récupération des informations du webhook. Code de statut : {response.status_code}")

# Utilisation
webhook_url = input(f"{couleur.RED}\nWebhook -> {couleur.RESET}")
obtenir_informations_webhook(webhook_url)

input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
Reset()