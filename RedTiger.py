# Copyright (c) RedTiger
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Program.Config.Config import *
from Program.Config.Util import *

try:
   import webbrowser
   import re
   import pyzipper
   from tkinter import messagebox
except Exception as e:
   ErrorModule(e)

option_01 = "Website-Vulnerability-Scanner"
option_02 = "Website-Info-Scanner"
option_03 = "Website-Url-Scanner"
option_04 = "Ip-Scanner"
option_05 = "Ip-Port-Scanner"
option_06 = "Ip-Pinger"
option_07 = "Soon"
option_08 = "Soon"
option_09 = "Soon"

option_10 = "D0x-Create"
option_11 = "D0x-Tracker"
option_12 = "Get-Image-Exif"
option_13 = "Google-Dorking"
option_14 = "Username-Tracker"
option_15 = "Email-Tracker"
option_16 = "Email-Lookup"
option_17 = "Phone-Number-Lookup"
option_18 = "Ip-Lookup"
option_19 = "Instagram-Account"

option_20 = "Phishing-Attack"
option_21 = "Password-Zip-Cracked-Attack"
option_22 = "Password-Hash-Decrypted-Attack"
option_23 = "Password-Hash-Encrypted"
option_24 = "Search-In-DataBase"
option_25 = "Dark-Web-Links"
option_26 = "Ip-Generator"
option_27 = "Soon"
option_28 = "Soon"
option_29 = "Soon"

option_30 = "Virus-Builder"

option_31 = "Python-Obfuscator-(Premium)"
option_32 = "Discord-Rat-(Premium)"
option_33 = "Website-DoS-(Premium)"
option_34 = "Proxy-Scraper-(Premium)"
option_35 = "Soon"
option_36 = "Soon"
option_37 = "Soon"
option_38 = "Soon"
option_39 = "Soon"

option_40 = "Roblox-Cookie-Login"
option_41 = "Roblox-Cookie-Info"
option_42 = "Roblox-Id-Info"
option_43 = "Roblox-User-Info"
option_44 = "Soon"
option_45 = "Soon"
option_46 = "Soon"
option_47 = "Soon"
option_48 = "Soon"
option_49 = "Soon"

option_50 = "Discord-Token-Nuker"
option_51 = "Discord-Token-Info"
option_52 = "Discord-Token-Joiner"
option_53 = "Discord-Token-Leaver"
option_54 = "Discord-Token-Login"
option_55 = "Discord-Token-To-Id-And-Brute"
option_56 = "Discord-Token-Server-Raid"
option_57 = "Discord-Token-Spammer"
option_58 = "Discord-Token-Delete-Friends"
option_59 = "Discord-Token-Block-Friends"
option_60 = "Discord-Token-Mass-Dm"
option_61 = "Discord-Token-Delete-Dm"
option_62 = "Discord-Token-Status-Changer"
option_63 = "Discord-Token-Language-Changer"
option_64 = "Discord-Token-House-Changer"
option_65 = "Discord-Token-Theme-Changer"
option_66 = "Discord-Token-Generator"
option_67 = "Discord-Bot-Server-Nuker"
option_68 = "Discord-Bot-Invite-To-Id"
option_69 = "Discord-Server-Info"
option_70 = "Discord-Nitro-Generator"
option_71 = "Discord-Webhook-Info"
option_72 = "Discord-Webhook-Delete"
option_73 = "Discord-Webhook-Spammer"
option_74 = "Discord-Webhook-Generator"
option_75 = "Soon"
option_76 = "Soon"
option_77 = "Soon"
option_78 = "Soon"
option_79 = "Soon"
option_80 = "Soon"

option_next = "Next"
option_back = "Back"
option_site = "Site"
option_info = "Info"

option_01_txt = f"{red}[{white}01{red}]{white} " + option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = f"{red}[{white}02{red}]{white} " + option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = f"{red}[{white}03{red}]{white} " + option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = f"{red}[{white}04{red}]{white} " + option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = f"{red}[{white}05{red}]{white} " + option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = f"{red}[{white}06{red}]{white} " + option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = f"{red}[{white}07{red}]{white} " + option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = f"{red}[{white}08{red}]{white} " + option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = f"{red}[{white}09{red}]{white} " + option_09.ljust(30)[:30].replace("-", " ")

