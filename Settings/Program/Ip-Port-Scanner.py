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
except Exception as e:
   ErrorModule(e)
   
Title("Ip Port Scanner")

try:
    def scan_port(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Open{red} | Port: {white}{port}")
            sock.close()
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}")
            return

    def scan_ports(ip, start_port, end_port):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}

    ip = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..")
    start_port = 1
    end_port = 65535

    scan_ports(ip, start_port, end_port)
    Continue()
    Reset()
except Exception as e:
    Error(e)