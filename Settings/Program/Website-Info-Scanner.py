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
    import socket
    import concurrent.futures
    import requests
    from urllib.parse import urlparse
    import ssl
    import urllib3
    from requests.exceptions import RequestException
    import time
    import re
    import dns.resolver
    from bs4 import BeautifulSoup
    import whois
except Exception as e:
    ErrorModule(e)

Title("Website Scanner")

try:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    def website_found_url(url):
        if not urlparse(url).scheme:
            website_url = "https://" + url
        else:
            website_url = url
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Website: {white}{website_url}{red}")
        return website_url

    def website_domain(website_url):
        parsed_url = urlparse(website_url)
        domain = parsed_url.netloc
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Domain: {white}{domain}{red}")
        return domain

    def website_ip(domain):
        try:
            ip = socket.gethostbyname(domain)
        except socket.gaierror:
            ip = "None"

        if ip != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} IP: {white}{ip}{red}")
        return ip

    def ip_type(ip):
        if ':' in ip:
            type = "ipv6" 
        elif '.' in ip:
            type = "ipv4"
        else:
            type = "Unknown"
            return
        
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} IP Type: {white}{type}{red}")

    def website_secure(website_url):
        secure = website_url.startswith("https://")
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Secure: {white}{secure}{red}")

    def website_status(website_url):
        try:
            response = requests.get(website_url, timeout=5)
            status_code = response.status_code
        except RequestException:
            status_code = 404
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status Code: {white}{status_code}{red}")

    def ip_info(ip):
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

        host_isp = api.get('isp', 'None')
        if host_isp != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host Isp: {white}{host_isp}{red}")

        host_org = api.get('org', 'None')
        if host_org != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host Org: {white}{host_org}{red}")

        host_as = api.get('asn', 'None')
        if host_as != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host AS: {white}{host_as}{red}")

    def ip_dns(ip):
        try:
            dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        except:
            dns = "None"
        
        if dns != "None":
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Host DNS: {white}{dns}{red}")

    def website_port(ip):
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

    def http_headers(website_url):
        try:
            response = requests.get(website_url, timeout=5)
            headers = response.headers
            for header, value in headers.items():
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} HTTP Header: {white}{header}{red} Value: {white}{value}{red}")
        except RequestException:
            pass

    def check_ssl_certificate(website_url):
        try:
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=urlparse(website_url).hostname) as sock:
                sock.settimeout(5)
                sock.connect((urlparse(website_url).hostname, 443))
                cert = sock.getpeercert()
            for key, value in cert.items():
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} SSL Certificate Key: {white}{key}{red} Value: {white}{value}{red}")
        except:
            pass

    def check_security_headers(website_url):
        headers_of_interest = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']
        try:
            response = requests.get(website_url, timeout=5)
            headers = response.headers
            for header in headers_of_interest:
                if header in headers:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Security Header: {white}{header}{red} Value: {white}{headers[header]}{red}")
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Missing Security Header: {white}{header}{red}")
        except RequestException:
            pass

    def analyze_cookies(website_url):
        try:
            response = requests.get(website_url, timeout=5)
            cookies = response.cookies
            for cookie in cookies:
                secure = 'Secure' if cookie.secure else 'Not Secure'
                httponly = 'HttpOnly' if cookie.has_nonstandard_attr('HttpOnly') else 'Not HttpOnly'
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Cookie: {white}{cookie.name}{red} Secure: {white}{secure}{red} HttpOnly: {white}{httponly}{red}")
        except RequestException:
            pass

    def check_redirections(website_url):
        try:
            response = requests.get(website_url, timeout=5, allow_redirects=True)
            if response.history:
                for resp in response.history:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Redirections: {white}{resp.url}{red} Status: {white}{resp.status_code}{red}")
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Redirections: {white}{response.url}{red} Status: {white}{response.status_code}{red}")
            else: pass
        except RequestException:
            pass

    def check_additional_http_headers(website_url):
        try:
            response = requests.get(website_url, timeout=5)
            headers = response.headers
            additional_headers = ['Server', 'X-Powered-By', 'X-UA-Compatible', 'X-Permitted-Cross-Domain-Policies']
            for header in additional_headers:
                if header in headers:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Additional Header: {white}{header}{red} Value: {white}{headers[header]}{red}")
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Missing Additional Header: {white}{header}{red}")
        except RequestException:
            pass

    def test_performance(website_url):
        try:
            start_time = time.time()
            response = requests.get(website_url, timeout=10)
            end_time = time.time()
            response_time = end_time - start_time
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Response Time: {white}{response_time:.2f} seconds{red}")
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Response Size: {white}{len(response.content)} bytes{red}")
        except RequestException:
            pass

    def analyze_content(website_url):
        try:
            response = requests.get(website_url, timeout=5)
            content = response.text
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if title_match:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Page Title: {white}{title_match.group(1)}{red}")
            else: pass
        except RequestException:
            pass

    def analyze_dns(domain):
        try:
            result = dns.resolver.resolve(domain, 'A')
            for ipval in result:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} DNS A Record: {white}{ipval.to_text()}{red}")

            result = dns.resolver.resolve(domain, 'MX')
            for exdata in result:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} DNS MX Record: {white}{exdata.exchange}{red}")

            result = dns.resolver.resolve(domain, 'TXT')
            for txtdata in result:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} DNS TXT Record: {white}{txtdata.to_text()}{red}")

            result = dns.resolver.resolve(domain, 'NS')
            for nsdata in result:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} DNS NS Record: {white}{nsdata.to_text()}{red}")
        except: pass

    def detect_technologies(website_url):
        try:
            response = requests.get(website_url, timeout=5)
            headers = response.headers
            technologies = []

            if 'x-powered-by' in headers:
                technologies.append(f"X-Powered-By: {headers['x-powered-by']}")

            if 'server' in headers:
                technologies.append(f"Server: {headers['server']}")

            soup = BeautifulSoup(response.content, 'html.parser')
            scripts = soup.find_all('script', src=True)
            for script in scripts:
                if 'jquery' in script['src']:
                    technologies.append("jQuery")
                if 'bootstrap' in script['src']:
                    technologies.append("Bootstrap")

            if technologies:
                for tech in technologies:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Detected Technology: {white}{tech}{red}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} No specific technologies detected{red}")
        except: pass

    def analyze_whois(domain):
        try:
            whois_info = whois.whois(domain)
            registrar = whois_info.registrar
            if registrar != None:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} WHOIS Registrar: {white}{registrar}{red}")

            creation_date = whois_info.creation_date
            if creation_date != None:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} WHOIS Creation Date: {white}{creation_date}{red}")
            
            expiration_date = whois_info.expiration_date
            if expiration_date != None:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} WHOIS Expiration Date: {white}{expiration_date}{red}")

            name_servers = whois_info.name_servers
            if name_servers != None:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} WHOIS Name Servers: {white}{', '.join(name_servers)}{red}")
        except: pass

    Slow(scan_banner)
    url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Website URL -> {reset}")
    Censored(url)
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..{reset}")

    website_url = website_found_url(url)
    domain = website_domain(website_url)
    ip = website_ip(domain)
    ip_type(ip)
    test_performance(website_url)
    website_secure(website_url)
    website_status(website_url)
    ip_info(ip)
    ip_dns(ip)
    analyze_dns(domain)
    website_port(ip)
    http_headers(website_url)
    check_ssl_certificate(website_url)
    check_security_headers(website_url)
    analyze_cookies(website_url)
    check_redirections(website_url)
    check_additional_http_headers(website_url)
    analyze_content(website_url)
    detect_technologies(website_url)
    analyze_whois(domain)
    Continue()
    Reset()

except Exception as e:
    Error(e)