option_10_txt = f"{red}[{white}10{red}]{white} " + option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = f"{red}[{white}11{red}]{white} " + option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = f"{red}[{white}12{red}]{white} " + option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = f"{red}[{white}13{red}]{white} " + option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = f"{red}[{white}14{red}]{white} " + option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = f"{red}[{white}15{red}]{white} " + option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = f"{red}[{white}16{red}]{white} " + option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = f"{red}[{white}17{red}]{white} " + option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = f"{red}[{white}18{red}]{white} " + option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = f"{red}[{white}19{red}]{white} " + option_19.ljust(30)[:30].replace("-", " ")

option_20_txt = f"{red}[{white}20{red}]{white} " + option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = f"{red}[{white}21{red}]{white} " + option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = f"{red}[{white}22{red}]{white} " + option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = f"{red}[{white}23{red}]{white} " + option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = f"{red}[{white}24{red}]{white} " + option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = f"{red}[{white}25{red}]{white} " + option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = f"{red}[{white}26{red}]{white} " + option_26.ljust(30)[:30].replace("-", " ")
option_27_txt = f"{red}[{white}27{red}]{white} " + option_27.ljust(30)[:30].replace("-", " ")
option_28_txt = f"{red}[{white}28{red}]{white} " + option_28.ljust(30)[:30].replace("-", " ")
option_29_txt = f"{red}[{white}29{red}]{white} " + option_29.ljust(30)[:30].replace("-", " ")

option_30_txt = f"{red}[{white}30{red}]{white} " + option_30.ljust(30)[:30].replace("-", " ")
option_31_txt = f"{red}[{white}31{red}]{white} " + option_31.ljust(30)[:30].replace("-", " ")
option_32_txt = f"{red}[{white}32{red}]{white} " + option_32.ljust(30)[:30].replace("-", " ")
option_33_txt = f"{red}[{white}33{red}]{white} " + option_33.ljust(30)[:30].replace("-", " ")
option_34_txt = f"{red}[{white}34{red}]{white} " + option_34.ljust(30)[:30].replace("-", " ")
option_35_txt = f"{red}[{white}35{red}]{white} " + option_35.ljust(30)[:30].replace("-", " ")
option_36_txt = f"{red}[{white}36{red}]{white} " + option_36.ljust(30)[:30].replace("-", " ")
option_37_txt = f"{red}[{white}37{red}]{white} " + option_37.ljust(30)[:30].replace("-", " ")
option_38_txt = f"{red}[{white}38{red}]{white} " + option_38.ljust(30)[:30].replace("-", " ")
option_39_txt = f"{red}[{white}39{red}]{white} " + option_39.ljust(30)[:30].replace("-", " ")

option_40_txt = f"{red}[{white}40{red}]{white} " + option_40.ljust(30)[:30].replace("-", " ")
option_41_txt = f"{red}[{white}41{red}]{white} " + option_41.ljust(30)[:30].replace("-", " ")
option_42_txt = f"{red}[{white}42{red}]{white} " + option_42.ljust(30)[:30].replace("-", " ")
option_43_txt = f"{red}[{white}43{red}]{white} " + option_43.ljust(30)[:30].replace("-", " ")
option_44_txt = f"{red}[{white}44{red}]{white} " + option_44.ljust(30)[:30].replace("-", " ")
option_45_txt = f"{red}[{white}45{red}]{white} " + option_45.ljust(30)[:30].replace("-", " ")
option_46_txt = f"{red}[{white}46{red}]{white} " + option_46.ljust(30)[:30].replace("-", " ")
option_47_txt = f"{red}[{white}47{red}]{white} " + option_47.ljust(30)[:30].replace("-", " ")
option_48_txt = f"{red}[{white}48{red}]{white} " + option_48.ljust(30)[:30].replace("-", " ")
option_49_txt = f"{red}[{white}49{red}]{white} " + option_49.ljust(30)[:30].replace("-", " ")

