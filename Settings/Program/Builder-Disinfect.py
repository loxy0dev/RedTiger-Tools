import os
import sys

def disinfect():
    try:
        def DeleteStartup():
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
        
        try:
            DeleteStartup()
        except:
            pass

        def UnblockSite():

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
        try:
            UnblockSite()
        except:
            pass

    except Exception as e:
        print(e)

disinfect()