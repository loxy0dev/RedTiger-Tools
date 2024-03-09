from Config.Config import *
from urllib.request import Request, urlopen
from json import *

ip = input(f"{color.RED}[?] | Ip -> {color.RESET}")

try:
 ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
 ipdata = loads(ipdatanojson)
except:
 ipdata = 'N/A'

try:
  country = ipdata["country_name"]
except:
  country = "N/A"
try:
  city = ipdata["city"]
except:
  city = "N/A"
try: 
  country_code = ipdata["country_code"].lower()
except:
  country_code = "N/A"
try:
  postal = ipdata["postal"]
except:
  postal = "N/A"
try:
  state = ipdata["state"]
except:
  state = "N/A"
try:
  latitude = ipdata["latitude"]
except:
  latitude = "N/A"
try:
  longitude = ipdata["longitude"]
except:
  longitude = "N/A"
  
print(f"""
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Ip        : {color.WHITE}{ip}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Country   : {color.WHITE}{country} ({country_code}){color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} State     : {color.WHITE}{state}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Postal    : {color.WHITE}{postal}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} City      : {color.WHITE}{city}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Longitude : {color.WHITE}{longitude}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Latitude  : {color.WHITE}{latitude}{color.RED}
""")
Continue()
Reset()