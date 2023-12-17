
from Options.Options import *

TitrePage("Dox Create")

chemin = "./01-Dox-Créés/DOX.txt"


print(couleur.RED + f"\n[INFORMATION] | {couleur.LIGHTRED_EX} Vous pouvez modifier les informations a tout moment.")
print(couleur.RED + f"[INFORMATION] | {couleur.LIGHTRED_EX} Skipez la questions si vous ne s'avaez pas quoi mettre.")
print(couleur.RED + f"\nEntrez les informations de votre victime:\n")


fichier = open(chemin, 'w').write


print(couleur.RED + "Info Perso:")
nom = input(couleur.CYAN + "Nom: " + couleur.RESET)
prenom = input(couleur.CYAN +"Prénom: " + couleur.RESET)
datene = input(couleur.CYAN +"Date Naissance: " + couleur.RESET)

print(couleur.RED + "\nInfo Pc:")
nompc= input(couleur.CYAN +"Nom Du PC: " + couleur.RESET)
ip= input(couleur.CYAN +"Ip: " + couleur.RESET)

print(couleur.RED + "\nLocalisaton:")
pays = input(couleur.CYAN +"Pays: " + couleur.RESET)
region = input(couleur.CYAN +"Régions: " + couleur.RESET)
postal= input(couleur.CYAN +"Code Postal: " + couleur.RESET)
ville = input(couleur.CYAN +"Ville: " + couleur.RESET)
rue = input(couleur.CYAN +"Rue: " + couleur.RESET)

print(couleur.RED + "\nCompte/Mdp:")
print(couleur.YELLOW + "Discord:")
discord = input(couleur.CYAN + "Nom: " + couleur.RESET)
token = input(couleur.CYAN + "Token: " + couleur.RESET)
mail= input(couleur.CYAN +"Adresse Mail: " + couleur.RESET)
mdp= input(couleur.CYAN +"Mot de passe: " + couleur.RESET)

print(couleur.YELLOW + "\nMail:")
amail = input(couleur.CYAN + "Adresse: " + couleur.RESET)
mmail = input(couleur.CYAN + "Mot De Passe: " + couleur.RESET)

print(couleur.YELLOW + "\nMdp Possible:")
mdpp1 = input(couleur.CYAN + "Mdp: " + couleur.RESET)
mdpp2 = input(couleur.CYAN + "Mdp: " + couleur.RESET)
mdpp3 = input(couleur.CYAN + "Mdp: " + couleur.RESET)

autremdp= input(couleur.CYAN +"\nAutres Comptes: " + couleur.RESET)

print(couleur.RED + "\nAutres Infos:")
autreinfo= input(couleur.CYAN +"Info: " + couleur.RESET)


fichier(""" ^^^ Enregistrer sous... | Ctrl + Maj + S
        
        oooooooooo.     .oooooo.   ooooooo  ooooo 
        `888'   `Y8b   d8P'  `Y8b   `8888    d8'  
         888      888 888      888    Y888..8P    
         888      888 888      888     `8888'     
         888      888 888      888    .8PY888.    
         888     d88' `88b    d88'   d8'  `888b   
        o888bood8P'    `Y8bood8P'  o888o  o88888o   By Red-Tiger
_________________________________________________________________                        

""")

fichier("-----------------------Info Perso:-----------------------")

fichier("\n\nNom           :  " + nom)
fichier("\nPrenom        :  " + prenom)
fichier("\nDate Naissance:  " + datene)

fichier("\n\n------------------------Info Pc:-------------------------")
fichier("\n\nNom Du Pc     :  " + nompc)
fichier("\nIp            :  " + ip)

fichier("\n\n----------------------Localisation:----------------------")

fichier("\n\nPays          :  " + pays)
fichier("\nRegions       :  " + region)
fichier("\nCode Postal   :  " + postal)
fichier("\nVille         :  " + ville)
fichier("\nRue           :  " + rue)

fichier("\n\n-----------------------Compte/Mdp:-----------------------")

fichier("\n\nDiscord:")

fichier("\nNom           :  " + discord)
fichier("\nToken         :  " + token)
fichier("\nAdresse Mail  :  " + mail)
fichier("\nMot de passe  :  " + mdp)

fichier("\n\nMail:")
fichier("\nAdresse       :  " + amail)
fichier("\nMot De Passe  :  " + mmail)

fichier("\n\nMdp Possible  :  " + mdpp1 + " - " + mdpp2 + " - " + mdpp3)

fichier("\n\nAutres Comptes:")

fichier("\n" + autremdp)

fichier("\n\n----------------------Autres Infos:----------------------")
fichier("\n\n" + autreinfo)


open(chemin, 'w').close()



print(couleur.RED + "\nToute les informations on été recueilli avec succès :)")

input(couleur.RED + "\nFaites entrer pour sauvegarder: " + couleur.RESET)
time.sleep(1)
print(couleur.CYAN + "Sauvegarde en cours...")
time.sleep(3)
print(couleur.RED + "Sauvegarde effectuer !")
print(couleur.RED + f"\nChemin d'accès au document texte: {couleur.CYAN}\"{chemin}\""+ couleur.RESET)
print(couleur.RED + f"\n[INFORMATION] | {couleur.LIGHTRED_EX}Renommez le fichier ou déplacez-le, car il sera réinitialisé !" + couleur.RESET)
time.sleep(3)
print(couleur.RED + f"\n[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez relancer !\n" + couleur.RESET)

os.system("pause")