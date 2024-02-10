from Programmes.Options.Options import *

import sys
import subprocess
import os
import time

Title("Menu")

os.system("cls")
print(f"Version {version_tool}")
time.sleep(1)
while True:
   new_color = open('Programmes/Programmes/Options/Theme.txt', 'r').read()
   color.RED = getattr(color, new_color, color.RED)
   color.LIGHTRED_EX = getattr(color, f"LIGHT{new_color}_EX", color.LIGHTRED_EX)

   os.system("cls")

   print(color.RED + f"""     
                                                      
			   ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███   │Grab: {color.LIGHTRED_EX}aucun{color.RED}
			  ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒ │Virus: {color.LIGHTRED_EX}aucun{color.RED}
			  ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒ ├───────────────
			  ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄   │Version: {color.LIGHTRED_EX}{version_tool}{color.RED}
			  ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒ │By: {color.LIGHTRED_EX}{creator}{color.RED}
			  ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ├───────────────
			    ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░ │Username: {color.LIGHTRED_EX}{username_user}{color.RED}
			   ░░   ░    ░    ░ ░  ░      ░       ▒ ░░ ░   ░    ░     ░░   ░   │The checkers are 100% legit!
 			    ░        ░  ░   ░                 ░        ░    ░  ░   ░     

> Change Theme -> {color.LIGHTRED_EX}[?]{color.RED} 
> Change Username -> {color.LIGHTRED_EX}[!]{color.RED}
> Exit -> {color.LIGHTRED_EX}[0]{color.RED}
╔═══                              ═══╗ ╔═══            {color.LIGHTRED_EX}Discord:{color.RED}            ═══╗ ╔═══                                ═══╗
║                                    ║ ║                                      ║ ║                                      ║
    {color.LIGHTRED_EX}[01]{color.RED} -> Info                           {color.LIGHTRED_EX}[08]{color.RED} -> Webhook Catégorie (4)            {color.LIGHTRED_EX}[15]{color.RED} ->           
    {color.LIGHTRED_EX}[02]{color.RED} -> Website (2)                    {color.LIGHTRED_EX}[09]{color.RED} -> Token Catégorie (2)              {color.LIGHTRED_EX}[16]{color.RED} -> 
    {color.LIGHTRED_EX}[03]{color.RED} -> Ip Catégorie (3)               {color.LIGHTRED_EX}[10]{color.RED} -> Invite Catégorie (1)             {color.LIGHTRED_EX}[17]{color.RED} -> 
    {color.LIGHTRED_EX}[04]{color.RED} -> Password Catégorie (1)         {color.LIGHTRED_EX}[11]{color.RED} -> Nitro Catégorie (1)              {color.LIGHTRED_EX}[18]{color.RED} -> 
    {color.LIGHTRED_EX}[05]{color.RED} -> Stealer Catégorie (3)          {color.LIGHTRED_EX}[12]{color.RED} ->                                  {color.LIGHTRED_EX}[19]{color.RED} -> 
    {color.LIGHTRED_EX}[06]{color.RED} ->                                {color.LIGHTRED_EX}[13]{color.RED} ->                                  {color.LIGHTRED_EX}[20]{color.RED} -> 
    {color.LIGHTRED_EX}[07]{color.RED} ->                                {color.LIGHTRED_EX}[14]{color.RED} ->                                  {color.LIGHTRED_EX}[21]{color.RED} -> 
║                                    ║ ║                                      ║ ║                                      ║
╚═══                              ═══╝ ╚═══                                ═══╝ ╚═══                                ═══╝
""")

   try:
        choice = input(color.RED + f"╰┈➤ " + color.RESET)

        if choice in ['0', '00', 'exit', 'Exit']:
            LAPprint(f"\n{color.RED}[!] | Exit." + color.RESET)
            time.sleep(1)
            Exit()

        if choice in ['1', '01', 'info', 'Info']:
            commande = 'python ./Programmes/Programmes/Info.py'
            subprocess.run(commande, shell=True)

        if choice in ['2', '02', 'discord', 'Discord', 'site', 'website']:
            print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> WebSite Red-Tiger
{color.LIGHTRED_EX}[02]{color.RED} -> Server Discord
""")
            choice = input(color.RED + f"[->] " + color.RESET)

            if choice in ['1', '01']:
             commande = 'python ./Programmes/Programmes/Site.py'
             subprocess.run(commande, shell=True)

            if choice in ['2', '02']:
             commande = 'python ./Programmes/Programmes/Discord.py'
             subprocess.run(commande, shell=True)



        if choice in ['3', '03']:
           print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Ip Pinger
{color.LIGHTRED_EX}[02]{color.RED} -> Ip Generator + Checker
{color.LIGHTRED_EX}[03]{color.RED} -> Ip Info
""")        
           choice = input(color.RED + f"[->] " + color.RESET)
           if choice in ['1', '01']:
              commande = 'python ./Programmes/Programmes/IpPinger.py'
              subprocess.run(commande, shell=True)

           if choice in ['2', '02']:
              commande = 'python ./Programmes/Programmes/IpGenerator.py'
              subprocess.run(commande, shell=True)

           if choice in ['3', '03']:
              commande = 'python ./Programmes/Programmes/IpInfo.py'
              subprocess.run(commande, shell=True)
        


        if choice in ['4', '04']:
           print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Password Generator
