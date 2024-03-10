from Config.Util import *
from Config.Config import *
import time
import os

Title("Ip Pinger")

hostname = input(color.RED + "\n[?] | IP -> " + color.RESET)

print(color.RED + f"\nInformation Ip \"{hostname}\":{color.RESET}")
time.sleep(0.5)
response = os.system("ping -n 1 " + hostname)
if response == 0:
    response = 0
    pingstatus = "Network Active"
    LAPprint(f"\n{color.RED}[!] | IP Online." + color.RESET)
else:
    pingstatus = "Network Error"
    LAPprint(f"\n{color.RED}[!] | IP Offline." + color.RESET)

Continue()
Reset()

os.system("pause")