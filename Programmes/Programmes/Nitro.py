import requests
from bs4 import BeautifulSoup
import time

def verifier_contenu(url, contenu_a_verifier):
    try:
        # Obtenir le contenu HTML de la page avec un délai d'attente de 10 secondes
        reponse = requests.get(url, timeout=10)
        reponse.raise_for_status()

        # Attendre 2 secondes pour laisser la page se charger complètement
        time.sleep(2)

        # Utiliser BeautifulSoup pour analyser le HTML
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # Vérifier si le contenu spécifié est présent (insensible à la casse)
        if contenu_a_verifier.lower() in soup.get_text().lower():
            print(f"Le contenu '{contenu_a_verifier}' est présent sur la page.")
        else:
            print(f"Le contenu '{contenu_a_verifier}' n'est pas présent sur la page.")

    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la requête : {e}")

# Exemple d'utilisation avec une URL et un contenu à vérifier
url_a_verifier = "https://discord.gift/D5QKNbNx9EbkvWh2 "
contenu_a_verifier = "invalide"
verifier_contenu(url_a_verifier, contenu_a_verifier)