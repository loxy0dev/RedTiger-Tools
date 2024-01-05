from Options.Options import *

import requests
from bs4 import BeautifulSoup

url = input(f"{couleur.RED}\nURL site -> {couleur.RESET}")

print(f"""
{couleur.LIGHTRED_EX}[01]{couleur.RED} -> Html
{couleur.LIGHTRED_EX}[02]{couleur.RED} -> Css (soon)
""")

choix = input(f"{couleur.RED}What do you want to scrap ? -> ")
try:
 if choix in ['1', '01']:
    response = requests.get(url)
    scrap = response.text
    chemin = "./04-Web-Scraping/html.txt"
    with open(chemin, 'w', encoding='utf-8') as fichier:
     fichier.write(scrap)

    print(f"{couleur.RED}\nThe html was sent to \"{couleur.CYAN}{chemin}{couleur.RED}\"")
    time.sleep(3)
    Reset()
 else:
    ErreurChoix()
except:
  ErreurUrl()