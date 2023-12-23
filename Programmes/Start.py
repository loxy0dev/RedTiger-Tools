from Programmes.Options.Options import *

import sys
import subprocess
import os
import time

print(f"Version {version}")
time.sleep(2)
while True:
  nouvelle_couleur = open('Programmes/Programmes/Options/Theme.txt', 'r').read()
  couleur.RED = getattr(couleur, nouvelle_couleur, couleur.RED)
  couleur.LIGHTRED_EX = getattr(couleur, f"LIGHT{nouvelle_couleur}_EX", couleur.LIGHTRED_EX)

  TitrePage("Start")

  os.system("cls")

  print(couleur.RED + f"""     
                                                      
			   ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███   │Grabb: {couleur.LIGHTRED_EX}aucun{couleur.RED}
			  ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒ │Virus: {couleur.LIGHTRED_EX}aucun{couleur.RED}
			  ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒ ├───────────────
			  ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄   │Version: {couleur.LIGHTRED_EX}{version}{couleur.RED}
			  ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒ │By: {couleur.LIGHTRED_EX}{createur}{couleur.RED}
			  ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ├───────────────
			    ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░ │Username: {couleur.LIGHTRED_EX}{nom_utilisateur}{couleur.RED}
			   ░░   ░    ░    ░ ░  ░      ░       ▒ ░░ ░   ░    ░     ░░   ░   │Site: {couleur.LIGHTRED_EX}[02]{couleur.RED}
 			    ░        ░  ░   ░                 ░        ░    ░  ░   ░     

> Change Theme -> {couleur.LIGHTRED_EX}[?]{couleur.RED} 
> Change Username -> {couleur.LIGHTRED_EX}[!]{couleur.RED}
> Exit -> {couleur.LIGHTRED_EX}[0]{couleur.RED}
╔═══                              ═══╗ ╔═══            {couleur.LIGHTRED_EX}Discord:{couleur.RED}            ═══╗ ╔═══                                ═══╗
║                                    ║ ║                                      ║ ║                                      ║
    {couleur.LIGHTRED_EX}[01]{couleur.RED} -> Info                           {couleur.LIGHTRED_EX}[08]{couleur.RED} -> Webhook Catégorie (4)            {couleur.LIGHTRED_EX}[15]{couleur.RED} ->           
    {couleur.LIGHTRED_EX}[02]{couleur.RED} -> Site internet (2)              {couleur.LIGHTRED_EX}[09]{couleur.RED} -> Token Catégorie (2)              {couleur.LIGHTRED_EX}[16]{couleur.RED} -> 
    {couleur.LIGHTRED_EX}[03]{couleur.RED} -> Ip Catégorie (3)               {couleur.LIGHTRED_EX}[10]{couleur.RED} -> Invite Catégorie (1)             {couleur.LIGHTRED_EX}[17]{couleur.RED} -> 
    {couleur.LIGHTRED_EX}[04]{couleur.RED} -> Mdp Catégorie (2)              {couleur.LIGHTRED_EX}[11]{couleur.RED} ->                                  {couleur.LIGHTRED_EX}[18]{couleur.RED} -> 
    {couleur.LIGHTRED_EX}[05]{couleur.RED} -> Stealer Catégorie (2)          {couleur.LIGHTRED_EX}[12]{couleur.RED} ->                                  {couleur.LIGHTRED_EX}[19]{couleur.RED} -> 
    {couleur.LIGHTRED_EX}[06]{couleur.RED} ->                                {couleur.LIGHTRED_EX}[13]{couleur.RED} ->                                  {couleur.LIGHTRED_EX}[20]{couleur.RED} -> 
    {couleur.LIGHTRED_EX}[07]{couleur.RED} ->                                {couleur.LIGHTRED_EX}[14]{couleur.RED} ->                                  {couleur.LIGHTRED_EX}[21]{couleur.RED} -> 
║                                    ║ ║                                      ║ ║                                      ║
╚═══                              ═══╝ ╚═══                                ═══╝ ╚═══                                ═══╝
""")


  choix = input(couleur.RED + f"[->] " + couleur.RESET)
  
  try:

        if choix in ['0', '00', 'exit', 'Exit']:
            LAPprint(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Fermeture" + couleur.RESET)
            time.sleep(1)
            sys.exit()

        if choix in ['1', '01', 'info', 'Info']:
            commande = 'python ./Programmes/Programmes/Info.py'
            subprocess.run(commande, shell=True)

        if choix in ['2', '02', 'discord', 'Discord']:
            print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Site Red-Tiger
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Serveur Discord
""")
            choixWebhook = input(couleur.RED + f"[->] " + couleur.RESET)
            if choixWebhook in ['1', '01']:
             commande = 'python ./Programmes/Programmes/Site.py'
             subprocess.run(commande, shell=True)
            if choixWebhook in ['2', '02']:
             commande = 'python ./Programmes/Programmes/Discord.py'
             subprocess.run(commande, shell=True)



        if choix in ['3', '03']:
           print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Ip Pinger
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Ip Generator + Chekeur
{couleur.LIGHTRED_EX}[03]{couleur.RED} -> Ip Stresser
""")        
           choixWebhook = input(couleur.RED + f"[->] " + couleur.RESET)
           if choixWebhook in ['1', '01']:
              commande = 'python ./Programmes/Programmes/IpPinger.py'
              subprocess.run(commande, shell=True)

           if choixWebhook in ['2', '02']:
              commande = 'python ./Programmes/Programmes/IpGenerator.py'
              subprocess.run(commande, shell=True)

           if choixWebhook in ['3', '03']:
              commande = 'python ./Programmes/Programmes/IpStresser.py'
              subprocess.run(commande, shell=True)
            
           else:
             print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
             time.sleep(3)
             os.system("cls")
             continue
        


        if choix in ['4', '04']:
           print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Mdp Generator
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Mdp Crack (travaux)
""")        
           choixWebhook = input(couleur.RED + f"[->] " + couleur.RESET)
           if choixWebhook in ['1', '01']:
              commande = 'python ./Programmes/Programmes/MdpGenerator.py'
              subprocess.run(commande, shell=True)

           if choixWebhook in ['2', '02']:
              commande = 'python ./Programmes/Programmes/MdpCrack.py'
              subprocess.run(commande, shell=True)
            
           else:
             print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
             time.sleep(3)
             os.system("cls")
             continue
        


        if choix in ['5', '05']:
           print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Stealer Create (.Exe)
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Dox Create
""")        
           choixWebhook = input(couleur.RED + f"[->] " + couleur.RESET)
           if choixWebhook in ['1', '01']:
              commande = 'python ./Programmes/Programmes/StealerCreate.py'
              subprocess.run(commande, shell=True)

           if choixWebhook in ['2', '02']:
              commande = 'python ./Programmes/Programmes/DoxCreate.py'
              subprocess.run(commande, shell=True)
            
           else:
             print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
             time.sleep(3)
             os.system("cls")
             continue



        if choix in ['8', '08']:
           print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Webhook Create
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Webhook Spammer
{couleur.LIGHTRED_EX}[03]{couleur.RED} -> Webhook Info
{couleur.LIGHTRED_EX}[04]{couleur.RED} -> Webhook Generator + Chekeur
""")        
           choixWebhook = input(couleur.RED + f"[->] " + couleur.RESET)
           if choixWebhook in ['1', '01']:
              commande = 'python ./Programmes/Programmes/WebhookCreate.py'
              subprocess.run(commande, shell=True)

           if choixWebhook in ['2', '02']:
              commande = 'python ./Programmes/Programmes/WebhookSpammer.py'
              subprocess.run(commande, shell=True)

           if choixWebhook in ['3', '03']:
              commande = 'python ./Programmes/Programmes/WebhookInfo.py'
              subprocess.run(commande, shell=True)

           if choixWebhook in ['4', '04']:
              commande = 'python ./Programmes/Programmes/WebhookGenerator.py'
              subprocess.run(commande, shell=True)
            
           else:
             print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
             time.sleep(3)
             os.system("cls")
             continue
           


        if choix in ['9', '09']:
           print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Token Id
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Token Id Brute
""")        
           choixWebhook = input(couleur.RED + f"[->] " + couleur.RESET)
           if choixWebhook in ['1', '01']:
              commande = 'python ./Programmes/Programmes/TokenId.py'
              subprocess.run(commande, shell=True)

           if choixWebhook in ['2', '02']:
              commande = 'python ./Programmes/Programmes/TokenIdBrute.py'
              subprocess.run(commande, shell=True)
            
           else:
             print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
             time.sleep(3)
             os.system("cls")
             continue
           
        if choix in ['10', '10']:
           print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Invite Bot Id
