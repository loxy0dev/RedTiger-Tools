try:
 from Program.Config.Config import *
 from Program.Config.Util import *
 import requests
 import re
 import webbrowser

 Clear()
 Title("Menu")

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


 page1 = f"""{color.WHITE}[{color.RED}Page n°1{color.WHITE}]
   {color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Tool Info                      {color.WHITE}[{color.RED}11{color.WHITE}] {color.RED}->{color.WHITE} Discord Webhook Generator      {color.WHITE}[{color.RED}21{color.WHITE}] {color.RED}->{color.WHITE} Discord Mass Dm
   {color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Web Site                       {color.WHITE}[{color.RED}12{color.WHITE}] {color.RED}->{color.WHITE} Discord Webhook Create         {color.WHITE}[{color.RED}22{color.WHITE}] {color.RED}->{color.WHITE} Discord Server Info
   {color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Ip Info                        {color.WHITE}[{color.RED}13{color.WHITE}] {color.RED}->{color.WHITE} Discord Nitro Generator        {color.WHITE}[{color.RED}23{color.WHITE}] {color.RED}->{color.WHITE} Discord Raid Server (soon)
   {color.WHITE}[{color.RED}04{color.WHITE}] {color.RED}->{color.WHITE} Ip Pinger                      {color.WHITE}[{color.RED}14{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Generator        {color.WHITE}[{color.RED}24{color.WHITE}] {color.RED}->{color.WHITE} Discord Status Changer
   {color.WHITE}[{color.RED}05{color.WHITE}] {color.RED}->{color.WHITE} Ip Generator                   {color.WHITE}[{color.RED}15{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Info             {color.WHITE}[{color.RED}25{color.WHITE}] {color.RED}->{color.WHITE} Discord Language Changer
   {color.WHITE}[{color.RED}06{color.WHITE}] {color.RED}->{color.WHITE} Number Info                    {color.WHITE}[{color.RED}16{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Nuker            {color.WHITE}[{color.RED}26{color.WHITE}] {color.RED}->{color.WHITE} Discord Theme Changer
   {color.WHITE}[{color.RED}07{color.WHITE}] {color.RED}->{color.WHITE} Dox Create                     {color.WHITE}[{color.RED}17{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Joiner           {color.WHITE}[{color.RED}27{color.WHITE}] {color.RED}->{color.WHITE} Discord House Changer
   {color.WHITE}[{color.RED}08{color.WHITE}] {color.RED}->{color.LIGHTYELLOW_EX} Builder Grab/Stealer           {color.WHITE}[{color.RED}18{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Leaver (soon)    {color.WHITE}[{color.RED}28{color.WHITE}] {color.RED}->{color.WHITE} Discord Bot Invite To Id
   {color.WHITE}[{color.RED}09{color.WHITE}] {color.RED}->{color.WHITE} Discord Webhook Info           {color.WHITE}[{color.RED}19{color.WHITE}] {color.RED}->{color.WHITE} Discord Token Login            {color.WHITE}[{color.RED}29{color.WHITE}] {color.RED}->{color.WHITE} Discord Bot Server Nuker (soon)
   {color.WHITE}[{color.RED}10{color.WHITE}] {color.RED}->{color.WHITE} Discord Webhook Spammer        {color.WHITE}[{color.RED}20{color.WHITE}] {color.RED}->{color.WHITE} Discord Token To Id            {color.WHITE}[{color.RED}30{color.WHITE}] {color.RED}-> Next Page ▶"""
 page2 = f"""{color.WHITE}[{color.RED}Page n°2{color.WHITE}]
   {color.WHITE}[{color.RED}31{color.WHITE}] {color.RED}-> ◀ Previous Page                {color.WHITE}[{color.RED}41{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}61{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}32{color.WHITE}] {color.RED}->{color.WHITE} Roblox Cookie Login            {color.WHITE}[{color.RED}42{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}62{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}33{color.WHITE}] {color.RED}->{color.WHITE} Roblox Cookie Info             {color.WHITE}[{color.RED}43{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}63{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}34{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}44{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}64{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}35{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}45{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}65{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}36{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}46{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}66{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}37{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}47{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}67{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}38{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}48{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}68{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}39{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}49{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}69{color.WHITE}] {color.RED}->{color.WHITE} 
   {color.WHITE}[{color.RED}40{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}50{color.WHITE}] {color.RED}->{color.WHITE}                                {color.WHITE}[{color.RED}60{color.WHITE}] {color.RED}-> Next Page ▶"""
 
 with open("Settings/Program/Config/Page.txt", "r") as file:
  page = file.read()
 if page in ["1"]:
    page = page1
    Title("Menu - Page n°1")
 elif page in ["2"]:
    page = page2
    Title("Menu - Page n°2")
 else:
    page = page1
    Title("Menu - Page n°1")

 while True:
   import shutil
   Clear()
   print(color.RED + f"""{popup_version}                                                                                                   
                             ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███
                            ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                            ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                            ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄
                            ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                            ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                              ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
                             ░░   ░    ░    ░ ░  ░      ░       ▒ ░░ ░   ░    ░     ░░   ░
                              ░        ░  ░   ░                 ░        ░    ░  ░   ░      {color.WHITE}
                                             
                                             {color.WHITE}{github_tool}    
                                 -------------------------------------------------------    
                                 {color.WHITE}| {color.RED}Hacking Tool{color.WHITE} | {color.RED}Ip Tool{color.WHITE} | {color.RED}Discord Tool{color.WHITE} | {color.RED}Roblox Tool{color.WHITE} |
                                 -------------------------------------------------------
   
   {page}
""")

   choice = input(f"{color.RED}-> {color.RESET}")

   if choice in ['1', '01']:
      StartProgram("ToolInfo.py")

   elif choice in ['2', '02']:
      StartProgram("WebSite.py")

   elif choice in ['3', '03']:
      StartProgram("IpInfo.py")

   elif choice in ['4', '04']:
      StartProgram("IpPinger.py")

   elif choice in ['5', '05']:
      StartProgram("IpGenerator.py")

   elif choice in ['6', '06']:
      StartProgram("NumberInfo.py")

   elif choice in ['7', '07']:
      StartProgram("DoxCreate.py")

   elif choice in ['8', '08']:
      StartProgram("BuilderGrab.py")

   elif choice in ['9', '09']:
      StartProgram("DiscordWebhookInfo.py")

   elif choice in ['10']:
      StartProgram("DiscordWebhookSpammer.py")

   elif choice in ['11']:
      StartProgram("DiscordWebhookGenerator.py")

   elif choice in ['12']:
      StartProgram("DiscordWebhookCreate.py")

   elif choice in ['13']:
      StartProgram("DiscordNitroGenerator.py")

   elif choice in ['14']:
      StartProgram("DiscordTokenGenerator.py")

   elif choice in ['15']:
      StartProgram("DiscordTokenInfo.py")

   elif choice in ['16']:
      StartProgram("DiscordTokenNuker.py")

   elif choice in ['17']:
      StartProgram("DiscordTokenJoiner.py")

   elif choice in ['18']:
      StartProgram("DiscordTokenLeaver.py")

   elif choice in ['19']:
      StartProgram("DiscordTokenLogin.py")

   elif choice in ['20']:
      StartProgram("DiscordTokenToId.py")

   elif choice in ['21']:
      StartProgram("DiscordMassDm.py")

   elif choice in ['22']:
      StartProgram("DiscordServerInfo.py")

   elif choice in ['23']:
      StartProgram("DiscordRaidServer.py")

   elif choice in ['24']:
      StartProgram("DiscordStatusChanger.py")

   elif choice in ['25']:
      StartProgram("DiscordLanguageChanger.py")

   elif choice in ['26']:
      StartProgram("DiscordThemeChanger.py")

   elif choice in ['27']:
      StartProgram("DiscordHouseChanger.py")

   elif choice in ['28']:
      StartProgram("DiscordBotInviteToId.py")

   elif choice in ['29']:
      StartProgram("DiscordBotServerNuker.py")


   elif choice in ['30']:
      page = page2
      with open("Settings/Program/Config/Page.txt", "w") as file:
         file.write("2")
         Title("Menu - Page n°2")

   elif choice in ['31']:
      page = page1
      with open("Settings/Program/Config/Page.txt", "w") as file:
         file.write("1")
         Title("Menu - Page n°1")


   elif choice in ['32']:
      StartProgram("RobloxCookieLogin.py")

   elif choice in ['33']:
      StartProgram("RobloxCookieInfo.py")
      

except:
   file = 'python ./Settings/Setup.py'
   subprocess.run(file, shell=True)



   