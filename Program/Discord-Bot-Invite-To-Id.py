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
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Discord Invite Bot To Id")

try:
    Slow(discord_banner)
    try:
        IdBot = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} ID bot -> {reset}"))
    except:
        ErrorId()

    invite_url = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'
    response = requests.get(invite_url)
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Invite Url: {white + invite_url} (status: {response.status_code})")

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Open in browser ? (y/n) -> {reset}")
    if choice in ['y', 'Y', 'Yes', 'yes']:
        webbrowser.open_new_tab(invite_url)
        Continue()
        Reset()
    else:
        Continue()
        Reset()
except Exception as e:
    Error(e)