""")        
           choixWebhook = input(couleur.RED + f"[->] " + couleur.RESET)
           if choixWebhook in ['1', '01']:
              commande = 'python ./Programmes/Programmes/InviteBotId.py'
              subprocess.run(commande, shell=True)
            
           else:
             print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
             time.sleep(3)
             os.system("cls")
             continue
           

            


        
        if choix in ['!', 'username', 'Username', 'nom', 'Nom']:
           nom_utilisateur = input(f"{couleur.RED}\nVeuillez choisir votre Username (mettez rien pour revenir par défault) -> {couleur.RESET}")
           if not nom_utilisateur:
            nom_utilisateur = os.getlogin()
            with open('./Programmes/Programmes/Options/NomUtilisateur.txt', 'w') as fichier:
                fichier.write(f"{nom_utilisateur}'s")
                continue
           else:
              with open('./Programmes/Programmes/Options/NomUtilisateur.txt', 'w') as fichier:
               fichier.write(f"{nom_utilisateur}")
               continue
        
        if choix in ['?', 'theme', 'Theme', 'couleur', 'Couleur']:
            APprint(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> {couleur.MAGENTA}Violet{couleur.RED}
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> {couleur.BLUE}Bleu{couleur.RED}
{couleur.LIGHTRED_EX}[03]{couleur.RED} -> {couleur.GREEN}Vert{couleur.RED}
{couleur.LIGHTRED_EX}[04]{couleur.RED} -> {couleur.YELLOW}Jaune{couleur.RED}
{couleur.LIGHTRED_EX}[05]{couleur.RED} -> {colorama.Fore.RED}Rouge{couleur.RED} (défault)
{couleur.LIGHTRED_EX}[06]{couleur.RED} -> {couleur.WHITE}Blanc{couleur.RED}
""")
            ChoixCouleur = input(f"{couleur.RED}[->] {couleur.RESET}").upper()

            if ChoixCouleur in ['1', '01']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("MAGENTA")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.MAGENTA}Violet{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['2', '02']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("BLUE")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.BLUE}Bleu{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['3', '03']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("GREEN")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.GREEN}Vert{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['4', '04']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("YELLOW")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.YELLOW}Jaune{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['5', '05']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("RED")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {colorama.Fore.RED}Rouge{couleur.RED} (défault).", couleur.RESET)
                time.sleep(3)
                Reset()
             
            if ChoixCouleur in ['6', '06']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("WHITE")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.WHITE}Blanc{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
            
            else:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("RED")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {colorama.Fore.RED}Rouge{couleur.RED} (défault).", couleur.RESET)
                time.sleep(3)
                Reset()

            couleur.RED = getattr(couleur, nouvelle_couleur, couleur.RED)
            couleur.LIGHTRED_EX = getattr(couleur, f"LIGHT{nouvelle_couleur}_EX", couleur.LIGHTRED_EX)

        else:
             print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
             time.sleep(3)
             os.system("cls")
             continue
        
  except:
       print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
       time.sleep(3)
       os.system("cls")
       continue

os.system("pause")