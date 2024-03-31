from Config.Util import *
from Config.Config import *
import requests

Title("Discord Server Info")

invite = input(f"{color.RED}\n{INPUT} Server Invitation -> {color.RESET}")
try:
    invite_code = invite.split("/")[-1]
except:
    invite_code = invite
response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

if response.status_code == 200:
    data = response.json()
    type_value = data['type']
    code_value = data['code']
    inviter_id = data['inviter']['id']
    inviter_username = data['inviter']['username']
    inviter_avatar = data['inviter']['avatar']
    inviter_discriminator = data['inviter']['discriminator']
    inviter_public_flags = data['inviter']['public_flags']
    inviter_premium_type = data['inviter']['premium_type']
    inviter_flags = data['inviter']['flags']
    inviter_banner = data['inviter']['banner']
    inviter_accent_color = data['inviter']['accent_color']
    inviter_global_name = data['inviter']['global_name']
    inviter_banner_color = data['inviter']['banner_color']
    expires_at = data['expires_at']
    flags = data['flags']
    server_id = data['guild_id']
    server_name = data['guild']['name']
    server_icon = data['guild']['icon']
    server_features = data['guild']['features']
    server_verification_level = data['guild']['verification_level']
    server_nsfw_level = data['guild']['nsfw_level']
    server_nsfw = data['guild']['nsfw']
    server_premium_subscription_count = data['guild']['premium_subscription_count']
    channel_id = data['channel']['id']
    channel_type = data['channel']['type']
    channel_name = data['channel']['name']
else:
    ErrorUrl()

print(f"""{color.RED}
Invitation Information:
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Invitation        : {color.WHITE}{invite}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Type              : {color.WHITE}{type_value}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Code              : {color.WHITE}{code_value}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Expired           : {color.WHITE}{expires_at}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server ID         : {color.WHITE}{server_id}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server Name       : {color.WHITE}{server_name}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Channel ID        : {color.WHITE}{channel_id}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Channel Name      : {color.WHITE}{channel_name}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Channel Type      : {color.WHITE}{channel_type}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server Icon       : {color.WHITE}{server_icon}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server Features   : {color.WHITE}{server_features}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server NSFW Level : {color.WHITE}{server_nsfw_level}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server NSFW       : {color.WHITE}{server_nsfw}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Flags             : {color.WHITE}{flags}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server Verification Level         : {color.WHITE}{server_verification_level}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Server Premium Subscription Count : {color.WHITE}{server_premium_subscription_count}{color.RED}

Inviter Information:
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} ID            : {color.WHITE}{inviter_id}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Username      : {color.WHITE}{inviter_username}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Global Name   : {color.WHITE}{inviter_global_name}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Avatar        : {color.WHITE}{inviter_avatar}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Discriminator : {color.WHITE}{inviter_discriminator}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Public Flags  : {color.WHITE}{inviter_public_flags}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Premium Type  : {color.WHITE}{inviter_premium_type}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Flags         : {color.WHITE}{inviter_flags}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Banner        : {color.WHITE}{inviter_banner}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Accent Color  : {color.WHITE}{inviter_accent_color}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Banner Color  : {color.WHITE}{inviter_banner_color}{color.RED}
""")
Continue()
Reset()