""")        
           choice = input(color.RED + f"[->] " + color.RESET)
           if choice in ['1', '01']:
              commande = 'python ./Programmes/Programmes/MdpGenerator.py'
              subprocess.run(commande, shell=True)
        


        if choice in ['5', '05']:
           print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Stealer Create (.Exe) (token grab, loc grab, etc..)
{color.LIGHTRED_EX}[02]{color.RED} -> Dox Create
{color.LIGHTRED_EX}[03]{color.RED} -> Web Scraping
""")        
           choice = input(color.RED + f"[->] " + color.RESET)
           if choice in ['1', '01']:
              commande = 'python ./Programmes/Programmes/StealerCreate.py'
              subprocess.run(commande, shell=True)

           if choice in ['2', '02']:
              commande = 'python ./Programmes/Programmes/DoxCreate.py'
              subprocess.run(commande, shell=True)
            
           if choice in ['3', '03']:
              commande = 'python ./Programmes/Programmes/WebScraping.py'
              subprocess.run(commande, shell=True)
           



        if choice in ['8', '08']:
           print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Webhook Create
{color.LIGHTRED_EX}[02]{color.RED} -> Webhook Spammer
{color.LIGHTRED_EX}[03]{color.RED} -> Webhook Info
{color.LIGHTRED_EX}[04]{color.RED} -> Webhook Generator + Checker
""")        
           choice = input(color.RED + f"[->] " + color.RESET)
           if choice in ['1', '01']:
              commande = 'python ./Programmes/Programmes/WebhookCreate.py'
              subprocess.run(commande, shell=True)

           if choice in ['2', '02']:
              commande = 'python ./Programmes/Programmes/WebhookSpammer.py'
              subprocess.run(commande, shell=True)

           if choice in ['3', '03']:
              commande = 'python ./Programmes/Programmes/WebhookInfo.py'
              subprocess.run(commande, shell=True)

           if choice in ['4', '04']:
              commande = 'python ./Programmes/Programmes/WebhookGenerator.py'
              subprocess.run(commande, shell=True)
           


        if choice in ['9', '09']:
           print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Token Id
{color.LIGHTRED_EX}[02]{color.RED} -> Token Id Brute + Checker
""")        
           choice = input(color.RED + f"[->] " + color.RESET)
           if choice in ['1', '01']:
              commande = 'python ./Programmes/Programmes/TokenId.py'
              subprocess.run(commande, shell=True)

           if choice in ['2', '02']:
              commande = 'python ./Programmes/Programmes/TokenIdBrute.py'
              subprocess.run(commande, shell=True)

           
        if choice in ['10', '10']:
           print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Invite Bot Id
