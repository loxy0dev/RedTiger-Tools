from Config.Util import *
from Config.Config import *
import requests

webhook_url = input(f"{color.RED}\n[?] | URL Webhook -> {color.RESET}")
try:
    response = requests.delete(webhook_url)
    response.raise_for_status()
    print(f"{color.RED}[!] | Webhook Deleted.")
    Continue()
    Reset()
except:
    ErrorWebhook()