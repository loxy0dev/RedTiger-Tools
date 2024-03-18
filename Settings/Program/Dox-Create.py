from Config.Util import *
from Config.Config import *
import time
import random

Title("Dox Create")

print(color.RED + f"\nVictim information:\n")

by = input(color.RED + "Doxed By: " + color.RESET)
cause = input(color.RED + "Cause: " + color.RESET)

print(color.YELLOW + "\nDiscord:")
username_discord = input(color.RED + "Username: " + color.RESET)
name_discord = input(color.RED + "Display Name: " + color.RESET)
id_discord = input(color.RED + "Id: " + color.RESET)
token_discord = input(color.RED + "Token: " + color.RESET)
email_discord = input(color.RED + "Email: " + color.RESET)
password_discord = input(color.RED + "Password: " + color.RESET)

print(color.YELLOW + "\nPc:")
ip_pc = input(color.RED + "Ip: " + color.RESET)
name_pc = input(color.RED + "Name: " + color.RESET)
os_pc = input(color.RED + "Os: " + color.RESET)
key_pc = input(color.RED + "Windows Key: " + color.RESET)
vpn_pc = input(color.RED + "Vpn Y/N: " + color.RESET)

print(color.YELLOW + "\nPhone:")
number = input(color.RED + "Phone Number: " + color.RESET)
brand = input(color.RED + "Brand: " + color.RESET)
operator = input(color.RED + "Operator: " + color.RESET)

print(color.YELLOW + "\nPersonal:")
last_name = input(color.RED + "Last Name: " + color.RESET)
first_name = input(color.RED + "First Name: " + color.RESET)
age = input(color.RED + "Age:" + color.RESET)

mother = input(color.RED + "Mother: " + color.RESET)
father = input(color.RED + "Father: " + color.RESET)
brother = input(color.RED + "Brother: " + color.RESET)
sister = input(color.RED + "Sister: " + color.RESET)

print(color.YELLOW + "\nLoc:")
continent = input(color.RED + "Continent: " + color.RESET)
country = input(color.RED + "Country: " + color.RESET)
postal_code = input(color.RED + "Postal Code: " + color.RESET)
city = input(color.RED + "City: " + color.RESET)
address = input(color.RED + "Adress: " + color.RESET)

print(color.YELLOW + "\nAccounts")
mail = input(color.RED + "Mail: " + color.RESET)
password = input(color.RED + "Password: " + color.RESET)
other = input(color.RED + "\nOther: " + color.RESET)
print(f"{color.RED}Finished.")

name_file = input(f"{color.RED}\n[?] | Choose the file name -> {color.RESET}")
if not name_file.strip():
    name_file = f'No Name {random.randint(1, 999)}'

path = f"./1-File-Create/D0x - {name_file}.txt"
fichier = open(path, 'w', encoding="utf-8").write

fichier(f"""
 ██████╗   ██████╗  ██╗  ██╗
 ██╔══██╗ ██╔═████╗ ╚██╗██╔╝
 ██║  ██║ ██║██╔██║  ╚███╔╝ 
 ██║  ██║ ████╔╝██║  ██╔██╗ 
 ██████╔╝ ╚██████╔╝ ██╔╝ ██╗ By RedTiger
 ╚═════╝   ╚═════╝  ╚═╝  ╚═╝                                                                                                                              
╔══════════════════════╗
║|[+] Doxed By: {by}   ║
║|[+] Cause: {cause}   ║
╚══════════════════════╝

╓─────────────────────Discord──────────────────────╖
║|[+] Username: {username_discord}
║|[+] Display Name: {name_discord}
║|[+] ID: {id_discord}
║|[+] Token: {token_discord}
║|[+] E-Mail: {email_discord}
║|[+] Password: {password_discord}
╙────────────────────────────────────────────────╜

╓───────────────────────Info──────────────────────╖
║+────────────Pc────────────+
║|[+] IP: {ip_pc}
║|[+] Name: {name_pc}
║|[+] OS: {os_pc}
║|[+] Windows Key: {key_pc}
║|[+] VPN Y/N: {vpn_pc}
║
║+───────────Phone──────────+
║|[+] Phone Number: {number}
║|[+] Brand: {brand}
║|[+] Operator: {operator}
║
║+───────────Personal───────+
║|[+] Last Name: {last_name}
║|[+] First Name: {first_name}
║|[+] Age: {age}
║
║|[+] Mother Y/N: {mother}
║|[+] Father Y/N: {father}
║|[+] Brother Y/N: {brother}
║|[+] Sister Y/N: {sister}
║
║+────────────Loc───────────+
║|[+] Continent: {continent}
║|[+] Country: {country}
║|[+] Postal Code: {postal_code}
║|[+] City: {city}
║|[+] Address: {address}
╙────────────────────────────────────────────────╜

╓─────────────────────Accounts─────────────────────╖
║+───────────Mail───────────+
║|[+] : {mail}
║
║+───────────Passwords──────+
║|[+] : {password}
║
║+───────────Others──────────+
║ {other}
╙────────────────────────────────────────────────╜""")


open(path, 'w').close()

print(color.RED + f"[!] | The DOX {color.CYAN}\"{name_file}\"{color.RED} was sent to: {color.CYAN}\"{path}\""+ color.RESET)
time.sleep(3)
input(color.RED + f"[!] | Press to save -> " + color.RESET)