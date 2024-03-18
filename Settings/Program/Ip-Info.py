from Config.Util import *
from Config.Config import *
from urllib.request import Request, urlopen
from json import *
import requests
import webbrowser

Title("Ip Info")

ip = input(f"{color.RED}\n[?] | Ip -> {color.RESET}")

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
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Ip        : {color.WHITE}{ip}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Status    : {color.WHITE}{status}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Country   : {color.WHITE}{country} ({country_code}){color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Region    : {color.WHITE}{region} ({region_code}){color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Zip       : {color.WHITE}{zip_postal}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} City      : {color.WHITE}{city}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Longitude : {color.WHITE}{longitude}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Latitude  : {color.WHITE}{latitude}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Timezone  : {color.WHITE}{timezone}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Isp       : {color.WHITE}{isp}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Org       : {color.WHITE}{org}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} As        : {color.WHITE}{as_number}{color.RED}
""")
choice = input(f"{color.RED}[?] | Open google map (y/n) -> {color.RESET}")
if choice in ["y", "Y", "yes", "Yes", "YES" ]:
    webbrowser.open(url_position)
    Continue()
    Reset()
else:
 Continue()
 Reset()