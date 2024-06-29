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

import os
import sys
import psutil
import time
import keyboard
import subprocess

def disinfect():
    try:
        def UnblockTaskManager():
            "Perm Admin Required"
            print(f"[!] | Unblock Task Manager.")
            subprocess.run("reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f", shell=True)

        def UnblockKey():
            print(f"[!] | Unblock Key.")
            key = [
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
            for key_block in key:
                try: keyboard.unblock_key(key_block)
                except: pass
            

        def DeleteRestart():
            print(f"[!] | Delete Restart.")
            def EndTask(file):
                for proc in psutil.process_iter():
                    try:
                        if file.lower() in proc.name().lower():
                            proc.terminate()
                    except:
                        pass
            EndTask("ㅤ.exe")
            EndTask("ㅤ.py")

        def DeleteStartup():
            print(f"[!] | Delete Startup.")
            if sys.platform.startswith('win'):  
                folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            elif sys.platform.startswith('darwin'): 
                folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
            elif sys.platform.startswith('linux'):
                folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')

            file = f"{folder}/ㅤ.exe"
            if os.path.exists(file):
                os.remove(file)

            file = f"{folder}/ㅤ.py"
            if os.path.exists(file):
                os.remove(file)

        def UnblockSite():
            "Perm Admin Required"
            print(f"[!] | Unblock Website.")
            def unblock_website(website):
                hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
                redirect = "127.0.0.1"
                with open(hosts_path, "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    for line in lines:
                        if not line.startswith(redirect + " " + website):
                            file.write(line)
                    file.truncate()
            websites_to_block = [
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
            for website in websites_to_block:
                unblock_website(website)

        print(f"[!] | Disinfection RedTiger stealer in progress..")
        time.sleep(1)
        try:
            UnblockTaskManager()
        except:
            pass
        time.sleep(2)
        try:
            UnblockKey()
        except:
            pass
        time.sleep(2)
        try:
            DeleteRestart()
        except:
            pass
        time.sleep(2)
        try:
            DeleteStartup()
        except:
            pass
        time.sleep(2)
        try:
            UnblockSite()
        except:
            pass
        time.sleep(1)
        print(f"[!] | Disinfection finished.")
        time.sleep(3)

    except Exception as e:
        print(e)

disinfect()

#    ╔════════════════════════════════════════════════════════════════════════════╗
#    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
#    ╚════════════════════════════════════════════════════════════════════════════╝
