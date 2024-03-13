from Config.Util import *
from Config.Config import *
import requests

Title("Discord Server Info")

invite = input(f"{color.RED}[?] | Server Invitation -> {color.RESET}")
try:
    invite_code = invite.split("/")[-1]
except:
    invite_code = invite