option_50_txt = f"{red}[{white}50{red}]{white} " + option_50.ljust(30)[:30].replace("-", " ")
option_51_txt = f"{red}[{white}51{red}]{white} " + option_51.ljust(30)[:30].replace("-", " ")
option_52_txt = f"{red}[{white}52{red}]{white} " + option_52.ljust(30)[:30].replace("-", " ")
option_53_txt = f"{red}[{white}53{red}]{white} " + option_53.ljust(30)[:30].replace("-", " ")
option_54_txt = f"{red}[{white}54{red}]{white} " + option_54.ljust(30)[:30].replace("-", " ")
option_55_txt = f"{red}[{white}55{red}]{white} " + option_55.ljust(30)[:30].replace("-", " ")
option_56_txt = f"{red}[{white}56{red}]{white} " + option_56.ljust(30)[:30].replace("-", " ")
option_57_txt = f"{red}[{white}57{red}]{white} " + option_57.ljust(30)[:30].replace("-", " ")
option_58_txt = f"{red}[{white}58{red}]{white} " + option_58.ljust(30)[:30].replace("-", " ")
option_59_txt = f"{red}[{white}59{red}]{white} " + option_59.ljust(30)[:30].replace("-", " ")

option_60_txt = f"{red}[{white}60{red}]{white} " + option_60.ljust(30)[:30].replace("-", " ")
option_61_txt = f"{red}[{white}61{red}]{white} " + option_61.ljust(30)[:30].replace("-", " ")
option_62_txt = f"{red}[{white}62{red}]{white} " + option_62.ljust(30)[:30].replace("-", " ")
option_63_txt = f"{red}[{white}63{red}]{white} " + option_63.ljust(30)[:30].replace("-", " ")
option_64_txt = f"{red}[{white}64{red}]{white} " + option_64.ljust(30)[:30].replace("-", " ")
option_65_txt = f"{red}[{white}65{red}]{white} " + option_65.ljust(30)[:30].replace("-", " ")
option_66_txt = f"{red}[{white}66{red}]{white} " + option_66.ljust(30)[:30].replace("-", " ")
option_67_txt = f"{red}[{white}67{red}]{white} " + option_67.ljust(30)[:30].replace("-", " ")
option_68_txt = f"{red}[{white}68{red}]{white} " + option_68.ljust(30)[:30].replace("-", " ")
option_69_txt = f"{red}[{white}69{red}]{white} " + option_69.ljust(30)[:30].replace("-", " ")

option_70_txt = f"{red}[{white}70{red}]{white} " + option_70.ljust(30)[:30].replace("-", " ")
option_71_txt = f"{red}[{white}71{red}]{white} " + option_71.ljust(30)[:30].replace("-", " ")
option_72_txt = f"{red}[{white}72{red}]{white} " + option_72.ljust(30)[:30].replace("-", " ")
option_73_txt = f"{red}[{white}73{red}]{white} " + option_73.ljust(30)[:30].replace("-", " ")
option_74_txt = f"{red}[{white}74{red}]{white} " + option_74.ljust(30)[:30].replace("-", " ")
option_75_txt = f"{red}[{white}75{red}]{white} " + option_75.ljust(30)[:30].replace("-", " ")
option_76_txt = f"{red}[{white}76{red}]{white} " + option_76.ljust(30)[:30].replace("-", " ")
option_77_txt = f"{red}[{white}77{red}]{white} " + option_77.ljust(30)[:30].replace("-", " ")
option_78_txt = f"{red}[{white}78{red}]{white} " + option_78.ljust(30)[:30].replace("-", " ")
option_79_txt = f"{red}[{white}79{red}]{white} " + option_79.ljust(30)[:30].replace("-", " ")

option_back_txt = option_back + f" {red}[{white}B{red}]{white}"
option_next_txt = option_next + f" {red}[{white}N{red}]{white}"
option_site_txt = f"{red}[{white}S{red}]{white} " + option_site
option_info_txt =  f"{red}[{white}I{red}]{white} " + option_info

