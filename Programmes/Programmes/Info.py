from Options.Options import *

import os
import time

TitrePage("Info")

LAPprint(f"""\n{couleur.RED}Informations:
{couleur.YELLOW}Username      :  {couleur.CYAN}{nom_utilisateur}
{couleur.YELLOW}Theme         :  {couleur.CYAN}{theme}
{couleur.YELLOW}Name Tool     :  {couleur.CYAN}{nom}
{couleur.YELLOW}Version       :  {couleur.CYAN}{version}
{couleur.YELLOW}Coding        :  {couleur.CYAN}{codage}
{couleur.YELLOW}Language      :  {couleur.CYAN}{language}
{couleur.YELLOW}Virus         :  {couleur.CYAN}None
{couleur.YELLOW}Token Grabb   :  {couleur.CYAN}None
{couleur.YELLOW}By            :  {couleur.CYAN}{createur}
{couleur.YELLOW}Discord [02]  :  {couleur.CYAN}{discord}
{couleur.YELLOW}Site    [02]  :  {couleur.CYAN}{siteweb}
""" + couleur.RESET)

Continue()
Reset()