"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    from json import *
    import requests
except Exception as e:
   ErrorModule(e)
   
Title("Ip Info")

try:
    ip = input(f"{color.RED}\n{INPUT} Ip -> {color.RESET}")
    print(f"{color.RED}{WAIT} Information Recovery..{reset}")
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    status = data["status"]
    if status in ["fail"]:
        status = "Invalid"
        ip_adress, country, country_code, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, url_position = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", 
    else:
        status = "Valid"
        ip_adress = data["query"]
        country = data["country"]
        country_code = data["countryCode"]
        region = data["regionName"]
        region_code = data["region"]
        city = data["city"]
        zip_postal = data["zip"]
        latitude = data["lat"]
        longitude = data["lon"]
        timezone = data["timezone"]
        isp = data["isp"]
        org = data["org"]
        as_number = data["as"]
        url_position = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

    print(f"""
    {white}[{red}+{white}]{red} Ip        : {white}{ip}{red}
    {white}[{red}+{white}]{red} Status    : {white}{status}{red}
    {white}[{red}+{white}]{red} Country   : {white}{country} ({country_code}){red}
    {white}[{red}+{white}]{red} Region    : {white}{region} ({region_code}){red}
    {white}[{red}+{white}]{red} Zip       : {white}{zip_postal}{red}
    {white}[{red}+{white}]{red} City      : {white}{city}{red}
    {white}[{red}+{white}]{red} Latitude  : {white}{latitude}{red}
    {white}[{red}+{white}]{red} Longitude : {white}{longitude}{red}
    {white}[{red}+{white}]{red} Timezone  : {white}{timezone}{red}
    {white}[{red}+{white}]{red} Isp       : {white}{isp}{red}
    {white}[{red}+{white}]{red} Org       : {white}{org}{red}
    {white}[{red}+{white}]{red} As        : {white}{as_number}{red}
    {reset}""")
    try:
        BrowserPrivate(site=url_position, title=f"Ip Localisation ({latitude}, {longitude})", search_bar=False)
    except:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)