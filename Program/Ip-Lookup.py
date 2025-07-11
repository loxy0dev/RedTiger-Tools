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
   
Title("Ip Lookup")

try:
    Slow(map_banner)
    ip = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search for information..")

    response = requests.get(f"http://ip-api.com/json/{ip}")
    api = response.json()

    status = "Valid" if api.get('status') == "success" else "Invalid"
    country = api.get('country', "None")
    country_code = api.get('countryCode', "None")
    region = api.get('regionName', "None")
    region_code = api.get('region', "None")
    zip = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('lat', "None")
    longitude = api.get('lon', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_host = api.get('as', "None")

    Slow(f"""
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} Status    : {white}{status}{red}
 {INFO_ADD} Country   : {white}{country} ({country_code}){red}
 {INFO_ADD} Region    : {white}{region} ({region_code}){red}
 {INFO_ADD} Zip       : {white}{zip}{red}
 {INFO_ADD} City      : {white}{city}{red}
 {INFO_ADD} Latitude  : {white}{latitude}{red}
 {INFO_ADD} Longitude : {white}{longitude}{red}
 {INFO_ADD} Timezone  : {white}{timezone}{red}
 {INFO_ADD} Isp       : {white}{isp}{red}
 {INFO_ADD} Org       : {white}{org}{red}
 {INFO_ADD} As        : {white}{as_host}{red}{reset}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

    Continue()
    Reset()
except Exception as e:
    Error(e)