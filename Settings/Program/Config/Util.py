from .Config import *

import colorama
import ctypes
import subprocess
import os
import time
import sys
from datetime import datetime

color_webhook = 0xa80505
username_webhook = name_tool
avatar_webhook = "https://media.discordapp.net/attachments/1184160374342299688/1187802357472440441/IMG_1846.png?ex=66102ea6&is=65fdb9a6&hm=220bbc709c52bfc164939b6fb33ae7cc92127ff37554fa1edf9a2339d0f16e98&=&format=webp&quality=lossless&width=353&height=350"

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET

try:
    username_pc = os.getlogin()
except:
    username_pc = "redtiger"

INPUT = f'{red}[{white}>{red}] |'
INFO = f'{red}[{white}!{red}] |'
ERROR = f'{red}[{white}x{red}] |'
ADD = f'{red}[{white}+{red}] |'

GEN_VALID = f'{green}[{white}+{green}] |'
GEN_INVALID = f'{red}[{white}x{red}] |'

def get_current_datetime():
    now = datetime.now()
    return now.hour, now.minute, now.second, now.year, now.day, now.month

def ModuleInstall(module):
    subprocess.check_call(['pip', 'install', module])

def ModuleUninstall(module):
    subprocess.check_call(['pip', 'uninstall', module])

def Title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} | {title}")

def Reset():
    file = f'python ./Settings/Start.py'
    subprocess.run(file, shell=True)

def Clear():
    os.system("cls")

def Exit():
    sys.exit()

def StartProgram(program):
    file = f'python ./Settings/Program/{program}'
    subprocess.run(file, shell=True)

def APprint(texte, delai=0.0000000001):
        for ligne in texte.split('\n'):
          for caractere in ligne:
              print(caractere, end='', flush=True)
              time.sleep(delai)
          print()  
          time.sleep(delai * 0)

def LAPprint(texte, delai=0.03):
        for ligne in texte.split('\n'):
          for caractere in ligne:
              print(caractere, end='', flush=True)
              time.sleep(delai)
          print()  
          time.sleep(delai * 0)
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

def Browser_Private(site, search_bar=True, title="Navigateur Web"):
    class WebBrowserApp(QMainWindow):
        def __init__(self, url=None, width=1000, height=300, search_bar=True, title="Navigateur Web"):
            super().__init__()
            self.setWindowTitle(title)

            self.search_bar = search_bar
            self.url_entry = QLineEdit()
            self.url_entry.returnPressed.connect(self.load_url)
            self.url_entry.setText(url or "") 
            self.url_entry.setVisible(self.search_bar)

            # Créer le QWebEngineView
            self.webview = QWebEngineView()

            layout = QVBoxLayout()
            if self.search_bar:
                layout.addWidget(self.url_entry)
            layout.addWidget(self.webview)

            # Widget central
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            if url:
                self.load_url()  # Charger l'URL lors de l'initialisation
            logo = "./Img/RedTiger_Icon.ico"
            self.setWindowIcon(QIcon(logo))

            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)

        def toggle_search_bar(self, visible):
            self.url_entry.setVisible(visible)

        def load_url(self):
            url = self.url_entry.text()
            if url:
                self.webview.load(QUrl(url))

        def contextMenuEvent(self, event):
            pass  # Désactiver le menu contextuel

    def main():
        app = QApplication(sys.argv)
        app.setStyleSheet("""
            QMainWindow {
                background-color: #1c1c1c;
                color: #ffffff;
            }
            QLineEdit {
                background-color: #333333;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
            }
            QWebEngineView {
                background-color: #1c1c1c;
                color: #ffffff;
                border: none;
            }
        """)
        browser = WebBrowserApp(url=site, width=500, height=10, search_bar=search_bar, title=f"{name_tool} {version_tool} | {title}")  # Utiliser directement le titre
        browser.show()
        sys.exit(app.exec_())

    main()

def Continue():
    input(color.RED + f"{INFO} Press to continue -> " + color.RESET)
    
