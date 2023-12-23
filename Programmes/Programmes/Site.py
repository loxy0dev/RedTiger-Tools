from Options.Options import *

import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

import webbrowser

TitrePage("Site Web (site)")

site = siteweb
navigateur = "Edge"
try:
 s=Service("./Driver/msedgedriver.exe")
 driver = webdriver.Edge(service=s)

 print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Démarrage de {couleur.CYAN}\"{navigateur}\"\n" + couleur.RESET)

 driver.get(site)
 
 driver.find_element_by_id("id_du_bouton").click

 print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Accès au site {couleur.CYAN}\"{site}\"\n" + couleur.RESET)
 
except:
 webbrowser.open_new_tab(site)
 print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Accès au site {couleur.CYAN}\"{site}\"\n" + couleur.RESET)

input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
Reset()

os.system("pause")