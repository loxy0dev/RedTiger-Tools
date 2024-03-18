from Config.Util import *
from Config.Config import *
import requests

Title("Discord Token Info")

token_discord = input(f"{color.RED}\n[?] | Token -> {color.RESET}")
try:
 print(f"{color.RED}[!] | Information Recovery..")
 user = requests.get(
    'https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()
 billing_discord = requests.get(
    'https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
 guilds = requests.get(
    'https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord}).json()
 friends = requests.get(
    'https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token_discord}).json()
 gift_codes_discord = requests.get(
    'https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()

 username_discord = user['username'] + '#' + user['discriminator']
 user_id_discord = user['id']
 email_discord = user['email']
 phone_discord = user['phone']
 mfa_discord = user['mfa_enabled']
except:
      ErrorToken()
      
try:
    avatar_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif" if requests.get(
        f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.png"
except:
    avatar_discord = "None"

if user['premium_type'] == 0:
                nitro_discord = 'None'
elif user['premium_type'] == 1:
                nitro_discord = 'Nitro Classic'
elif user['premium_type'] == 2:
                nitro_discord = 'Nitro Boosts'
elif user['premium_type'] == 3:
                nitro_discord = 'Nitro Basic'
else:
                nitro_discord = 'None'

if billing_discord:
    payment_methods = []

    for method in billing_discord:
        if method['type'] == 1:
            payment_methods.append('CB: ')

        elif method['type'] == 2:
            payment_methods.append("Paypal: ")

        else:
            payment_methods.append('Other: ')

    payment_methods = ', '.join(payment_methods)

else:
    billing_discord = "None"

if friends:
    hq_friends_discord = []
    for friend in friends:
        unprefered_flags = [64, 128, 256, 1048704]
        data = f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})"

        if len('\n'.join(hq_friends_discord)) + len(data) >= 1024:
            break

        hq_friends_discord.append(data)

    if len(hq_friends_discord) > 0:
        hq_friends_discord = '\n' + ' / '.join(hq_friends_discord)

    else:
        hq_friends_discord = "None"

else:
    hq_friends_discord = "None"

if gift_codes_discord:
    codes = []
    for code in gift_codes_discord:
        name = code['promotion']['outbound_title']
        code = code['code']
        data = f":gift: `{name}`\n:ticket: `{code}`"

        if len('\n\n'.join(codes)) + len(data) >= 1024:
            break

        codes.append(data)

    if len(codes) > 0:
        codes = '\n\n'.join(codes)

    else:
        codes = "None"

else:
    gift_codes_discord = "None"

print(f"""{color.RED}
{color.WHITE}[{color.RED}!{color.WHITE}]{color.RED} Token {color.WHITE}Valid{color.RED}.
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Username  : {color.WHITE}{username_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Id        : {color.WHITE}{user_id_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Email     : {color.WHITE}{email_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Phone     : {color.WHITE}{phone_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Token     : {color.WHITE}{token_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Nitro     : {color.WHITE}{nitro_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar    : {color.WHITE}{avatar_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Multi-Factor Authentication : {color.WHITE}{mfa_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Billing   : {color.WHITE}{billing_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Gift Code : {color.WHITE}{gift_codes_discord}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Friend    : {color.WHITE}{hq_friends_discord}{color.RED}
""")
Continue()
Reset()