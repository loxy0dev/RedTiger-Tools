
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

option_01 = "Tool-Info"
option_02 = "Web-Site"
option_03 = "Ip-Info"
option_04 = "Ip-Pinger"
option_05 = "Ip-Generator"
option_06 = "Dox-Tracker"
option_07 = "Dox-Create"
option_08 = "Number-Info"
option_09 = "Builder-Stealer"
option_10 = "Illegal-Website"
option_11 = "Discord-Webhook-Generator"
option_12 = "Discord-Webhook-Info"
option_13 = "Discord-Webhook-Delete"
option_14 = "Discord-Webhook-Spammer"
option_15 = "Discord-Token-Info"
option_16 = "Discord-Token-Nuker"
option_17 = "Discord-Token-Joiner"
option_18 = "Discord-Token-Leaver-(soon)"
option_19 = "Discord-Token-Login"
option_20 = "Discord-Token-To-Id"
option_21 = "Discord-Token-Generator"
option_22 = "Discord-Server-Info"
option_23 = "Discord-Mass-Dm"
option_24 = "Discord-Status-Changer"
option_25 = "Discord-Language-Changer"
option_26 = "Discord-Theme-Changer"
option_27 = "Discord-House-Changer"
option_28 = "Discord-Bot-Invite-To-Id"
option_29 = "Discord-Bot-Server-Nuker"

option_32 = "Discord-Spam-Message-Channel"
option_33 = "Discord-Nitro-Generator"
option_34 = "Roblox-Cookie-Info"
option_35 = "Roblox-Cookie-Login"
option_36 = ""
option_37 = ""
option_38 = ""
option_39 = ""
option_40 = ""
option_41 = ""
option_42 = ""
option_43 = ""
option_44 = ""
option_45 = ""
option_46 = ""
option_47 = ""
option_48 = ""
option_49 = ""
option_50 = ""
option_61 = ""
option_62 = ""
option_63 = ""
option_64 = ""
option_65 = ""
option_66 = ""
option_67 = ""
option_68 = ""
option_69 = ""
 
option_next = "Next Page ▶"
option_previous = "◀ Previous Page"

option_01_txt = option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = color.LIGHTYELLOW_EX + option_09.ljust(30)[:30].replace("-", " ")
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


page1 = f"""{color.WHITE}[{color.RED}Page n°1{color.WHITE}]
   {color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} {option_01_txt} {color.WHITE}[{color.RED}11{color.WHITE}] {color.RED}->{color.WHITE} {option_11_txt} {color.WHITE}[{color.RED}21{color.WHITE}] {color.RED}->{color.WHITE} {option_21_txt}
   {color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} {option_02_txt} {color.WHITE}[{color.RED}12{color.WHITE}] {color.RED}->{color.WHITE} {option_12_txt} {color.WHITE}[{color.RED}22{color.WHITE}] {color.RED}->{color.WHITE} {option_22_txt}
   {color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} {option_03_txt} {color.WHITE}[{color.RED}13{color.WHITE}] {color.RED}->{color.WHITE} {option_13_txt} {color.WHITE}[{color.RED}23{color.WHITE}] {color.RED}->{color.WHITE} {option_23_txt}
   {color.WHITE}[{color.RED}04{color.WHITE}] {color.RED}->{color.WHITE} {option_04_txt} {color.WHITE}[{color.RED}14{color.WHITE}] {color.RED}->{color.WHITE} {option_14_txt} {color.WHITE}[{color.RED}24{color.WHITE}] {color.RED}->{color.WHITE} {option_24_txt}
   {color.WHITE}[{color.RED}05{color.WHITE}] {color.RED}->{color.WHITE} {option_05_txt} {color.WHITE}[{color.RED}15{color.WHITE}] {color.RED}->{color.WHITE} {option_15_txt} {color.WHITE}[{color.RED}25{color.WHITE}] {color.RED}->{color.WHITE} {option_25_txt}
   {color.WHITE}[{color.RED}06{color.WHITE}] {color.RED}->{color.WHITE} {option_06_txt} {color.WHITE}[{color.RED}16{color.WHITE}] {color.RED}->{color.WHITE} {option_16_txt} {color.WHITE}[{color.RED}26{color.WHITE}] {color.RED}->{color.WHITE} {option_26_txt}
   {color.WHITE}[{color.RED}07{color.WHITE}] {color.RED}->{color.WHITE} {option_07_txt} {color.WHITE}[{color.RED}17{color.WHITE}] {color.RED}->{color.WHITE} {option_17_txt} {color.WHITE}[{color.RED}27{color.WHITE}] {color.RED}->{color.WHITE} {option_27_txt}
   {color.WHITE}[{color.RED}08{color.WHITE}] {color.RED}->{color.WHITE} {option_08_txt} {color.WHITE}[{color.RED}18{color.WHITE}] {color.RED}->{color.WHITE} {option_18_txt} {color.WHITE}[{color.RED}28{color.WHITE}] {color.RED}->{color.WHITE} {option_28_txt}
   {color.WHITE}[{color.RED}09{color.WHITE}] {color.RED}->{color.WHITE} {option_09_txt} {color.WHITE}[{color.RED}19{color.WHITE}] {color.RED}->{color.WHITE} {option_19_txt} {color.WHITE}[{color.RED}29{color.WHITE}] {color.RED}->{color.WHITE} {option_29_txt}
   {color.WHITE}[{color.RED}10{color.WHITE}] {color.RED}->{color.WHITE} {option_10_txt} {color.WHITE}[{color.RED}20{color.WHITE}] {color.RED}->{color.WHITE} {option_20_txt} {color.WHITE}[{color.RED}30{color.WHITE}] {color.RED}-> {option_next_txt}"""

