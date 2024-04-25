from Config.Util import *
from Config.Config import *
try:
   import socket
   import concurrent.futures
except Exception as e:
   ErrorModule(e)
   
Title("Ip Port")

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {white}Open{red} | Port: {white}{port}")
        sock.close()
    except Exception as e:
        print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Error: {white}{e}")
        return

def scan_ports(ip, start_port, end_port):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}

ip = input(f"{color.RED}\n{INPUT} Ip -> {color.RESET}")
print(f"{WAIT} Search Port..")
start_port = 1
end_port = 65535

scan_ports(ip, start_port, end_port)
Continue()
Reset()