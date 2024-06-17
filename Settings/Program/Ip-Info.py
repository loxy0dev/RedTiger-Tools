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
    ip = input(f"\n{INPUT} Ip -> {reset}")
    print(f"{WAIT} Information Recovery..{reset}")

    response = requests.get(f"https://{website}/api/ip/ip={ip}")
    api = response.json()

    ip = api['ip']
    status = api['status']
    country = api['country']
    country_code = api['country_code']
    region = api['region']
    region_code = api['region_code']
    zip = api['zip']
    city = api['city']
    latitude = api['latitude']
    longitude = api['longitude']
    timezone = api['timezone']
    isp = api['isp']
    org = api['org']
    as_host = api['as']
    loc_url = api['loc_url']
    credit = api['credit']
    copyright = api['copyright']

    print(f"""
    {white}[{red}+{white}]{red} Ip        : {white}{ip}{red}
    {white}[{red}+{white}]{red} Status    : {white}{status}{red}
    {white}[{red}+{white}]{red} Country   : {white}{country} ({country_code}){red}
    {white}[{red}+{white}]{red} Region    : {white}{region} ({region_code}){red}
    {white}[{red}+{white}]{red} Zip       : {white}{zip}{red}
    {white}[{red}+{white}]{red} City      : {white}{city}{red}
    {white}[{red}+{white}]{red} Latitude  : {white}{latitude}{red}
    {white}[{red}+{white}]{red} Longitude : {white}{longitude}{red}
    {white}[{red}+{white}]{red} Timezone  : {white}{timezone}{red}
    {white}[{red}+{white}]{red} Isp       : {white}{isp}{red}
    {white}[{red}+{white}]{red} Org       : {white}{org}{red}
    {white}[{red}+{white}]{red} As        : {white}{as_host}{red}
    {white}[{red}+{white}]{red} Copyright : {white}{copyright}{red}
    {reset}""")
    try:
        BrowserPrivate(site=loc_url, title=f"Ip Localisation ({latitude}, {longitude})", search_bar=False)
    except:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)