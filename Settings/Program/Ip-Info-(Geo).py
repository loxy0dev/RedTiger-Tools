"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    import requests
    import socket
    import concurrent.futures
except Exception as e:
   ErrorModule(e)
   
Title("Ip Info")

try:
    Slow(map_banner)
    ip = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")

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
    {INFO_ADD} Ip         : {white}{ip}{red}
    {INFO_ADD} Status     : {white}{status}{red}
    {INFO_ADD} Country    : {white}{country} ({country_code}){red}
    {INFO_ADD} Region     : {white}{region} ({region_code}){red}
    {INFO_ADD} Zip        : {white}{zip}{red}
    {INFO_ADD} City       : {white}{city}{red}
    {INFO_ADD} Latitude   : {white}{latitude}{red}
    {INFO_ADD} Longitude  : {white}{longitude}{red}
    {INFO_ADD} Timezone   : {white}{timezone}{red}
    {INFO_ADD} Isp        : {white}{isp}{red}
    {INFO_ADD} Org        : {white}{org}{red}
    {INFO_ADD} As         : {white}{as_host}{red}
    {reset}""")
    try:
        BrowserPrivate(site=loc_url, title=f"Ip Localisation ({latitude}, {longitude})", search_bar=False)
    except:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)