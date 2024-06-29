# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Settings.Program.Config.Config import *
from Settings.Program.Config.Util import *

try:
   import webbrowser
   import re
   import colorama
except:
   ErrorModule()

colorama.init()

try:
   url = url_config
   response = requests.get(url)
   if response.status_code == 200:
       content = response.text
       match = re.search(r'version_tool\s*=\s*"([^"]+)"', content)
       if match:
           current_version = match.group(1)
           if current_version != version_tool:
               print(f"{INFO} Please download the new version of the tool ! {white}{version_tool}{color.LIGHTYELLOW_EX} -> {white}{current_version}{red}")
               webbrowser.open(github_tool)
               input(f"{INFO} Enter to still use this version -> {color.RESET}")
               popup_version = f"{color.LIGHTYELLOW_EX}Please update the tool: {white}{version_tool}{color.LIGHTYELLOW_EX} -> {white}{current_version}{red}"
           else:
               popup_version = ""
       else:
           popup_version = ""
   else:
       popup_version = ""
except:
   popup_version = ""

option_01 = "Tool-Info"
option_02 = "Tool-Website"
option_03 = "Virus-Build-(Stealer,-Malware)"
option_04 = "Sql-Vulnerability"
option_05 = "Website-Scanner"
option_06 = "Illegal-Website"
option_07 = "Search-In-DataBase"
option_08 = "Dox-Create"
option_09 = "Dox-Tracker-(OSINT)"
option_10 = "Username-Tracker-(OSINT)"
option_11 = "Email-Tracker-(OSINT)"
option_12 = "Email-Info"
option_13 = "Number-Info"
option_14 = "Ip-Info-(Lookup)"
option_15 = "Ip-Port-Scanner"
option_16 = "Ip-Pinger"
option_17 = "Ip-Generator"
option_18 = "Password-Encrypted"
option_19 = "Password-Decrypted"
option_20 = "Get-Your-Ip"
option_21 = "Soon"
option_22 = "Discord-Token-Info"
option_23 = "Discord-Token-Nuker"
option_24 = "Discord-Token-Joiner"
option_25 = "Discord-Token-Leaver"
option_26 = "Discord-Token-Login"
option_27 = "Discord-Token-To-Id-And-Brute"
option_28 = "Discord-Token-Server-Raid"
option_29 = "Discord-Token-Spammer"
option_32 = "Discord-Token-Delete-Friends"
option_33 = "Discord-Token-Block-Friends"
option_34 = "Discord-Token-Mass-Dm"
option_35 = "Discord-Token-Delete-Dm"
option_36 = "Discord-Token-Status-Changer"
option_37 = "Discord-Token-Language-Changer"
option_38 = "Discord-Token-House-Changer"
option_39 = "Discord-Token-Theme-Changer"
option_40 = "Discord-Token-Generator"
option_41 = "Discord-Bot-Server-Nuker"
option_42 = "Discord-Bot-Invite-To-Id"
option_43 = "Discord-Server-Info"
option_44 = "Discord-Nitro-Generator"
option_45 = "Discord-Webhook-Info"
option_46 = "Discord-Webhook-Delete"
option_47 = "Discord-Webhook-Spammer"
option_48 = "Discord-Webhook-Generator"
option_49 = "Roblox-Cookie-Login"
option_50 = "Roblox-Cookie-Info"
option_51 = "Roblox-User-Info"
option_52 = "Roblox-Id-Info"
option_53 = ""
option_54 = ""
option_55 = ""
option_56 = ""
option_57 = ""
option_58 = ""
option_59 = ""
option_60 = ""
option_61 = "" 
option_62 = ""
option_63 = ""
option_64 = ""
option_65 = ""
option_66 = ""
option_67 = ""
option_68 = ""
option_69 = ""

option_next = "Next Page >>"
option_previous = "<< Previous Page"

option_01_txt = option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = option_26.ljust(30)[:30].replace("-", " ")
option_27_txt = option_27.ljust(30)[:30].replace("-", " ")
option_28_txt = option_28.ljust(30)[:30].replace("-", " ")
option_29_txt = option_29.ljust(30)[:30].replace("-", " ")

