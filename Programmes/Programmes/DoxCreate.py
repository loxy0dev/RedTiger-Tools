from Options.Options import *

import time
import os

TitrePage("Dox Create")

chemin = "./01-Dox-Create/DOX.txt"

print(couleur.RED + f"\nVictim information:\n")


fichier = open(chemin, 'w').write


print(couleur.RED + "Info Perso:")
nom = input(couleur.CYAN + "Name: " + couleur.RESET)
prenom = input(couleur.CYAN +"First Name: " + couleur.RESET)
datene = input(couleur.CYAN +"Date of birth: " + couleur.RESET)

print(couleur.RED + "\nInfo Pc:")
nompc= input(couleur.CYAN +"Name PC: " + couleur.RESET)
ip= input(couleur.CYAN +"Ip: " + couleur.RESET)

print(couleur.RED + "\nLocalisaton:")
pays = input(couleur.CYAN +"Country: " + couleur.RESET)
region = input(couleur.CYAN +"Regions: " + couleur.RESET)
postal= input(couleur.CYAN +"Postal Code: " + couleur.RESET)
ville = input(couleur.CYAN +"City: " + couleur.RESET)
rue = input(couleur.CYAN +"Street: " + couleur.RESET)

print(couleur.RED + "\nAccount/Mdp:")
print(couleur.YELLOW + "Discord:")
discord = input(couleur.CYAN + "Name: " + couleur.RESET)
token = input(couleur.CYAN + "Token: " + couleur.RESET)
mail= input(couleur.CYAN +"Mail address: " + couleur.RESET)
mdp= input(couleur.CYAN +"Password: " + couleur.RESET)

print(couleur.YELLOW + "\nMail:")
amail = input(couleur.CYAN + "Adress: " + couleur.RESET)
mmail = input(couleur.CYAN + "Password: " + couleur.RESET)

print(couleur.YELLOW + "\nPassword Possible:")
mdpp1 = input(couleur.CYAN + "Password 1: " + couleur.RESET)
mdpp2 = input(couleur.CYAN + "Password 2: " + couleur.RESET)
mdpp3 = input(couleur.CYAN + "Password 3: " + couleur.RESET)

autremdp= input(couleur.CYAN +"\nOther Accounts: " + couleur.RESET)

print(couleur.RED + "\Other Infos:")
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

fichier("\n\nName          :  " + nom)
fichier("\nFirst Name    :  " + prenom)
fichier("\nDate of birth :  " + datene)

fichier("\n\n------------------------Info Pc:-------------------------")
fichier("\n\nName Pc       :  " + nompc)
fichier("\nIp            :  " + ip)

fichier("\n\n----------------------Localisation:----------------------")

fichier("\n\nCountry       :  " + pays)
fichier("\nRegions       :  " + region)
fichier("\nPostal Code   :  " + postal)
fichier("\nCity          :  " + ville)
fichier("\nStreet        :  " + rue)

fichier("\n\n-----------------------Compte/Mdp:-----------------------")

fichier("\n\nDiscord:")

fichier("\nName          :  " + discord)
fichier("\nToken         :  " + token)
fichier("\nAdress Mail   :  " + mail)
fichier("\nPassword      :  " + mdp)

fichier("\n\nMail:")
fichier("\nAdress        :  " + amail)
fichier("\nPassword      :  " + mmail)

fichier("\n\nPassword Possible  :  " + mdpp1 + " - " + mdpp2 + " - " + mdpp3)

fichier("\n\nOther Accounts:")

fichier("\n" + autremdp)

fichier("\n\n----------------------Other Infos:----------------------")
fichier("\n\n" + autreinfo)


open(chemin, 'w').close()


print(couleur.RED + f"\nThe DOX was sent to: {couleur.CYAN}\"{chemin}\""+ couleur.RESET)
time.sleep(3)
Continue()