menu1 = f""" ┌─ {option_info_txt}                                                                                               {option_next_txt} ─┐
 ├─ {option_site_txt} ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            │
 └─┬─────────┤ Network Scanner ├─────────┬──────────────┤ Osint ├──────────────┬────────────┤ Utilities ├────────────┴─
   │         └─────────────────┘         │              └───────┘              │            └───────────┘
   ├─ {option_01_txt                    }├─ {option_10_txt                    }├─ {option_20_txt}
   ├─ {option_02_txt                    }├─ {option_11_txt                    }├─ {option_21_txt}
   ├─ {option_03_txt                    }├─ {option_12_txt                    }├─ {option_22_txt}
   ├─ {option_04_txt                    }├─ {option_13_txt                    }├─ {option_23_txt}
   ├─ {option_05_txt                    }├─ {option_14_txt                    }├─ {option_24_txt}
   └─ {option_06_txt                    }├─ {option_15_txt                    }├─ {option_25_txt}
                                         ├─ {option_16_txt                    }└─ {option_26_txt}
                                         ├─ {option_17_txt                    }
                                         ├─ {option_18_txt                    }
                                         └─ {option_19_txt                    }

"""

menu2 = f""" ┌─ {option_info_txt}                                                                                                {option_next_txt} ─┐
 ├─ {option_site_txt}  ┌───────────────┐                         ┌──────┐                              ┌────────┐    {option_back_txt} ─┤
─┴─┬──────────┤ Virus Builder ├──────────┬──────────────┤ Paid ├───────────────┬──────────────┤ Roblox ├──────────────┴─
   │          └───────────────┘          │              └──────┘               │              └────────┘
   └─ {option_30_txt                    }├─ {option_31_txt                    }├─ {option_40_txt}
           ├─ Stealer                    ├─ {option_32_txt                    }├─ {option_41_txt}
           ├─ Grabber                    ├─ {option_33_txt                    }├─ {option_42_txt}
           └─ Malware                    └─ {option_34_txt                    }└─ {option_43_txt}                                    






"""

menu3 = f""" ┌─ {option_info_txt}                                                                                                {option_back_txt} ─┐
 ├─ {option_site_txt}                                           ┌─────────┐                                                    │
─┴─┬───────────────────────────────────────────────────┤ Discord ├────────────────────────────────────────────────────┘
   │                                                   └─────────┘                       
   ├─ {option_50_txt                    }┌─ {option_60_txt                    }┌─ {option_70_txt}
   ├─ {option_51_txt                    }├─ {option_61_txt                    }├─ {option_71_txt}
   ├─ {option_52_txt                    }├─ {option_62_txt                    }├─ {option_72_txt}
   ├─ {option_53_txt                    }├─ {option_63_txt                    }├─ {option_73_txt}
   ├─ {option_54_txt                    }├─ {option_64_txt                    }├─ {option_74_txt}
   ├─ {option_55_txt                    }├─ {option_65_txt                    }│
   ├─ {option_56_txt                    }├─ {option_66_txt                    }│
   ├─ {option_57_txt                    }├─ {option_67_txt                    }│
   ├─ {option_58_txt                    }├─ {option_68_txt                    }│
   ├─ {option_59_txt                    }├─ {option_69_txt                    }│
   └─────────────────────────────────────┴─────────────────────────────────────┘
"""

def Update():
   popup_version = ""
   try:
      new_version = re.search(r'version_tool\s*=\s*"([^"]+)"', requests.get(url_config).text).group(1)
      if new_version != version_tool:
         webbrowser.open(f"https://{github_tool}")
         colorama.init()
         input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Please install the new version of the tool: {white + version_tool + red} -> {white + new_version} ")
         popup_version = f"{red}New Version: {white + version_tool + red} -> {white + new_version}"
         colorama.deinit()
         Clear()
   except: pass

   return popup_version

menu_path = os.path.join(tool_path, "Program", "Config", "Menu.txt")

def Menu():
   popup_version = ""

   try:
      with open(menu_path, "r") as file:
         menu_number = file.read()
      menu_mapping = {"1": menu1, "2": menu2, "3": menu3}
      menu = menu_mapping.get(menu_number, menu1)
   except:
      menu = menu1
      menu_number = "1"

   banner = f"""{popup_version}                                                                                      
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
{menu}"""
   return banner, menu_number

