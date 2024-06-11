from Config.Util import *
from Config.Config import *
try:
   import socket
except Exception as e:
   ErrorModule(e)
   
Title("Website Info")

def get_ip_address(domain):
    try:
        ip = socket.gethostbyname(domain)
    except:
        ip = "None"
    return ip

website = input(f"\n{INPUT} Website Url -> {color.RESET}")
print(f"{color.RED}{WAIT} Information Recovery..{reset}")
if "https://" in website:
    secure = True
    domain = website.replace("https://", "")
elif "http://" in website:
    secure = False
    domain = website.replace("http://", "")
else:
    secure = None
    domain = website

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
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Website : {color.WHITE}{website}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Domain  : {color.WHITE}{domain}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Ip      : {color.WHITE}{ip}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Status  : {color.WHITE}{status}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Secure  : {color.WHITE}{secure}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Isp     : {color.WHITE}{isp}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Org     : {color.WHITE}{org}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} As      : {color.WHITE}{as_number}{color.RED}
{color.RESET}""")

Continue()
Reset()
