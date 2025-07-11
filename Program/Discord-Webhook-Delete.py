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
    import requests
except Exception as e:
   ErrorModule(e)
   

Title("Discord Webhook Delete")

try:
    webhook_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} URL Webhook -> {color.RESET}")
    if CheckWebhook(webhook_url) == False:
        ErrorWebhook()
    try:
        response = requests.delete(webhook_url)
        response.raise_for_status()
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Webhook Deleted.")
        Continue()
        Reset()
    except:
        ErrorWebhook()
except Exception as e:
    Error(e)