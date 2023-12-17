from Programmes.Options.Options import *

while True:
  nouvelle_couleur = open('Programmes/Options/Theme.txt', 'r').read()
  couleur.RED = getattr(couleur, nouvelle_couleur, couleur.RED)
  couleur.LIGHTRED_EX = getattr(couleur, f"LIGHT{nouvelle_couleur}_EX", couleur.LIGHTRED_EX)

  TitrePage("Start")

  os.system("cls")

  APprint(couleur.RED + f"""     
                                                      
			   ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███   │Grabb: {couleur.LIGHTRED_EX}aucun{couleur.RED}
			  ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒ │Virus: {couleur.LIGHTRED_EX}aucun{couleur.RED}
			  ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒ ├───────────────
			  ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄   │Version: {couleur.LIGHTRED_EX}{version}{couleur.RED}
			  ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒ │By: {couleur.LIGHTRED_EX}{createur}{couleur.RED}
			  ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ├───────────────
			    ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░ │Username: {couleur.LIGHTRED_EX}{nom_utilisateur}{couleur.RED}
			   ░░   ░    ░    ░ ░  ░      ░       ▒ ░░ ░   ░    ░     ░░   ░   │Webhook: Discord
 			    ░        ░  ░   ░                 ░        ░    ░  ░   ░     

> Change Theme -> {couleur.LIGHTRED_EX}[?]{couleur.RED} 
> Change Username -> {couleur.LIGHTRED_EX}[!]{couleur.RED}    
╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                                 ═══╗
║                                    ║ ║                                     ║ ║                                       ║
    {couleur.LIGHTRED_EX}[00]{couleur.RED} -> Exit                           {couleur.LIGHTRED_EX}[07]{couleur.RED} -> DoxCreate
    {couleur.LIGHTRED_EX}[01]{couleur.RED} -> Info                           {couleur.LIGHTRED_EX}[08]{couleur.RED} -> StealerCreate (.Exe)          
    {couleur.LIGHTRED_EX}[02]{couleur.RED} -> ServeurDiscord (site)          {couleur.LIGHTRED_EX}[09]{couleur.RED} -> WebhookSpammer                         
    {couleur.LIGHTRED_EX}[03]{couleur.RED} -> IpPinger                       {couleur.LIGHTRED_EX}[10]{couleur.RED} -> WebhookCreate                    
    {couleur.LIGHTRED_EX}[04]{couleur.RED} -> IpGenerator + Chekeur          {couleur.LIGHTRED_EX}[11]{couleur.RED} -> WebhookGenerator + Chekeur         
    {couleur.LIGHTRED_EX}[05]{couleur.RED} -> MdpCrack (Travaux)             {couleur.LIGHTRED_EX}[12]{couleur.RED} -> WebhookInfo                
    {couleur.LIGHTRED_EX}[06]{couleur.RED} -> MdpGénérator                   {couleur.LIGHTRED_EX}[13]{couleur.RED} ->
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
            commande = 'python Programmes/Info.py'
            subprocess.run(commande, shell=True)

        if choix in ['2', '02', 'discord', 'Discord']:
            commande = 'python Programmes/Discord.py'
            subprocess.run(commande, shell=True)

        if choix in ['3', '03']:
            commande = 'python Programmes/IpPinger.py'
            subprocess.run(commande, shell=True) 

        if choix in ['4', '04']:
            commande = 'python Programmes/IpGenerator.py'
            subprocess.run(commande, shell=True)

        if choix in ['5', '05']:
            commande = 'python Programmes/MdpCrack.py'
            subprocess.run(commande, shell=True)

        if choix in ['6', '06']:
            commande = 'python Programmes/MdpGenerator.py'
            subprocess.run(commande, shell=True)

        if choix in ['7', '07']:
            commande = 'python Programmes/DoxCreate.py'
            subprocess.run(commande, shell=True)

        if choix in ['8', '08']:
            commande = 'python Programmes/StealerCreate.py'
            subprocess.run(commande, shell=True)

        if choix in ['9', '09']:
            commande = 'python Programmes/WebhookSpammer.py'
            subprocess.run(commande, shell=True)
        
        if choix in ['10', '10']:
            commande = 'python Programmes/WebhookCreate.py'
            subprocess.run(commande, shell=True)
        
        if choix in ['11', '11']:
            commande = 'python Programmes/WebhookGenerator.py'
            subprocess.run(commande, shell=True)
        
        if choix in ['12', '12']:
            commande = 'python Programmes/WebhookInfo.py'
            subprocess.run(commande, shell=True)


        
        if choix in ['!', 'username', 'Username', 'nom', 'Nom']:
           nom_utilisateur = input(f"{couleur.RED}\nVeuillez choisir votre Username (mettez rien pour revenir par défault) -> {couleur.RESET}")
           if not nom_utilisateur:
            nom_utilisateur = os.getlogin()
            with open('Programmes/Options/NomUtilisateur.txt', 'w') as fichier:
                fichier.write(f"{nom_utilisateur}'s")
                continue
           else:
              with open('Programmes/Options/NomUtilisateur.txt', 'w') as fichier:
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
             with open('Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("MAGENTA")
             with open('Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.MAGENTA}Violet{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['2', '02']:
             with open('Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("BLUE")
             with open('Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.BLUE}Bleu{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['3', '03']:
             with open('Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("GREEN")
             with open('Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.GREEN}Vert{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['4', '04']:
             with open('Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("YELLOW")
             with open('Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.YELLOW}Jaune{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
             
            if ChoixCouleur in ['5', '05']:
             with open('Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("RED")
             with open('Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {colorama.Fore.RED}Rouge{couleur.RED} (défault).", couleur.RESET)
                time.sleep(3)
                ResetS()
             
            if ChoixCouleur in ['6', '06']:
             with open('Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("WHITE")
             with open('Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {couleur.WHITE}Blanc{couleur.RED}.", couleur.RESET)
                time.sleep(3)
                continue
            
            else:
             with open('Programmes/Options/Theme.txt', 'w') as fichier:
              fichier.write("RED")
             with open('Programmes/Options/Theme.txt', 'r') as fichier:
                nouvelle_couleur = fichier.read()
                print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le theme a été changé en: {colorama.Fore.RED}Rouge{couleur.RED} (défault).", couleur.RESET)
                time.sleep(3)
                ResetS()

            couleur.RED = getattr(couleur, nouvelle_couleur, couleur.RED)
            couleur.LIGHTRED_EX = getattr(couleur, f"LIGHT{nouvelle_couleur}_EX", couleur.LIGHTRED_EX)

  except:
       LAPprint(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Le choix n'existe pas !", couleur.RESET)
       time.sleep(3)
       os.system("cls")
       continue

os.system("pause")