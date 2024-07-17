# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from .Config import *
try:
    import colorama
    import ctypes
    import subprocess
    import os
    import time
    import sys
    import datetime
    import sys
    import requests
    import webbrowser
except Exception as e:
    import os
    print(f"[x] | Error Module (Restart Setup.bat): {e}")
    os.system("pause")

color_webhook = 0xa80505
username_webhook = name_tool
avatar_webhook = "https://media.discordapp.net/attachments/1185940734256357427/1252261629546987550/logo_redtiger.png?ex=66719306&is=66704186&hm=c0cdee4699eb76dd404125866c4130d77ed177426daf71d8c976e5bbcb44c6bd&=&format=webp&quality=lossless&width=810&height=810"

color = colorama.Fore
colorama.init()
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW

try:
    username_pc = os.getlogin()
except:
    username_pc = "username"

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

BEFORE = f'{red}[{white}'
AFTER = f'{red}]'

BEFORE_GREEN = f'{green}[{white}'
AFTER_GREEN = f'{green}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'

GEN_VALID = f'{BEFORE_GREEN}+{AFTER_GREEN} |'
GEN_INVALID = f'{BEFORE}x{AFTER} |'

INFO_ADD = f'{white}[{red}+{white}]{red}'

def Censored(text):
    censored = ["loxy", website, creator]
    for censored_text in censored:
        if text in censored:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{white}{text}{red}".')
            Continue()
            Reset()
        elif censored_text in text:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{white}{text}{red}".')
            Continue()
            Reset()
        else:
            pass

def ModuleInstall(module):
    subprocess.check_call(['pip', 'install', module])

def ModuleUninstall(module):
    subprocess.check_call(['pip', 'uninstall', module])

def Title(title):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} | {title}")
    elif sys.platform.startswith("linux"):
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} | {title}\x07")
        
def Clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")

def Reset():
        if sys.platform.startswith("win"):
            file = f'python ./RedTiger.py'
            subprocess.run(file, shell=True)
        elif sys.platform.startswith("linux"):
            file = f'python3 ./RedTiger.py'
            subprocess.run(file, shell=True)

def StartProgram(program):
    if sys.platform.startswith("win"):
        file = f'python ./Settings/Program/{program}'
        subprocess.run(file, shell=True)
    elif sys.platform.startswith("linux"):
        file = f'python3 ./Settings/Program/{program}'
        subprocess.run(file, shell=True)

def Slow(texte):
    delai = 0.03
    lignes = texte.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press to continue -> " + reset)

def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
    Continue()
    Reset()

def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(1)

def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(3)
    Reset()

def ErrorId():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid ID !", reset)
    time.sleep(3)
    Reset()

def ErrorUrl():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid URL !", reset)
    time.sleep(3)
    Reset()

def ErrorResponse():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Response !", reset)
    time.sleep(3)
    Reset()

def ErrorEdge():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Edge not installed or driver not up to date !", reset)
    time.sleep(3)
    Reset()

def ErrorToken():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Token !", reset)
    time.sleep(3)
    Reset()
    
def ErrorNumber():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number !", reset)
    time.sleep(3)
    Reset()

def ErrorWebhook():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Webhook !", reset)
    time.sleep(3)
    Reset()

def ErrorCookie():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Cookie !", reset)
    time.sleep(3)
    Reset()

def ErrorUsername():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Username !", reset)
    time.sleep(3)
    Reset()

