from Options.Options import *
from urllib.request import Request, urlopen
from json import *

ip = input(f"{color.RED}[?] | Ip -> {color.RESET}")

try:
 ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
 ipdata = loads(ipdatanojson)
except:
 ipdata = 'N/A'

try:
 pays = ipdata["country_name"]
except:
  pays = "N/A"
try:
 ville = ipdata["city"]
except:
 ville = "N/A"
try:
 pays_code = ipdata["country_code"].lower()
except:
  pays_code = "N/A"
try:
 postal = ipdata["postal"]
except:
  postal = "N/A"
try:
 etat = ipdata["state"]
except:
  etat = "N/A"
try:
  latitude = ipdata["latitude"]
except:
  latitude = "N/A"
try:
  longitude = ipdata["longitude"]
except:
  longitude = "N/A"
  
print(f"""{color.RED}
Localisation "{color.CYAN}{ip}{color.RED}":
{color.YELLOW}Country    : {color.CYAN}{pays} ({pays_code})
{color.YELLOW}State      : {color.CYAN}{etat}
{color.YELLOW}Postal     : {color.CYAN}{postal}
{color.YELLOW}City       : {color.CYAN}{ville}
{color.YELLOW}Longitude  : {color.CYAN}{longitude}
{color.YELLOW}Latitude   : {color.CYAN}{latitude}
""")
Continue()
Reset()