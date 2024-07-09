# Copyright (c) RedTiger (https://redtiger.shop)
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
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
   ErrorModule(e)
   

Title("Number Info (Lookup)")

try:
    phone_number = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Phone Number -> {color.RESET}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
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
    {INFO_ADD} Phone        : {white}{phone_number}{red}
    {INFO_ADD} Formatted    : {white}{formatted_number}{red}
    {INFO_ADD} Status       : {white}{status}{red}
    {INFO_ADD} Country Code : {white}{country_code}{red}
    {INFO_ADD} Country      : {white}{country}{red}
    {INFO_ADD} Region       : {white}{region}{red}
    {INFO_ADD} Timezone     : {white}{timezone_info}{red}
    {INFO_ADD} Operator     : {white}{operator}{red}
    {INFO_ADD} Type Number  : {white}{type_number}{red}
    """)
        Continue()
        Reset()
    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Invalid Format ! [Ex: {white}+442012345678{red} or {white}+33623456789{red}]")
        Continue()
        Reset()
except Exception as e:
    Error(e)