""")        
           choice = input(color.RED + f"[->] " + color.RESET)
           if choice in ['1', '01']:
              commande = 'python ./Programmes/Programmes/InviteBotId.py'
              subprocess.run(commande, shell=True)

         
        if choice in ['11', '11']:
           print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Nitro Générator + Checker
""")        
           choice = input(color.RED + f"[->] " + color.RESET)
           if choice in ['1', '01']:
              commande = 'python ./Programmes/Programmes/NitroGenerator.py'
              subprocess.run(commande, shell=True)
           

            


        
        if choice in ['!', 'username', 'Username', 'nom', 'Nom']:
           username_user = input(f"{color.RED}\n[?] | Username -> {color.RESET}")
           if not username_user:
            username_user = os.getlogin()
            with open('./Programmes/Programmes/Options/NomUtilisateur.txt', 'w') as fichier:
                fichier.write(f"{username_user}'s")
                continue
           else:
              with open('./Programmes/Programmes/Options/NomUtilisateur.txt', 'w') as fichier:
               fichier.write(f"{username_user}")
               continue
        
        if choice in ['?', 'theme', 'Theme', 'couleur', 'Couleur']:
            APprint(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> {color.MAGENTA}Magenta{color.RED}
{color.LIGHTRED_EX}[02]{color.RED} -> {color.BLUE}Blue{color.RED}
{color.LIGHTRED_EX}[03]{color.RED} -> {color.GREEN}Green{color.RED}
{color.LIGHTRED_EX}[04]{color.RED} -> {color.YELLOW}Yellow{color.RED}
{color.LIGHTRED_EX}[05]{color.RED} -> {colorama.Fore.RED}Red{color.RED} (défault)
{color.LIGHTRED_EX}[06]{color.RED} -> {color.WHITE}White{color.RED}
""")
            ChoixCouleur = input(f"{color.RED}[->] {color.RESET}").upper()

            if ChoixCouleur in ['1', '01']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("MAGENTA")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                new_color = fichier.read()
                print(f"\n{color.RED}[!] | Theme: {color.MAGENTA}{new_color}{color.RED}.", color.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['2', '02']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("BLUE")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                new_color = fichier.read()
                print(f"\n{color.RED}[!] | Theme: {color.BLUE}{new_color}{color.RED}.", color.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['3', '03']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("GREEN")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                new_color = fichier.read()
                print(f"\n{color.RED}[!] | Theme: {color.GREEN}{new_color}{color.RED}.", color.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['4', '04']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("YELLOW")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                new_color = fichier.read()
                print(f"\n{color.RED}[!] | Theme: {color.YELLOW}{new_color}{color.RED}.", color.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['5', '05']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("RED")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                new_color = fichier.read()
                print(f"\n{color.RED}[!] | Theme: {color.RED}{new_color}{color.RED}.", color.RESET)
                time.sleep(3)
                Reset()
             
            if ChoixCouleur in ['6', '06']:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("WHITE")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                new_color = fichier.read()
                print(f"\n{color.RED}[!] | Theme: {color.WHITE}{new_color}{color.RED}.", color.RESET)
                time.sleep(3)
                continue

            else:
             with open('./Programmes/Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("RED")
             with open('./Programmes/Programmes/Options/Theme.txt', 'r') as fichier:
                new_color = fichier.read()
                print(f"\n{color.RED}[!] | Theme: {color.RED}{new_color}{color.RED}.", color.RESET)
                time.sleep(3)
                Reset()

            color.RED = getattr(color, new_color, color.RED)
            color.LIGHTRED_EX = getattr(color, f"LIGHT{new_color}_EX", color.LIGHTRED_EX)
        
   except:
       ErrorChoice()