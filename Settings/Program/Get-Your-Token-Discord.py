
"""
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
    ╚════════════════════════════════════════════════════════════════════════════╝
"""

from Config.Util import *
from Config.Config import *

try:
    import os
    import json
    import requests
    from Crypto.Cipher import AES
    import base64
    import re
    from win32crypt import CryptUnprotectData
except Exception as e:
   ErrorModule(e)

Title("Get Your Token Discord")

if sys.platform.startswith("linux"):
    "LINUX"
    OnlyWindows()
    
def GetYourToken():
    class YourToken:
        def __init__(self):
            upload_tokens().upload()

    class extract_tokens:
        def __init__(self) -> None:
            self.base_url = "https://discord.com/api/v9/users/@me"
            self.appdata = os.getenv("localappdata")
            self.roaming = os.getenv("appdata")
            self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
            self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"

            self.tokens, self.uids = [], []

            self.extract()

        def extract(self) -> None:
            paths = {
                'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
                'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
                'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
                'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
                'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
                'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
                'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
                'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
                'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
                'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
                'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
                'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
                'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
            }

            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                _discord = name.replace(" ", "").lower()
                if "cord" in path:
                    if not os.path.exists(self.roaming+f'\\{_discord}\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.regexp_enc, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
                                                         1]), self.get_master_key(self.roaming+f'\\{_discord}\\Local State'))

                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

            if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

        def validate_token(self, token: str) -> bool:
            r = requests.get(self.base_url, headers={'Authorization': token})

            if r.status_code == 200:
                return True

            return False

        def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return

            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

            return master_key

    class upload_tokens:
        def __init__(self):
            self.tokens = extract_tokens().tokens

        def upload(self):
            number = 0
            if not self.tokens:
                print(f"{INFO} No token found.")

            for token_discord in self.tokens:
                user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()
                username_discord = user['username'] + '#' + user['discriminator']
                user_id_discord = user['id']
                number += 1
                print(f"""{red}
Token n°{number}:
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Token    : {white}{token_discord}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Username : {white}{username_discord}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Id       : {white}{user_id_discord}""")
    YourToken()

print(f"\n{INFO} File detected by the antivirus, but be aware that there is no backdoor!")
print(f"{INFO} Your Token is not sent to anyone.")
print(f"{WAIT} Search your Token..")
GetYourToken()
print()
Continue()
Reset()

"""
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
    ╚════════════════════════════════════════════════════════════════════════════╝
"""