option_32_txt = option_32.ljust(30)[:30].replace("-", " ")
option_33_txt = option_33.ljust(30)[:30].replace("-", " ")
option_34_txt = option_34.ljust(30)[:30].replace("-", " ")
option_35_txt = option_35.ljust(30)[:30].replace("-", " ")
option_36_txt = option_36.ljust(30)[:30].replace("-", " ")
option_37_txt = option_37.ljust(30)[:30].replace("-", " ")
option_38_txt = option_38.ljust(30)[:30].replace("-", " ")
option_39_txt = option_39.ljust(30)[:30].replace("-", " ")
option_40_txt = option_40.ljust(30)[:30].replace("-", " ")
option_41_txt = option_41.ljust(30)[:30].replace("-", " ")
option_42_txt = option_42.ljust(30)[:30].replace("-", " ")
option_43_txt = option_43.ljust(30)[:30].replace("-", " ")
option_44_txt = option_44.ljust(30)[:30].replace("-", " ")
option_45_txt = option_45.ljust(30)[:30].replace("-", " ")
option_46_txt = option_46.ljust(30)[:30].replace("-", " ")
option_47_txt = option_47.ljust(30)[:30].replace("-", " ")
option_48_txt = option_48.ljust(30)[:30].replace("-", " ")
option_49_txt = option_49.ljust(30)[:30].replace("-", " ")
option_50_txt = option_50.ljust(30)[:30].replace("-", " ")
option_51_txt = option_50.ljust(30)[:30].replace("-", " ")
option_52_txt = option_50.ljust(30)[:30].replace("-", " ")
option_53_txt = option_50.ljust(30)[:30].replace("-", " ")
option_54_txt = option_50.ljust(30)[:30].replace("-", " ")
option_55_txt = option_50.ljust(30)[:30].replace("-", " ")
option_56_txt = option_50.ljust(30)[:30].replace("-", " ")
option_57_txt = option_50.ljust(30)[:30].replace("-", " ")
option_58_txt = option_50.ljust(30)[:30].replace("-", " ")
option_59_txt = option_50.ljust(30)[:30].replace("-", " ")
option_60_txt = option_50.ljust(30)[:30].replace("-", " ")
option_61_txt = option_61.ljust(30)[:30].replace("-", " ")
option_62_txt = option_62.ljust(30)[:30].replace("-", " ")
option_63_txt = option_63.ljust(30)[:30].replace("-", " ")
option_64_txt = option_64.ljust(30)[:30].replace("-", " ")
option_65_txt = option_65.ljust(30)[:30].replace("-", " ")
option_66_txt = option_66.ljust(30)[:30].replace("-", " ")
option_67_txt = option_67.ljust(30)[:30].replace("-", " ")
option_68_txt = option_68.ljust(30)[:30].replace("-", " ")
option_69_txt = option_69.ljust(30)[:30].replace("-", " ")

option_previous_txt = option_previous.ljust(30)[:30]
option_next_txt = option_next.ljust(30)[:30]

page1 = f"""{white}[{red}Page n°1{white}]
   {white}[{red}01{white}] {red}->{white} {option_01_txt} {white}[{red}11{white}] {red}->{white} {option_11_txt} {white}[{red}21{white}] {red}->{white} {option_21_txt}
   {white}[{red}02{white}] {red}->{white} {option_02_txt} {white}[{red}12{white}] {red}->{white} {option_12_txt} {white}[{red}22{white}] {red}->{white} {option_22_txt}
   {white}[{red}03{white}] {red}->{white} {option_03_txt} {white}[{red}13{white}] {red}->{white} {option_13_txt} {white}[{red}23{white}] {red}->{white} {option_23_txt}
   {white}[{red}04{white}] {red}->{white} {option_04_txt} {white}[{red}14{white}] {red}->{white} {option_14_txt} {white}[{red}24{white}] {red}->{white} {option_24_txt}
   {white}[{red}05{white}] {red}->{white} {option_05_txt} {white}[{red}15{white}] {red}->{white} {option_15_txt} {white}[{red}25{white}] {red}->{white} {option_25_txt}
   {white}[{red}06{white}] {red}->{white} {option_06_txt} {white}[{red}16{white}] {red}->{white} {option_16_txt} {white}[{red}26{white}] {red}->{white} {option_26_txt}
   {white}[{red}07{white}] {red}->{white} {option_07_txt} {white}[{red}17{white}] {red}->{white} {option_17_txt} {white}[{red}27{white}] {red}->{white} {option_27_txt}
   {white}[{red}08{white}] {red}->{white} {option_08_txt} {white}[{red}18{white}] {red}->{white} {option_18_txt} {white}[{red}28{white}] {red}->{white} {option_28_txt}
   {white}[{red}09{white}] {red}->{white} {option_09_txt} {white}[{red}19{white}] {red}->{white} {option_19_txt} {white}[{red}29{white}] {red}->{white} {option_29_txt}
   {white}[{red}10{white}] {red}->{white} {option_10_txt} {white}[{red}20{white}] {red}->{white} {option_20_txt} {white}[{red}30{white}] {red}-> {option_next_txt}"""

