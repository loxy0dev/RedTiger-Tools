from .Config import *

import colorama
import ctypes
import subprocess
import os
import time
import sys
import datetime
import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

color_webhook = 0xa80505
username_webhook = name_tool
avatar_webhook = "https://media.discordapp.net/attachments/1184160374342299688/1223987317908181073/RedTiger_Logo.png?ex=661bda05&is=66096505&hm=c567e0e9e672ae70de44ddf128301ae0a6737d78a2f2a9f46ff9f2b717f0ac04&=&format=webp&quality=lossless&width=810&height=810"

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET

try:
    username_pc = os.getlogin()
except:
    username_pc = "username"

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

INPUT = f'{red}[{white}>{red}] |'
INFO = f'{red}[{white}!{red}] |'
ERROR = f'{red}[{white}x{red}] |'
ADD = f'{red}[{white}+{red}] |'
WAIT = f'{red}[{white}~{red}] |'

GEN_VALID = f'{green}[{white}+{green}] |'
GEN_INVALID = f'{red}[{white}x{red}] |'

def ModuleInstall(module):
    subprocess.check_call(['pip', 'install', module])

def ModuleUninstall(module):
    subprocess.check_call(['pip', 'uninstall', module])

def Title(title):
    try:
        "WINDOWS"
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} | {title}")
    except:
        "LINUX"
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} | {title}\x07")

def Reset():
    try:
        "WINDOWS"
        file = f'python ./Settings/Start.py'
        subprocess.run(file, shell=True)
    except:
        "LINUX"
        file = f'python3 ./Settings/Start.py'
        subprocess.run(file, shell=True)
def Clear():
    try:
        "WINDOWS"
        os.system("cls")
    except:
        "LINUX"
        os.system("clear")

def Exit():
    sys.exit()

def StartProgram(program):
    try:
        "WINDOWS"
        file = f'python ./Settings/Program/{program}'
        subprocess.run(file, shell=True)
    except:
        "LINUX"
        file = f'python3 ./Settings/Program/{program}'
        subprocess.run(file, shell=True)

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

def CheckWebhook(webhook):
    if webhook.lower().startswith("https://discord.com/api/webhooks"):
        pass
    else:
        ErrorWebhook()

def Choice1TokenDiscord():
    def CheckToken(token_number, token):
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            status = f"Valid"
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-10] + '*' * 10
            print(f"{white}[{red}{token_number}{white}]{red} -> {red}Status: {white}{status}{red} | User: {white}{username_discord}{red} | Token: {white}{token_sensur}")
        else:
            status = f"Invalid"
            print(f"{white}[{red}{token_number}{white}]{red} -> {red}Status: {white}{status}{red} | {red}Token: {white}{token}")

    file_token_discord = "./TokenDisc.txt"
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        print(f"{red}Token ({white}{file_token_discord}{red}):")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
    
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(f"{ERROR} No token in file: {white}{file_token_discord}")
        Continue()
        Reset()
        return None

    try:
        selected_token_number = int(input(f"\n{color.RED}{INPUT} Token -> {color.RESET}"))
    except:
        ErrorChoice()

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        pass
    else:
        ErrorChoice()
    return selected_token

def BrowserPrivate(site, search_bar=True, title="Navigateur Web"):
    class WebBrowserApp(QMainWindow):
        def __init__(self, url=None, width=1000, height=300, search_bar=True, title="Navigateur Web"):
            super().__init__()
            self.setWindowTitle(title)

            self.search_bar = search_bar
            self.url_entry = QLineEdit()
            self.url_entry.returnPressed.connect(self.load_url)
            self.url_entry.setText(url or "") 
            self.url_entry.setVisible(self.search_bar)

            self.webview = QWebEngineView()

            layout = QVBoxLayout()
            if self.search_bar:
                layout.addWidget(self.url_entry)
            layout.addWidget(self.webview)

            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            if url:
                self.load_url()
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
            pass 

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