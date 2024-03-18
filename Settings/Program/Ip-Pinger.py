from Config.Util import *
from Config.Config import *
import subprocess
import time

Title("Ip Pinger")

hostname = input(color.RED + "\n[?] | Ip -> " + color.RESET)
try:
    time_ping = int(input(color.RED + "[?] | Time Between Pings (s) -> " + color.RESET))
except:
    ErrorNumber()

def ping(ip_address):
    while True:
        result = subprocess.run(['ping', '-n', '1', ip_address], capture_output=True, text=True)

        ping_response = [line.strip() for line in result.stdout.split('\n') if "R‚ponse" in line]

        try:
            print(f"{color.WHITE}{ping_response[0]}")
        except Exception as e:
            print(f"{color.RED}[X] | Error: {color.WHITE}{e}")
        time.sleep(time_ping)

ping(hostname)

Continue()
Reset()