page2 = f"""{white}[{red}Page n°2{white}]
   {white}[{red}31{white}] {red}-> {option_previous_txt} {white}[{red}41{white}] {red}->{white} {option_41_txt} {white}[{red}61{white}] {red}->{white} {option_61_txt}
   {white}[{red}32{white}] {red}->{white} {option_32_txt} {white}[{red}42{white}] {red}->{white} {option_42_txt} {white}[{red}62{white}] {red}->{white} {option_62_txt}
   {white}[{red}33{white}] {red}->{white} {option_33_txt} {white}[{red}43{white}] {red}->{white} {option_43_txt} {white}[{red}63{white}] {red}->{white} {option_63_txt}
   {white}[{red}34{white}] {red}->{white} {option_34_txt} {white}[{red}44{white}] {red}->{white} {option_44_txt} {white}[{red}64{white}] {red}->{white} {option_64_txt}
   {white}[{red}35{white}] {red}->{white} {option_35_txt} {white}[{red}45{white}] {red}->{white} {option_45_txt} {white}[{red}65{white}] {red}->{white} {option_65_txt}
   {white}[{red}36{white}] {red}->{white} {option_36_txt} {white}[{red}46{white}] {red}->{white} {option_46_txt} {white}[{red}66{white}] {red}->{white} {option_66_txt}
   {white}[{red}37{white}] {red}->{white} {option_37_txt} {white}[{red}47{white}] {red}->{white} {option_47_txt} {white}[{red}67{white}] {red}->{white} {option_67_txt}
   {white}[{red}38{white}] {red}->{white} {option_38_txt} {white}[{red}48{white}] {red}->{white} {option_48_txt} {white}[{red}68{white}] {red}->{white} {option_68_txt}
   {white}[{red}39{white}] {red}->{white} {option_39_txt} {white}[{red}49{white}] {red}->{white} {option_49_txt} {white}[{red}69{white}] {red}->{white} {option_69_txt}
   {white}[{red}40{white}] {red}->{white} {option_40_txt} {white}[{red}50{white}] {red}->{white} {option_50_txt} {white}[{red}60{white}] {red}-> {option_next_txt}"""

def Menu():
   try:
      with open("./Settings/Program/Config/Page.txt", "r") as file:
         page = file.read()
      if page in ["1"]:
         page = page1
         Title("Page 1")
      elif page in ["2"]:
         page = page2
         Title("Page 2")
      else:
         page = page1
         Title("Page 1")
   except:
      page = page1
      Title("Page 1")

   menu = f"""{popup_version}{red}                                                                                                  
                             ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███
                            ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                            ▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                            ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄
                            ░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                            ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                              ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
                             ░░   ░    ░    ░ ░  ░      ░       ▒ ░░ ░   ░    ░     ░░   ░
                              ░        ░  ░   ░                 ░        ░    ░  ░   ░      

                                           {white}{github_tool}
                                                     {white}╔════════════╗
                                                     {white}║ {red}Multi-Tool{white} ║
                                                     {white}╚════════════╝
   {page}
   """
   return menu

Clear()
Slow(Menu())

