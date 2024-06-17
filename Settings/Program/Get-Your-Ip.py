"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    from json import *
    import requests
    import socket
    import win32api
except Exception as e:
   ErrorModule(e)
   
Title("Get Your Ip")

try:
    print(f"\n{INFO} Your Ip is not sent to anyone.")
    print(f"{WAIT} Search your Ip..")
    try:
        hostname_pc = socket.gethostname()
    except:
        hostname_pc = "None"

    try:
        username_pc = os.getlogin()
    except:
        username_pc = "None"

    try:
        displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
    except:
        displayname_pc = "None"

    try:
        response = requests.get(f'https://{website}/api/ip/myip')
        ip_address_public = response.json()['ip']
    except:
        ip_address_public = "None"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  

        ip_address_local = s.getsockname()[0]
        s.close()
    except:
        ip_address_local = "None"

    try:
        ip_address_ipv6 = []
        all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
        for interface in all_interfaces:
            if interface[0] == socket.AF_INET6:
                ip_address_ipv6.append(interface[4][0])
        ip_address_ipv6 = ' / '.join(ip_address_ipv6)
    except:
            ip_address_ipv6 = "None"

    print(f"""
    {white}[{red}+{white}]{red} Pc Hostname      : {white}{hostname_pc}{red}
    {white}[{red}+{white}]{red} Pc Username      : {white}{username_pc}{red}
    {white}[{red}+{white}]{red} Pc DisplayName   : {white}{displayname_pc}{red}
    {white}[{red}+{white}]{red} Ip Public [ipv4] : {white}{ip_address_public}{red}
    {white}[{red}+{white}]{red} Ip Local  [ipv4] : {white}{ip_address_local}{red}
    {white}[{red}+{white}]{red} Ipv6             : {white}{ip_address_ipv6}{red}
    """)

    Continue()
    Reset()
except Exception as e:
    Error(e)