def ErrorChoice():
    print(f"{color.RED}{ERROR} Invalid Choice !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorId():
    print(f"{color.RED}{ERROR} Invalid ID !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorUrl():
    print(f"{color.RED}{ERROR} Invalid URL !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorEdge():
    print(f"{color.RED}{ERROR}  Edge not installed or driver not up to date !")
    time.sleep(3)
    Reset()

def ErrorToken():
    print(f"{color.RED}{ERROR} Invalid Token !", color.RESET)
    time.sleep(3)
    Reset()
    
def ErrorNumber():
    print(f"{color.RED}{ERROR} Invalid Number !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorWebhook():
    print(f"{color.RED}{ERROR} Invalid Webhook !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorCookie():
    print(f"{color.RED}{ERROR} Invalid Cookie !", color.RESET)
    time.sleep(3)
    Reset()

def ErrorUsername():
    print(f"{color.RED}{ERROR} Invalid Username !", color.RESET)
    time.sleep(3)
    Reset()



world = r""" :...........................-*#%%#-....:-@@@@@@+......................................................................+
 :.......................-@@*@@@%-.*@@@@@@@@@@@@@@*....................................::..............................+
 :..........................*@%...%@@@@@@@@@@@@@@@.......................................:=............................=
 :........................:.:.........@@@@@@@@@@@@.........................:.........:@@@@@@@..........................+
 :..............#:%@@@...+.*%@@@:......%@@@@@@@@@.........................=....+=:=@@@@@@@@@@@@@@@#...+%*:.............=
 :-@@@@@@@@%%@@@@@#--=:.:=@=:%..*@=....:@@@@@@%-..............+@@@@@@......-*@%@@=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@*...+
 =@@@@@@@@@@@@@@##@@@@@@@@@%+...#@*....:@@@*.....:@@.........@@#:@@@.:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+-%.+
 :#@@@@@@@@@@@@@@@%:@@@@@@.....*#........@@................@@@:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=%#@@*.....+
 :...*......=@@@@@@@@@@@@@.....-@@@@...................+....:@..:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-.....=%.........+
 -............@@@@@@@@@@@@@@@#.@@@@@@*................#.%..:%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@+......@..........+
 :.............-@@@@@@@@@@@@@@@@@@#......................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=................+
 :..............@@@@@@@@@@@@::#@@@*:....................=@@@%*%@@@...#@@:.@@%@@@@@@@@@@@@@@@@@@@@@@@@..................+
 :..............@@@@@@@@@@@@@@@@-.....................@@@......+:=#@@%@@*.=@@@@@@@@@@@@@@@@@@@@@*@*....................+
 :...............#@@@@@@@@@@@@@-.......................+=@@@........+@@@@@@@@@@@@@@@@@@@@@@@@@@%..:..-.................+
 :.................+@@@@@#*-=#.......................-@@@@@@@@#@@%%+@@@@@@@@@@@@@@@@@@@@@@@@@@@@.......................+
 :...................+@@=...........................@@@@@@@@@@@@@@@@.@@@@+-=:.:@@@@@@@@@@@@@@@@........................+
 :....................:@@..#.......................+@@@@@@@@@@@@@@@@@.%@@@@:.....@@@=..*@@@............................+
 :..........................#......................=@@@@@@@@@@@@@@@@@@==.........%@......%@@...........................+
 :.............................=@@@@%................@@@@@@@@@@@@@@@@@@@#........................:.....................+
 :.............................@@@@@@@@@....................#@@@@@@@@@@-.................+...#@........................+
 :............................*@@@@@@@@@@@%+................=@@@@@@@@*....................#..-......:##................+
 :.............................@@@@@@@@@@@@@@................*@@@@@@@+..................................:..............+
 :..............................@@@@@@@@@@@@.................@@@@@@@@@..-.........................*@#..-...............+
 :................................@@@@@@@@@=.................#@@@@@@...%-......................-@@@@@@@@%..............+
 :...............................:@@@@@@@....................:@@@@@...........................@@@@@@@@@@@@.............+
 :...............................*@@@@@#......................=@@@............................@@@@@@@@@@@@=............+
 :...............................@@@@#................................................................%@@+.............+
 :..............................:@@#...................................................................................+
 :..............................-@#....................................................................................=
 :..............................+@.....................................................................................+"""