while True:
   try:
      Clear()
      print(Menu())
      choice = input(f"""{red}┌───({white}{username_pc}@redtiger{red})─[{white}~{red}]
└──{white}$ {reset}""")

      if choice in ['1', '01']:
         StartProgram(f"{option_01}.py")

      elif choice in ['2', '02']:
         StartProgram(f"{option_02}.py")

      elif choice in ['3', '03']:
         StartProgram(f"{option_03}.py")

      elif choice in ['4', '04']:
         StartProgram(f"{option_04}.py")

      elif choice in ['5', '05']:
         StartProgram(f"{option_05}.py")

      elif choice in ['6', '06']:
         StartProgram(f"{option_06}.py")

      elif choice in ['7', '07']:
         StartProgram(f"{option_07}.py")

      elif choice in ['8', '08']:
         StartProgram(f"{option_08}.py")

      elif choice in ['9', '09']:
         StartProgram(f"{option_09}.py")

      elif choice in ['10']:
         StartProgram(f"{option_10}.py")

      elif choice in ['11']:
         StartProgram(f"{option_11}.py")

      elif choice in ['12']:
         StartProgram(f"{option_12}.py")

      elif choice in ['13']:
         StartProgram(f"{option_13}.py")

      elif choice in ['14']:
         StartProgram(f"{option_14}.py")

      elif choice in ['15']:
         StartProgram(f"{option_15}.py")

      elif choice in ['16']:
         StartProgram(f"{option_16}.py")

      elif choice in ['17']:
         StartProgram(f"{option_17}.py")

      elif choice in ['18']:
         StartProgram(f"{option_18}.py")

      elif choice in ['19']:
         StartProgram(f"{option_19}.py")
      
      elif choice in ['20']:
         StartProgram(f"{option_20}.py")
      
      elif choice in ['21']:
         StartProgram(f"{option_21}.py")
      
      elif choice in ['22']:
         StartProgram(f"{option_22}.py")
      
      elif choice in ['23']:
         StartProgram(f"{option_23}.py")
      
      elif choice in ['24']:
         StartProgram(f"{option_24}.py")
      
      elif choice in ['25']:
         StartProgram(f"{option_25}.py")
      
      elif choice in ['26']:
         StartProgram(f"{option_26}.py")
      
      elif choice in ['27']:
         StartProgram(f"{option_27}.py")
      
      elif choice in ['28']:
         StartProgram(f"{option_28}.py")
      
      elif choice in ['29']:
         StartProgram(f"{option_29}.py")
      

      elif choice in ['30']:
         page = page2
         with open("./Settings/Program/Config/Page.txt", "w") as file:
            file.write("2")
            Title("Page 2")

      elif choice in ['31']:
         page = page1
         with open("./Settings/Program/Config/Page.txt", "w") as file:
            file.write("1")
            Title("Page 1")


      elif choice in ['32']:
         StartProgram(f"{option_32}.py")
      
      elif choice in ['33']:
         StartProgram(f"{option_33}.py")
      
      elif choice in ['34']:
         StartProgram(f"{option_34}.py")

      elif choice in ['35']:
         StartProgram(f"{option_35}.py")

      elif choice in ['36']:
         StartProgram(f"{option_36}.py")

      elif choice in ['37']:
         StartProgram(f"{option_37}.py")

      elif choice in ['38']:
         StartProgram(f"{option_38}.py")

      elif choice in ['39']:
         StartProgram(f"{option_39}.py")

      elif choice in ['40']:
         StartProgram(f"{option_40}.py")

      elif choice in ['41']:
         StartProgram(f"{option_41}.py")

      elif choice in ['42']:
         StartProgram(f"{option_42}.py")

      elif choice in ['43']:
         StartProgram(f"{option_43}.py")
   
      elif choice in ['44']:
         StartProgram(f"{option_44}.py")

      elif choice in ['45']:
         StartProgram(f"{option_45}.py")

      elif choice in ['46']:
         StartProgram(f"{option_46}.py")

      elif choice in ['47']:
         StartProgram(f"{option_47}.py")

      elif choice in ['48']:
         StartProgram(f"{option_48}.py")

      elif choice in ['49']:
         StartProgram(f"{option_49}.py")

      elif choice in ['50']:
         StartProgram(f"{option_50}.py")

      elif choice in ['51']:
         StartProgram(f"{option_51}.py")

      elif choice in ['52']:
         StartProgram(f"{option_52}.py")

      elif choice in ['53']:
         StartProgram(f"{option_53}.py")

      elif choice in ['54']:
         StartProgram(f"{option_54}.py")



      else:
         ErrorChoiceStart()
         
   except Exception as e:
      Error(e)