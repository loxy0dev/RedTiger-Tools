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
    import threading
    import time
    import socket
except Exception as e:
   ErrorModule(e)
   
Title("Ip Pinger")

try:
    def ping_ip(hostname, port, bytes):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            start_time = time.time() 
            sock.connect((hostname, port))
            data = b'\x00' * bytes
            sock.sendall(data)
            end_time = time.time() 
            elapsed_time = (end_time - start_time) * 1000 
            print(f'{BEFORE + current_time_hour() + AFTER} {ADD} Hostname: {white}{hostname}{red} time: {white}{elapsed_time:.2f}ms{red} port: {white}{port}{red} bytes: {white}{bytes}{red} status: {white}succeed{red}')
        except:
            elapsed_time = 0
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Hostname: {white}{hostname}{red} time: {white}{elapsed_time}ms{red} port: {white}{port}{red} bytes: {white}{bytes}{red} status: {white}fail{red}')

    Slow(wifi_banner)

    hostname = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> " + color.RESET)

    try:
        port_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Port (enter for default) -> " + color.RESET)
        if port_input.strip():
            port = int(port_input)
        else:
            port = 80  
        
        bytes_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Bytes (enter for default) -> " + color.RESET)
        if bytes_input.strip():
            bytes = int(bytes_input)
        else:
            bytes = 64
    except:
        ErrorNumber()

    while True:
        ping_ip(hostname, port, bytes)

except Exception as e:
    Error(e)