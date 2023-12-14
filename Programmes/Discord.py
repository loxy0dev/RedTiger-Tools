#Module
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os

#Options
from Options.Options import *

TitrePage("Red-Tiger | Serveur Discord (site)")

site = "https://discord.gg/BCS88D9axA"
navigateur = "Edge"

s=Service("./Driver/msedgedriver.exe")
driver = webdriver.Edge(service=s)

print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Démarrage de {couleur.CYAN}\"{navigateur}\"\n" + couleur.RESET)

driver.get(site)

print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Accès au serveur Discord {couleur.CYAN}\"{site}\"\n" + couleur.RESET)

input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
Reset()

os.system("pause")