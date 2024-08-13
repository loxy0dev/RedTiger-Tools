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
try:
    import requests
    import subprocess
    import socket
    import sys
    import ssl
    import concurrent.futures
    from requests.exceptions import RequestException
except Exception as e:
    ErrorModule(e)
    
Title("Ip Scanner")

try:
    def ip_type(ip):
        if ':' in ip:
            type = "ipv6"
        elif '.' in ip:
            type = "ipv4"
        else:
            type = "Unknown"
            return
        
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} IP Type: {white}{type}{red}")

    def ip_ping(ip):
        try:
            if sys.platform.startswith("win"):
                result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
            else:
                result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
            if result.returncode == 0:
                ping = "Succeed"
            else:
                ping = "Fail"
        except:
            ping = "Fail"

        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Ping: {white}{ping}{red}")

    def ip_port(ip):
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
            80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
            443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
            1521: "Oracle DB", 3389: "RDP"
        }

        port_list = [21, 22, 23, 25, 53, 69, 80, 110, 123, 143, 194, 389, 443, 161, 3306, 5432, 6379, 1521, 3389]

        def scan_port(ip, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    protocol = identify_protocol(ip, port)
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Port: {white}{port}{red} Status: {white}Open{red} Protocol: {white}{protocol}{red}")
                sock.close()
            except:
                pass

        def identify_protocol(ip, port):
            try:
                if port in port_protocol_map:
                    return port_protocol_map[port]
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    sock.connect((ip, port))
                    
                    sock.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode('utf-8'))
                    response = sock.recv(100).decode('utf-8')
                    if "HTTP" in response:
                        return "HTTP"

                    sock.send(b"\r\n")
                    response = sock.recv(100).decode('utf-8')
                    if "FTP" in response:
                        return "FTP"

                    sock.send(b"\r\n")
                    response = sock.recv(100).decode('utf-8')
                    if "SSH" in response:
                        return "SSH"

                    return "Unknown"
            except:
                return "Unknown"

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {executor.submit(scan_port, ip, port): port for port in port_list}
        concurrent.futures.wait(results)

    def ip_dns(ip):
        try:
            dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        except:
            dns = "None"
        if dns != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} DNS: {white}{dns}{red}")

    def ip_host_info(ip):
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

    def ssl_certificate_check(ip):
        port = 443
        try:
            sock = socket.create_connection((ip, port), timeout=1)
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
    ip_type(ip)
    ip_ping(ip)
    ip_dns(ip)
    ip_port(ip)
    ip_host_info(ip)
    ssl_certificate_check(ip)
    Continue()
    Reset()
except Exception as e:
    Error(e)
