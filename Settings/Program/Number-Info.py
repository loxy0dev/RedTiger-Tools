from Config.Util import *
from Config.Config import *
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

Title("Number Info")

phone_number = input(f"{color.RED}\n[?] | Phone Number -> {color.RESET}")
try:
    parsed_number = phonenumbers.parse(phone_number, None)
    if phonenumbers.is_valid_number(parsed_number):
        if phone_number.startswith("+"):
            country_code = "+" + phone_number[1:3] 
        else:
            country_code = "None"
        operator = carrier.name_for_number(parsed_number, "fr")
        type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_info = timezones[0] if timezones else None
        country = phonenumbers.region_code_for_number(parsed_number)
        region = geocoder.description_for_number(parsed_number, "fr")
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        status = "Valid"
    else:
        formatted_number = "None"
        region = "None"
        country = "None"
        operator = "None"
        type_number = "None"
        timezone_info = "None"
        country_code = "None"
        status = "Invalid"


    print(f"""
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Phone        : {color.WHITE}{phone_number}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Formatted    : {color.WHITE}{formatted_number}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Status       : {color.WHITE}{status}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Country Code : {color.WHITE}{country_code}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Country      : {color.WHITE}{country}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Region       : {color.WHITE}{region}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Timezone     : {color.WHITE}{timezone_info}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Operator     : {color.WHITE}{operator}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Type Number  : {color.WHITE}{type_number}{color.RED}
""")
    Continue()
    Reset()
except:
    print(f"{color.RED}[!] | Invalid Number Format ! [Format: {color.WHITE}+(country_code)(number){color.RED}] [Ex: {color.WHITE}+442012345678{color.RED} or {color.WHITE}+33623456789]")
    Continue()
    Reset()