page2 = f"""{color.WHITE}[{color.RED}Page n°2{color.WHITE}]
   {color.WHITE}[{color.RED}31{color.WHITE}] {color.RED}-> {option_previous_txt} {color.WHITE}[{color.RED}41{color.WHITE}] {color.RED}->{color.WHITE} {option_41_txt} {color.WHITE}[{color.RED}61{color.WHITE}] {color.RED}->{color.WHITE} {option_61_txt}
   {color.WHITE}[{color.RED}32{color.WHITE}] {color.RED}->{color.WHITE} {option_32_txt} {color.WHITE}[{color.RED}42{color.WHITE}] {color.RED}->{color.WHITE} {option_42_txt} {color.WHITE}[{color.RED}62{color.WHITE}] {color.RED}->{color.WHITE} {option_62_txt}
   {color.WHITE}[{color.RED}33{color.WHITE}] {color.RED}->{color.WHITE} {option_33_txt} {color.WHITE}[{color.RED}43{color.WHITE}] {color.RED}->{color.WHITE} {option_43_txt} {color.WHITE}[{color.RED}63{color.WHITE}] {color.RED}->{color.WHITE} {option_63_txt}
   {color.WHITE}[{color.RED}34{color.WHITE}] {color.RED}->{color.WHITE} {option_34_txt} {color.WHITE}[{color.RED}44{color.WHITE}] {color.RED}->{color.WHITE} {option_44_txt} {color.WHITE}[{color.RED}64{color.WHITE}] {color.RED}->{color.WHITE} {option_64_txt}
   {color.WHITE}[{color.RED}35{color.WHITE}] {color.RED}->{color.WHITE} {option_35_txt} {color.WHITE}[{color.RED}45{color.WHITE}] {color.RED}->{color.WHITE} {option_45_txt} {color.WHITE}[{color.RED}65{color.WHITE}] {color.RED}->{color.WHITE} {option_65_txt}
   {color.WHITE}[{color.RED}36{color.WHITE}] {color.RED}->{color.WHITE} {option_36_txt} {color.WHITE}[{color.RED}46{color.WHITE}] {color.RED}->{color.WHITE} {option_46_txt} {color.WHITE}[{color.RED}66{color.WHITE}] {color.RED}->{color.WHITE} {option_66_txt}
   {color.WHITE}[{color.RED}37{color.WHITE}] {color.RED}->{color.WHITE} {option_37_txt} {color.WHITE}[{color.RED}47{color.WHITE}] {color.RED}->{color.WHITE} {option_47_txt} {color.WHITE}[{color.RED}67{color.WHITE}] {color.RED}->{color.WHITE} {option_67_txt}
   {color.WHITE}[{color.RED}38{color.WHITE}] {color.RED}->{color.WHITE} {option_38_txt} {color.WHITE}[{color.RED}48{color.WHITE}] {color.RED}->{color.WHITE} {option_48_txt} {color.WHITE}[{color.RED}68{color.WHITE}] {color.RED}->{color.WHITE} {option_68_txt}
   {color.WHITE}[{color.RED}39{color.WHITE}] {color.RED}->{color.WHITE} {option_39_txt} {color.WHITE}[{color.RED}49{color.WHITE}] {color.RED}->{color.WHITE} {option_49_txt} {color.WHITE}[{color.RED}69{color.WHITE}] {color.RED}->{color.WHITE} {option_69_txt}
   {color.WHITE}[{color.RED}40{color.WHITE}] {color.RED}->{color.WHITE} {option_40_txt} {color.WHITE}[{color.RED}50{color.WHITE}] {color.RED}->{color.WHITE} {option_50_txt} {color.WHITE}[{color.RED}60{color.WHITE}] {color.RED}-> {option_next_txt}"""


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
                              ░        ░  ░   ░                 ░        ░    ░  ░   ░      
            
                                           {color.WHITE}{github_tool}    
                                 {color.WHITE}╔══════════════╦═════════╦══════════════╦═════════════╗
                                 {color.WHITE}║ {color.RED}Hacking Tool{color.WHITE} ║ {color.RED}Ip Tool{color.WHITE} ║ {color.RED}Discord Tool{color.WHITE} ║ {color.RED}Roblox Tool{color.WHITE} ║ 
                                 {color.WHITE}╚══════════════╩═════════╩══════════════╩═════════════╝  
   
   {page}
""")

   choice = input(f"{color.RED}-> {color.RESET}")

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
      with open("Settings/Program/Config/Page.txt", "w") as file:
         file.write("2")
         Title("Menu - Page n°2")

   elif choice in ['31']:
      page = page1
      with open("Settings/Program/Config/Page.txt", "w") as file:
         file.write("1")
         Title("Menu - Page n°1")


   elif choice in ['32']:
      StartProgram(f"{option_32}.py")
      
   elif choice in ['33']:
      StartProgram(f"{option_33}.py")
      
   elif choice in ['34']:
      StartProgram(f"{option_34}.py")

   elif choice in ['35']:
      StartProgram(f"{option_35}.py")