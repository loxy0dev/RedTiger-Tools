# Copyright (c) RedTiger 
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
try:
    import socket
    import ssl
    import subprocess
    import sys
    import requests
    from requests.exceptions import RequestException
    import concurrent.futures
except Exception as e:
    ErrorModule(e)
    
Title("Ip Scanner")

try:
    def IpType(ip):
        ip_type = "Unknown"
        if ':' in ip:
            ip_type = "ipv6"
        elif '.' in ip:
            ip_type = "ipv4"
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} IP Type: {white}{ip_type}{red}")

    def IpPing(ip):
        try:
            ping_cmd = ['ping', '-n', '1', ip] if sys.platform.startswith("win") else ['ping', '-c', '1', '-W', '1', ip]
            result = subprocess.run(ping_cmd, capture_output=True, text=True, timeout=1)
            ping = "Succeed" if result.returncode == 0 else "Fail"
        except Exception:
            ping = "Fail"
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Ping: {white}{ping}{red}")

    def IpPort(ip):
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
            80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
            443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
            1521: "Oracle DB", 3389: "RDP"
        }
        
        def scan_port(ip, port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        protocol = port_protocol_map.get(port, "Unknown")
                        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Port: {white}{port}{red} Status: {white}Open{red} Protocol: {white}{protocol}{red}")
            except Exception:
                pass
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda port: scan_port(ip, port), port_protocol_map.keys())

    def IpDns(ip):
        try:
            dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        except Exception:
            dns = "None"
        if dns != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} DNS: {white}{dns}{red}")

    def IpHostInfo(ip):
        api_url = f"https://ipinfo.io/{ip}/json"
        try:
            response = requests.get(api_url)
            api = response.json()
        except RequestException:
            api = {}

        host_country = api.get('country', 'None')
        if host_country != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host Country: {white}{host_country}{red}")

        host_name = api.get('hostname', 'None')
        if host_name != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host Name: {white}{host_name}{red}")

        host_isp = api.get('org', 'None')
        if host_isp != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host ISP: {white}{host_isp}{red}")

        host_as = api.get('asn', 'None')
        if host_as != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host AS: {white}{host_as}{red}")

    def SslCertificateCheck(ip):
        port = 443
        try:
            with socket.create_connection((ip, port), timeout=1) as sock:
                context = ssl.create_default_context()
                with context.wrap_socket(sock, server_hostname=ip) as ssock:
                    cert = ssock.getpeercert()
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} SSL Certificate: {white}{cert}{red}")
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} SSL Certificate Check Failed: {white}{e}{red}")


    Slow(scan_banner)
    ip = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Ip: {white}{ip}{red}")
    IpType(ip)
    IpPing(ip)
    IpDns(ip)
    IpPort(ip)
    IpHostInfo(ip)
    SslCertificateCheck(ip)
    Continue()
    Reset()

except Exception as e:
    Error(e)
