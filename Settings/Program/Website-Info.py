"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
   import socket
except Exception as e:
   ErrorModule(e)
   
Title("Website Info")

try:
    def get_ip_address(domain):
        try:
            ip = socket.gethostbyname(domain)
        except:
            ip = "None"
        return ip

    website = input(f"\n{INPUT} Website Url -> {color.RESET}")
    print(f"{color.RED}{WAIT} Information Recovery..{reset}")

    if "https://" in website or "http://" in website:
        pass
    else:
        website = "https://" + website

    if "https://" in website:
        secure = True
        domain = website.replace("https://", "")
        if domain.find("/") != -1:
            domain = domain[:domain.find("/")]

    elif "http://" in website:
        secure = False
        domain = website.replace("http://", "")
        if domain.find("/") != -1:
            domain = domain[:domain.find("/")]

    else:
        secure = None
        domain = website

    response = requests.get(website)
    status_code = response.status_code

    ip = get_ip_address(domain)

    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    status = data["status"]
    if status in ["fail"]:
        status = "Invalid"
        ip_adress, isp, org, as_number = "None", "None", "None", "None"
    else:
        status = "Valid"
        ip_adress = data["query"]
        isp = data["isp"]
        org = data["org"]
        as_number = data["as"]

    print(f"""
    {white}[{red}+{white}]{red} Website     : {white}{website}{red}
    {white}[{red}+{white}]{red} Domain      : {white}{domain}{red}
    {white}[{red}+{white}]{red} Secure      : {white}{secure}{red}
    {white}[{red}+{white}]{red} Status Code : {white}{status_code}{red}
    {white}[{red}+{white}]{red} Ip          : {white}{ip}{red}
    {white}[{red}+{white}]{red} Ip Status   : {white}{status}{red}
    {white}[{red}+{white}]{red} Host Org    : {white}{org}{red}
    {white}[{red}+{white}]{red} Host As     : {white}{as_number}{red}
    {color.RESET}""")

    Continue()
    Reset()

except Exception as e:
    Error(e)