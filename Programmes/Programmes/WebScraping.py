from Options.Options import *

import requests
from bs4 import BeautifulSoup

url = input(f"{color.RED}\n[?] | URL site -> {color.RESET}")

print(f"""
{color.LIGHTRED_EX}[01]{color.RED} -> Html
{color.LIGHTRED_EX}[02]{color.RED} -> Css (soon)
""")

choix = input(f"{color.RED}[?] | What do you want to scrap ? -> ")
try:
 if choix in ['1', '01']:
    response = requests.get(url)
    scrap = response.text
    path = "./03-Web-Scraping/html.txt"
    with open(path, 'w', encoding='utf-8') as fichier:
     fichier.write(scrap)

    print(f"{color.RED}\n[!] | The html was sent to \"{color.CYAN}{path}{color.RED}\"")
    time.sleep(3)
    Reset()
 else:
    ErrorChoice()
except:
  ErrorUrl()