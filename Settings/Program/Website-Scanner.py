# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
import socket
import requests

Title("Website Scanner")

try:
    def domain_scan(website_url):
        domain = website_url.replace("https://", "").replace("http://", "").split('/')[0]
        return domain
    
    def secure_scan(website_url):
        if website_url.startswith("https://"):
            secure = True
        else:
            secure = False
        return secure

    def status_scan(website_url):
        response = requests.get(website_url)
        status_code = response.status_code
        return status_code

    def ip_scan(domain):
        try:
            ip = socket.gethostbyname(domain)
        except:
            ip = "None"

        try:
            response = requests.get(f"https://{website}/api/ip/ip={ip}")
            api = response.json()
            status = api['status']
            host_isp = api['isp']
            host_org = api['org']
            host_as = api['as']
        except:
            status = "Invalid"
            host_isp = "None"
            host_org = "None"
            host_as = "None"

        return ip, status, host_isp, host_org, host_as
    
    def port_scan(ip):
        open_ports = []
        common_ports = {
            80: "HTTP",
            443: "HTTPS",
            21: "FTP",
            22: "SSH",
            25: "SMTP",
            53: "DNS",
            110: "POP3",
            143: "IMAP",
            3306: "MySQL",
            5432: "PostgreSQL",
            6379: "Redis",
            27017: "MongoDB",
            8080: "HTTP-alt"
        }
        
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append((port, service))
            except Exception as e:
                ErrorModule(e)
            finally:
                sock.close()

        return ' / '.join([f'{port}/{service}' for port, service in open_ports])

    Slow(scan_bannner)
    website_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Website Url -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..{reset}\n")

    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url

    print(f"    {INFO_ADD} Website     : {white}{website_url}{red}")

    domain = domain_scan(website_url)
    print(f"    {INFO_ADD} Domain      : {white}{domain}{red}")

    secure = secure_scan(website_url)
    print(f"    {INFO_ADD} Secure      : {white}{secure}{red}")

    status_code = status_scan(website_url)
    print(f"    {INFO_ADD} Status Code : {white}{status_code}{red}")

    ip, ip_status, host_isp, host_org, host_as = ip_scan(domain)
    print(f"""    {INFO_ADD} Ip          : {white}{ip}{red}
    {INFO_ADD} Ip Status   : {white}{ip_status}{red}
    {INFO_ADD} Host Isp    : {white}{host_isp}{red}
    {INFO_ADD} Host Org    : {white}{host_org}{red}
    {INFO_ADD} Host As     : {white}{host_as}{red}""")

    open_port = port_scan(ip)
    print(f"    {INFO_ADD} Open Ports  : {white}{open_port}{reset}")

    print()
    Continue()
    Reset()

except Exception as e:
    Error(e)