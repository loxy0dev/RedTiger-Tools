from Config.Util import *
from Config.Config import *
try:
    import requests
    from datetime import datetime, timezone
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Info")

print()
token_discord = Choice1TokenDiscord()
print(f"{color.RED}{WAIT} Information Recovery..{reset}")
try:
    user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()

    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})

    if r.status_code == 200:
        status = "Valid"
    else:
        status = "Invalid"

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
        email_discord = user['email']
    except:
        email_discord = "None"

    try:
        email_verified_discord = user['verified']
    except:
        email_verified_discord = "None"

    try:
        phone_discord = user['phone']
    except:
        phone_discord = "None"

    try:
        mfa_discord = user['mfa_enabled']
    except:
        mfa_discord = "None"

    try:
        country_discord = user['locale']
    except:
        country_discord = "None"

    try:
        created_at_discord = datetime.fromtimestamp(((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc)
    except:
        created_at_discord = "None"

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

    try:
        avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.png"
    except:
        avatar_url_discord = "None"
    
    try:
        avatar_discord = user['avatar']
    except:
        avatar_discord = "None"

    try:
        avatar_decoration_discord = user['avatar_decoration_data']
    except:
        avatar_decoration_discord = "None"
    
    try:
        public_flags_discord = user['public_flags']
    except:
        public_flags_discord = "None"
    
    try:
        flags_discord = user['flags']
    except:
        flags_discord = "None"

    try:
        banner_discord = user['banner']
    except:
        banner_discord = "None"
    
    try:
        banner_color_discord = user['banner_color']
    except:
        banner_color_discord = "None"

    try:
        accent_color_discord = user["accent_color"]
    except:
        accent_color_discord = "None"

    try:
        nsfw_discord = user['nsfw_allowed']
    except:
        nsfw_discord = "None"

    try:
        linked_users_discord = user['linked_users']
        linked_users_discord = ' / '.join(linked_users_discord)
        if not linked_users_discord.strip():
            linked_users_discord = "None"
    except:
        linked_users_discord = "None"
    
    try:
        bio_discord = "\n" + user['bio']
        if not bio_discord.strip() or bio_discord.isspace():
            bio_discord = "None"
    except:
        bio_discord = "None"
    
    try:
        authenticator_types_discord = user['authenticator_types']
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
      print(f"{ERROR} Error when retrieving information: {white}{e}")

print(f"""
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Status       : {color.WHITE}{status}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Token        : {color.WHITE}{token_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Username     : {color.WHITE}{username_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Display Name : {color.WHITE}{display_name_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Id           : {color.WHITE}{user_id_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Created      : {color.WHITE}{created_at_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Country      : {color.WHITE}{country_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Email        : {color.WHITE}{email_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Verified     : {color.WHITE}{email_verified_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Phone        : {color.WHITE}{phone_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Nitro        : {color.WHITE}{nitro_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Linked Users : {color.WHITE}{linked_users_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar Decor : {color.WHITE}{avatar_decoration_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar       : {color.WHITE}{avatar_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar URL   : {color.WHITE}{avatar_url_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Accent Color : {color.WHITE}{accent_color_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Banner       : {color.WHITE}{banner_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Banner Color : {color.WHITE}{banner_color_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Flags        : {color.WHITE}{flags_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Public Flags : {color.WHITE}{public_flags_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} NSFW         : {color.WHITE}{nsfw_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Multi-Factor Authentication : {color.WHITE}{mfa_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Authenticator Type          : {color.WHITE}{authenticator_types_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Billing      : {color.WHITE}{payment_methods_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Gift Code    : {color.WHITE}{gift_codes_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Guilds       : {color.WHITE}{guild_count}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Owner Guilds : {color.WHITE}{owner_guild_count}{owner_guilds_names}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Bio          : {color.WHITE}{bio_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Friend       : {color.WHITE}{friends_discord}{color.RED}
""")
Continue()
Reset()