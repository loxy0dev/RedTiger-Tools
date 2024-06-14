"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
   ErrorModule(e)
   

Title("Number Info")

try:
    phone_number = input(f"{color.RED}\n{INPUT} Phone Number -> {color.RESET}")
    print(f"{color.RED}{WAIT} Information Recovery..{reset}")
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
    {white}[{red}+{white}]{red} Phone        : {white}{phone_number}{red}
    {white}[{red}+{white}]{red} Formatted    : {white}{formatted_number}{red}
    {white}[{red}+{white}]{red} Status       : {white}{status}{red}
    {white}[{red}+{white}]{red} Country Code : {white}{country_code}{red}
    {white}[{red}+{white}]{red} Country      : {white}{country}{red}
    {white}[{red}+{white}]{red} Region       : {white}{region}{red}
    {white}[{red}+{white}]{red} Timezone     : {white}{timezone_info}{red}
    {white}[{red}+{white}]{red} Operator     : {white}{operator}{red}
    {white}[{red}+{white}]{red} Type Number  : {white}{type_number}{red}
    """)
        Continue()
        Reset()
    except:
        print(f"{INFO} Invalid Format ! [Ex: {white}+442012345678{red} or {white}+33623456789]")
        Continue()
        Reset()
except Exception as e:
    Error(e)