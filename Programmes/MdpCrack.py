import os
import time
import random


from Options.Options import *


TitrePage("Red-Tiger | Crack Mdp (Travaux)")

LAPprint(couleur.YELLOW + "\n[INFORMATION] | Pour l'instant c'est manuel mais bientot se sera automatique.\n")
LAPprint(couleur.RED + "\n[Choissez 10 mots et 2 symnole (. _) pour aider a craquer le mot de passe]\n")
LAPprint(couleur.RED + """Idéé de Mot:
- Nom et Prénom: (Nom, nom, Prenom, prenom) avec ou sens majuscule a la premiere lettre, sens accent.
- Code Postal: (30, 30000) les 2 premier ou le code entier.
- Date de naissance (J/M/A): (1, 10, 23)
- Et tout se que vous pouvez pour facilité.
    """)
mot1 = input(couleur.CYAN + "Mot 1: " + couleur.RESET)
mot2 = input(couleur.CYAN + "Mot 2: " + couleur.RESET)
mot3 = input(couleur.CYAN + "Mot 3: " + couleur.RESET)
mot4 = input(couleur.CYAN + "Mot 4: " + couleur.RESET)
mot5 = input(couleur.CYAN + "Mot 5: " + couleur.RESET)
mot6 = input(couleur.CYAN + "Mot 6: " + couleur.RESET)
mot7 = input(couleur.CYAN + "Mot 7: " + couleur.RESET)
mot8 = input(couleur.CYAN + "Mot 8: " + couleur.RESET)
mot9 = input(couleur.CYAN + "Mot 9: " + couleur.RESET)
mot10 = input(couleur.CYAN + "Mot 10 :" + couleur.RESET)
signe1 = input(couleur.CYAN + "Symbole 1 :" + couleur.RESET)
signe2 = input(couleur.CYAN + "Symbole 2 :" + couleur.RESET)

nb_mots_de_passe = int(input(couleur.RED + "\nNombre de Tentative (Recommander +1000) -> " + couleur.RESET))

def generer_mot_de_passe(longueur, mots_disponibles):

    mot_de_passe = ''.join(random.choice(mots_disponibles) for _ in range(longueur))
    return mot_de_passe

def generer_mots_de_passe(nb_mots_de_passe, longueur_min, longueur_max, mots_disponibles):

    mots_de_passe = set()

    while len(mots_de_passe) < nb_mots_de_passe:
        longueur_mots_de_passe = random.randint(longueur_min, longueur_max)
        mot_de_passe = generer_mot_de_passe(longueur_mots_de_passe, mots_disponibles)
        mots_de_passe.add(mot_de_passe)

    return list(mots_de_passe)

mots_disponibles = [mot1, mot2, mot3, mot4, mot5, mot6, mot7, mot8 , mot9 , mot10, signe1, signe2]

longueur_min = 1
longueur_max = 5

mots_de_passe_genere = generer_mots_de_passe(nb_mots_de_passe, longueur_min, longueur_max, mots_disponibles)

chemin = "./02-Potentiel-Mdp/MDP.txt"

fichier = open(chemin, 'w').write

print("/n")

for i, mot_de_passe in enumerate(mots_de_passe_genere, start=1):
    print(couleur.CYAN + f"Potentiel Mot de passe n°{i}   :   {couleur.BLUE}{mot_de_passe}")
    fichier(mot_de_passe + "\n")

print(couleur.RED + f"\nChemin d'accès au document texte:{couleur.CYAN} \"{chemin}\"" + couleur.RESET)
print(couleur.RED + f"\n[INFORMATION] | {couleur.LIGHTRED_EX}Renommez le fichier ou déplacez-le, car il sera réinitialisé !" + couleur.RESET)
time.sleep(3)
print(couleur.RED + f"\n[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez relancer !\n" + couleur.RESET)

os.system("pause")