def ErrorModule(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error Module (Restart Setup.bat): {white}{e}", reset)
    Continue()
    Reset()

def OnlyWindows():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Windows 10/11 !", reset)
    Continue()
    Reset()

def OnlyLinux():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Linux !", reset)
    Continue()
    Reset()

def CheckWebhook(webhook):
    if webhook.lower().startswith("https://discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("https://canary.discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://canary.discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("https://discordapp.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://discordapp.com/api/webhooks"):
        pass
    else:
        ErrorWebhook()

def ChoiceMultiChannelDiscord():
    try:
        num_channels = int(input(f"{INPUT} How many spam channels -> {reset}"))
    except ValueError:
        ErrorNumber()
    
    selected_channels = [] 
    number = 0
    for _ in range(num_channels):
        try:
            number += 1
            selected_channel_number = input(f"{color.RED}{INPUT} Channel Id {number}/{num_channels} -> {color.RESET}")
            selected_channels.append(selected_channel_number)
        except:
            ErrorId()

    return selected_channels


def ChoiceMultiTokenDisord():

    def CheckToken(token_number, token):
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            status = f"Valid"
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(f"{white}[{red}{token_number}{white}]{red} -> {red}Status: {white}{status}{red} | User: {white}{username_discord}{red} | Token: {white}{token_sensur}")
        else:
            status = f"Invalid"
            print(f"{white}[{red}{token_number}{white}]{red} -> {red}Status: {white}{status}{red} | {red}Token: {white}{token}")

    file_token_discord = "./2-Input/TokenDisc/TokenDisc.txt"
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            token_discord_number += 1
        
        if token_discord_number == 0:
            print(f"{INFO} No Token Discord in file: {white}{file_token_discord}{red} Please add tokens to the file.")
            Continue()
            Reset()
        else:
            print(f"{INFO} {white}{token_discord_number}{red} Token Discord found ({white}{file_token_discord}{red})")
    
    try:
        num_tokens = int(input(f"{INPUT} How many token (max {token_discord_number}) -> {reset}"))
        if num_tokens > token_discord_number:
            ErrorNumber()
    except:
        ErrorNumber()

    token_discord_number = 0
    with open(file_token_discord, 'r') as file_token:
        print()
        print(f"{red}Token Discord ({white}{file_token_discord}{red}):")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    number = 0
    selected_tokens = []
    print()
    for _ in range(num_tokens):
        try:
            number += 1
            selected_token_number = int(input(f"{color.RED}{INPUT} Token Number {number}/{num_tokens} -> {color.RESET}"))
        except:
            ErrorNumber()
        
        selected_token = tokens.get(selected_token_number)
        if selected_token:
            selected_tokens.append(selected_token)
        else:
            ErrorNumber()
    return selected_tokens


def Choice1TokenDiscord():
    def CheckToken(token_number, token):
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            status = f"Valid"
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(f"{white}[{red}{token_number}{white}]{red} -> {red}Status: {white}{status}{red} | User: {white}{username_discord}{red} | Token: {white}{token_sensur}")
        else:
            status = f"Invalid"
            print(f"{white}[{red}{token_number}{white}]{red} -> {red}Status: {white}{status}{red} | {red}Token: {white}{token}")

    file_token_discord = "./2-Input/TokenDisc/TokenDisc.txt"
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        print(f"{red}Token Discord ({white}{file_token_discord}{red}):")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
    
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(f"{INFO} No Token Discord in file: {white}{file_token_discord}{red} Please add tokens to the file.")
        Continue()
        Reset()
        return None

    try:
        selected_token_number = int(input(f"\n{color.RED}{INPUT} Token Number -> {color.RESET}"))
    except:
        ErrorChoice()

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': selected_token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            pass
        else:
            ErrorToken()
    else:
        ErrorChoice()
    return selected_token


def BrowserPrivate(site, search_bar=True, title="Navigateur Web"):
    try:
        from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
        from PyQt5.QtGui import QIcon
        from PyQt5.QtCore import QUrl, Qt
        from PyQt5.QtWebEngineWidgets import QWebEngineView
    except Exception as e:
        ErrorModule(e)

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

url_banner = red + r"""
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                  @@@@                                                    @@@@                     @@@@
                  @@@@                                                    @@@@       @@@@@          @@@
                  @@@@   @@@@ @@@@  @@@@@@@@  @@@   @@@ @@@@  @@@  @@@@   @@@@    @@@@@@@@@@@       @@@
                  @@@@   @@@@ @@@@  @@@ @@@@@ @@@@ @@@@ @@@@ @@@@  @@@@   @@@@  @@@@@@   @@@@@      @@@
                  @@@@   @@@@ @@@@@@@@@  @@@@@@@@@@@@@@ @@@@@@@@@@@@@@    @@@@  @@@@       @@@@     @@@
                  @@@@    @@@@@@@@@@@@@   @@@@@@@@@@@@   @@@@@@@@@@@@@    @@@@  @@@@       @@@@     @@@
                  @@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@     @@@@  @@@@@     @@@@@     @@@
                  @@@@    @@@@@@@@@@@@    @@@@@@@@@@@     @@@@@@@@@@@     @@@@   @@@@@@@@@@@@@      @@@
                  @@@@     @@@@@@@@@@@    @@@@@@@@@@@     @@@@@ @@@@@     @@@@     @@@@@@@@@@@@@    @@@
                  @@@@     @@@@@ @@@@      @@@@ @@@@@     @@@@@ @@@@      @@@@               @@@@@  @@@
                  @@@@      @@@   @@        @@   @@@       @@@   @@       @@@@                 @@@  @@@
                  @@@@                                                    @@@@                     @@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
"""

phishing_banner = red + r"""
                                                         .+#%@@%#+.                                     
                                                    .#@@@@@@@@@@@@@@@@#.                                
                                                  +@@@@@@@@@@@@@@@@@@@@@@*                              
                                                .%@@@@@@@@@@@@@@@@@@@@@@@@%.                            
                                                %@@@@@@@@@@@@@@@@@@@@@@@@@@%                            

                                               %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                          
                                                -..........................-.                           
                                                %@@@@@@%%@@@@@@@@@@@%@@@@@@%                            
                                                %@@@#     .%@@@@%.     *@@@%                            
                                                . :+%%+--+%@#::#@%*--+%%+: .                            
                                                                           .                            
                                                 :                        :                             
                                                  -                      =                              
                                                    -                  -                                
                                                       -=          --                                   
                                               -+#%@@@@@@=        =@@@@@@%#+-                           
                                            *@@@@@@@@@@@@=        =@@@@@@@@@@@@*                        
                                          *@@@@@@@@@@@@@@+        +@@@@@@@@@@@@@@#                      
                                         *@@@@@@@@@@@@@@@@%=    -%@@@@@@@@@@@@@@@@#                     
                                        -@@@@@@@@@@@@@@@@@@@%#*%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-  """

decrypted_banner = red + r"""
                                         ^M@@@@@@@@@v                                    
                                      v@@@@@@@@@@@@@@@@@                                 
                                    _@@@@@@@}    ;a@@@@@@@                               
                                   M@@@@@            @@@@@@                              
                                  ;@@@@@              O@@@@@                             
                                  @@@@@v               @@@@@                             
                                  @@@@@;               @@@@@                             
                                  @@@@@;                                                 
                                  @@@@@;        v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@j     @@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@v       @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@_   @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|      
                                               ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O  """


encrypted_banner = red + r"""
                                                       j@@@@@^                                 
                           _@v   p@@@@j           j@@@@@@@@@@@@@@@;          |@@@@M   v@}      
                          @@@@@} >@@@@    v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@p    @@@@_ _@@@@@     
                          >@@@v    @@     v@@@@@@@@@@@@      p@@@@@@@@@@@a     @@    j@@@_     
                           ^@@     @@@@   |@@@@@@@@@@^ @@@@@@; @@@@@@@@@@p   p@@@     M@;      
                           ^@@            >@@@@@@@@@@ p@@@@@@@ M@@@@@@@@@j            M@;      
                           ^@@@@@@@@@@@}   @@@@@@@@|            >@@@@@@@@;   @@@@@@@@@@@;      
                                           }@@@@@@@|    O@@@    >@@@@@@@M                      
                          |@@@@             @@@@@@@|     M@     >@@@@@@@^            @@@@j     
                          @@@@@@@@@@@@@@@>   @@@@@@|    O@@@    >@@@@@@    @@@@@@@@@@@@@@@     
                            ^                 @@@@@v            }@@@@@^                ^       
                                 p@@@@@@@@@^   M@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@p            
                                 p@_            ^@@@@@@@@@@@@@@@@@@>            >@a            
                                @@@@O              @@@@@@@@@@@@@@              J@@@@           
                               ;@@@@@                 J@@@@@@p                 @@@@@>          
                                  ;              p@              p@>  M@@_       ;             
                                          @@@@p  p@_  ;      j_  a@@@@@@@@j                    
                                         ^@@@@@@@@@   v@_   O@}       M@@_                     
                                            ;         p@|   O@}      }}                        
                                                    >@@@@@  O@@@@@@@@@@@J                      
                                                     p@@@j         ;@@@@^                      """



scan_bannner = red + r"""
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                   >|a@@@@@@@@@|                                                
                                              }@@@@@@@@@@@@@@@@| 000M|                                          
                                          ;@@@@@@O  @@@@@@@@@@@|  j000000_                                      
                                       }@@@@@v   |@@@@@@@@@@@@@| 00J  |00000j                                   
                                     @@@@@_     @@@@@@@@@@@@@@@| 0000    ;00000^                                
                                  ;@@@@v       _@@@@@@@     >@@| 0000v      }0000_                              
                                ^@@@@_         @@@@@@@      ^O@| 00000        ;0000_                            
                                 @@@@;         @@@@@@@      ;p@| 00000         0000^                            
                                   @@@@p       >@@@@@@@^    >@@| 0000v      J0000;                              
                                     O@@@@|     M@@@@@@@@@@@@@@| 0000    >00000                                 
                                       ;@@@@@J^  }@@@@@@@@@@@@@| 00v  j00000}                                   
                                          >@@@@@@@_;@@@@@@@@@@@| ;M000000_                                      
                                              >@@@@@@@@@@@@@@@@| 00000}                                          
                                                   ^jpM@@@@@@@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@| 
"""



sql_banner = red + r"""
                                                                                   ^                      
                                                                                 J@@M                     
                                                                        ^         @@@@^                   
                                                                     ;@@@>         J@@@                   
                                                                      ;@@@J      ;j j@@@}                 
                                                                       ^@@@O  ^J@@@@^;@@@}                
                                                                   >@@@; @@@@^;@@@@@> ;@@@O               
                                                                >j _@@@@j p@@@^;@|      @@@>              
           _____       _                                      }@@@@  @@@@j J@@@>                          
          / ____|     | |                                 ^a@@ _@@@@;_@@@@a }@@@>                         
         | (___   __ _| |                              ^} v@@@@^;@@@@@@@@@@@ >@@@v                        
          \___ \ / _` | |                            |@@@@ ^@@@@J@@@@@@@@@@@@;^@@@J                       
          ____) | (_| | |                         J@M }@@@@ _@@@@@@@@@@@@@@j    @@j                       
         |_____/ \__, |_|                      ; v@@@@ >@@@@@@@@@@@@@@@@j                                 
                    | |                     ^@@@@ ;@@@@v@@@@@@@@@@@@@j^                                   
                    |_|                     a@@@@@ >@@@@@@@@@@@@@@a                                       
                                            |@@@@@@@@@@@@@@@@@@J                                          
                                          |a ;@@@@@@@@@@@@@@a;                                            
                                         @@@@ ;@@@@@@@@@@@;                                               
                                        |@@@@@> @@@@@@@>                                                  
                                     }@@@pO@MJ   >pp_                                                     
                                  ;@@@a                                                                   
                               ;@@@p;                                                                     
                            >p@@M>                                                                        
                           }@@>                                                                          
"""



map_banner = red + r"""
                                      :**+ :::+*@@.                                                         
                              +: @ = =.  :#@@@@@@@@                 :     .=*@@#     -                      
                 @@@@-. :=: +@@.:% *=@@:   @@@@@@          :#=::     .:@=@@@@@@@@@@@@@@@@@@@@--.-:          
             .#@@@@@@@@@@@@@@@@@@:# .@@   #@@    :@-     +@@:@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*        
             #*   :%@@@@@@@@@@:   .@@#*              ..  ##@ *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:- %=         
                   *@@@@@@@@@@@@%@@@@@@@            = @=+@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+   #.        
                   #@@@@@@@@@##@@@@@= =#              #@@@#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=            
                  @@@@@@@@@@@#+#@@=                 :@@@-.#-*#@.  .@@.=%@@@@%@@@@@@@@@@@@@@@@@=  +          
                 :@@@@@@@@@@@@@@:                   :@@    # - @@@@@@@ =@@@*#*@@@@@@@@@@@@@=.=-  #:         
                  :@@@@@@@@@@@+                     @@@@@@@: :    @@@@@@@@@@@@@@@@@@@@@@@@@@@               
                   #@@@@@    @                     #%@@@@@@@@@@@@@@@@@:@@@@@@@@@@@@#@@@@@@@@@:              
                     @@@     .                    @@@@@@@@@@@@@@@@-%@@@%@#   @@@@@@#=@#@@@@@==              
                     =@@##@   =:*.                @@@@@@*@@@@@@@@@@-=@@@@.    +@@@:  %#@@#=   :             
                         .=@.                     #@@@@@@@@#@@@@@@@@+#:        %@      *%@=                 
                            . @@@@@@               @#@@*@@@@@@@@@@@@@@@=        :-     -       =.           
                             :@@@@@@@#=                   @@@@@@@@@@@@-               :+%  .@=              
                            -@@@@@@@@@@@@                 @+@@@@*+@@#                   @. @@.#   # :       
                             @@@@@@@@@@@@@@@               @@@@@*@@@                     :=.        @@@.    
                              @@@@@@@@@@@@@                #@@@@@@%@.                             :  :      
                               *@@@@@@@@@@%               :@@@@@@@@@ @@.                      .@@@@=:@      
                                :@@@@@@@@@                 #@@@@@@   @:                    .#@@@@@@@@@@     
                                :@@@@%@@                   .@@@@@-   .                     @@@@@@@@@@@@*    
                                :@@@@@@.                    *@@@-                          @@@@#@@@@@@@     
                                .@@@@@                                                           =@@@:    @=
                                 =@@                                                              =    #+   
                                  @%                                                                        
"""



virus_banner = red + r"""
                                                         ...                                       
                                                  +%@@@@@@@@@@@@@*.                                
                                               #@@@@@@@@@@@@@@@@@@@@@:                             
                                             %@@@@@@@@@@@@@@@@@@@@@@@@@:                           
                                           .@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                          
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                                           =@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                          
                                            #@@@%.     .@@@@+      #@@@%                           
                                             +@@=      .@@@@=      .@@#                            
                                              @@@@%%%@@@@%*@@@@%%%@@@@=                            
                                             .@@@@@@@@@@*  -@@@@@@@@@@=                            
                                           .    .::-@@@@@@@@@@@@+::.    .                          
                                         *@@@@#     @@@@@@@@@@@@-    +@@@@@.                       
                                         #@@@@@%    -%@@@@@@@@%=.   *@@@@@@:                       
                                       @@@@@@@@@@@@:            .#@@@@@@@@@@@-                     
                                       +@@@@@*#@@@@@@@@*:  .+@@@@@@@@%*%@@@@#                      
                                                    *@@@@@@@@@@%.                                  
                                        .==.    .+%@@@@@@@%@@@@@@@+:     :=:                       
                                       @@@@@@@@@@@@@@*.       :@@@@@@@@@@@@@@=                     
                                       -@@@@@@@@%=                :#@@@@@@@@*                      
                                         *@@@@@:                     %@@@@@:                       
                                         :%@@%.                       *@@@=                       
"""



logo_banner = red + r"""
                                         █████████████████████████████████████                                        
                                   ██████                  █                  ██████                                   
                               ██████                                             ██████                               
               ███████████████████                         █                         ███████████████████               
         █████           █████                      ██  ███ ███  ██                      █████           █████         
        ████           █████      ██   ██████       ████       ████       ██████   ██      █████           ████        
        ███           ████     ███   ███     ██████████         ██████████      ██   ███     ████           ███        
        ████         ████      ███             ████████         ████████             ███      ████         ████        
         ████      ██████      ████ ██████████  ████               ████  ███████████████      ██████      ████         
          ██████  █████              ██  ████ ██                       ██ ████  ██              █████  ██████         
            ███████████         ███   ██      ███████████     ███████████      ██   ███         ███████████     
              ██████████    ███ █████                                             █████ ███    ██████████  
                 ██████    ███     ██████        ███                ██        ██████     ███    ██████                 
                ███       ████                   ████     ███     ████                   ████       ████               
              ████        ████    ██             ██                 ██             ██    ████         ███              
             █████          ███████            ██████ ███████████ ██████            ███████          █████             
              ██     █      ███████              ███               ███              ███████      █     ██              
            ███     ██      ███████                █████       █████                ███████      ██     ███            
           ███      ███      ███████                 ███       ███                 ███████      ███      ███           
          ███       ████     ████████                    ██████                   ████████     █████      ███          
          ███      ████      ██    █████                  ███                  █████    ███     ████      ███          
          ███      ████            █ █████████████████████████████████████████████ █             ███      ███          
          █████     ███        █        ██████    ██  ███  ██  ██  ██    ██████        █         ██     █████          
          █████     █████     ██         █████    ██  ███  ██  ██  ██    █████         ██     ████      █████          
            ███      ████    █████  ██    █████    █████████████████    █████    ██  █████    ████      ███            
             █████    ████     ███████    ██████  ███████████████████  ██████    ███████     ████    █████             
             ██████    █████    ████████   █████████████████████████████████   ████████    █████    ██████             
              ██████    █ ████    █  ████     ███████████████████████████     ████  ██   ████ █    ██████              
                █████        ██      █████    █████ ███████████████ █████    █████      ██        █████                
                  ████        ██     ████     ████   █████████████   ████     ████     ██        ████                  
                   ████  █     █     ████     ███     ███████████     ███     ████     █     █  ████                   
                    ████████            ██    ██      █    █    █      ██    ██            ████████                    
                     █████████      █   ████   █████████████████████████   ████   █      █████████                     
                         ██████    ███  █████          █████████          █████  ███    ██████  █                      
                           ██████ █████████████           ███           █████████████ ██████                           
                            █████████████   ██████                   ██ ███   █████████████                            
                              █████            ███████████████████ █████            █████                              
                               ███              ███████████████████████               ██                               
                                                       █████████                                                       
                                                         █████                                                         
                                                           █                                                           
"""