while True:
   try:
      Clear()

      banner, menu_number = Menu()

      Title(f"Menu {menu_number}")
      Slow(MainColor(banner))

      choice = input(MainColor(f""" ┌──({white}{username_pc}@redtiger)─{red}[{white}~/{os_name}/Menu-{menu_number}]
 └─{white}$ {reset}"""))

      if choice in ['N', 'n', 'NEXT', 'Next', 'next']:
         menu_number = {"1": "2", "2": "3", "3": "1"}.get(menu_number, "1")
         with open(menu_path, "w") as file:
            file.write(menu_number)
         continue

      elif choice in ['B', 'b', 'BACK', 'Back', 'back']:
         menu_number = {"2": "1", "3": "2"}.get(menu_number, "1")
         with open(menu_path, "w") as file:
            file.write(menu_number)
         continue

      elif choice in ['I', 'i', 'INFO', 'Info', 'info']:
         StartProgram(f"{option_info}.py")
         continue

      elif choice in ['S', 's', 'SITE', 'Site', 'site']:
         StartProgram(f"{option_site}.py")
         continue
      
      elif choice == '30':
         if os_name == "Linux":
            print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} The builder virus is only compatible with Windows, under Linux it can encounter big problems.")
            messagebox.showinfo(f"RedTiger {version_tool} - Virus Builder", "The builder virus is only compatible with Windows, under Linux it can encounter big problems.")

         print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} It is important to disable your antivirus (Real-time Protection) before building, so that no files are deleted.")
         messagebox.showinfo(f"RedTiger {version_tool} - Virus Builder", "It is important to disable your antivirus (Real-time Protection) before building, so that no files are deleted.")
         try:
            zip_file_path = os.path.join(tool_path, "Program", "FileDetectedByAntivirus", "Password(redtiger).zip")
            file_path = os.path.join(tool_path, "Program", "FileDetectedByAntivirus", "VirusBuilderOptions.py")
            output = os.path.join(tool_path, "Program", "FileDetectedByAntivirus")
            if not os.path.exists(file_path):
               if os.path.exists(zip_file_path):
                  print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Decompression of the encrypted file: {white}Program\\FileDetectedByAntivirus\\Password(redtiger).zip")
                  with pyzipper.AESZipFile(zip_file_path) as zf:
                     zf.pwd = b'redtiger'
                     zf.extractall(output)
                  time.sleep(3)
               else:
                  print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Files are missing, please reinstall the tool.")
         except Exception as e:
            Error(e)

      options = {
         '01': option_01, '02': option_02, '03': option_03, '04': option_04,
         '05': option_05, '06': option_06, '07': option_07, '08': option_08,
         '09': option_09, '10': option_10, '11': option_11, '12': option_12,
         '13': option_13, '14': option_14, '15': option_15, '16': option_16,
         '17': option_17, '18': option_18, '19': option_19, '20': option_20,
         '21': option_21, '22': option_22, '23': option_23, '24': option_24,
         '25': option_25, '26': option_26, '27': option_27, '28': option_28,
         '29': option_29, '30': option_30, '31': option_31, '32': option_32,
         '33': option_33, '34': option_34, '35': option_35, '36': option_36,
         '37': option_37, '38': option_38, '39': option_39, '40': option_40,
         '41': option_41, '42': option_42, '43': option_43, '44': option_44,
         '45': option_45, '46': option_46, '47': option_47, '48': option_48,
         '49': option_49, '50': option_50, '51': option_51, '52': option_52,
         '53': option_53, '54': option_54, '55': option_55, '56': option_56,
         '57': option_57, '58': option_58, '59': option_59, '60': option_60,
         '61': option_61, '62': option_62, '63': option_63, '64': option_64,
         '65': option_65, '66': option_66, '67': option_67, '68': option_68,
         '69': option_69, '70': option_70, '71': option_71, '72': option_72,
         '73': option_73, '74': option_74, '75': option_75, '76': option_76,
         '77': option_77, '78': option_78, '79': option_79
      }

      if choice in options:  
         StartProgram(f"{options[choice]}.py")
      elif '0' + choice in options:
         StartProgram(f"{options['0' + choice]}.py")
      else:
         ErrorChoiceStart()

   except Exception as e:
      Error(e)
