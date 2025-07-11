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
except Exception as e:
   ErrorModule(e)
   
Title("Discord Server Info")

try:
    Slow(discord_banner)
    invite = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Server Invitation -> {reset}")
    try:
        invite_code = invite.split("/")[-1]
    except:
        invite_code = invite

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        api = response.json()

        type_value = api.get('type', "None")
        code_value = api.get('code', "None")
        inviter_info = api.get('inviter', {})
        inviter_id = inviter_info.get('id', "None")
        inviter_username = inviter_info.get('username', "None")
        inviter_avatar = inviter_info.get('avatar', "None")
        inviter_discriminator = inviter_info.get('discriminator', "None")
        inviter_public_flags = inviter_info.get('public_flags', "None")
        inviter_flags = inviter_info.get('flags', "None")
        inviter_banner = inviter_info.get('banner', "None")
        inviter_accent_color = inviter_info.get('accent_color', "None")
        inviter_global_name = inviter_info.get('global_name', "None")
        inviter_banner_color = inviter_info.get('banner_color', "None")
        expires_at = api.get('expires_at', "None")
        flags = api.get('flags', "None")
        server_info = api.get('guild', {})
        server_id = server_info.get('id', "None")
        server_name = server_info.get('name', "None")
        server_icon = server_info.get('icon', "None")
        server_features = server_info.get('features', "None")
        if server_features != "None":
            server_features = ' / '.join(server_features)
        server_verification_level = server_info.get('verification_level', "None")
        server_nsfw_level = server_info.get('nsfw_level', "None")
        server_descritpion = server_info.get('description', "None")
        server_nsfw = server_info.get('nsfw', "None")
        server_premium_subscription_count = server_info.get('premium_subscription_count', "None")
        channel_info = api.get('channel', {})
        channel_id = channel_info.get('id', "None")
        channel_type = channel_info.get('type', "None")
        channel_name = channel_info.get('name', "None")
    else:
        ErrorUrl()

    Slow(f"""
{red}Invitation Information:
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} Invitation         : {white}{invite}{red}
 {INFO_ADD} Type               : {white}{type_value}{red}
 {INFO_ADD} Code               : {white}{code_value}{red}
 {INFO_ADD} Expired            : {white}{expires_at}{red}
 {INFO_ADD} Server ID          : {white}{server_id}{red}
 {INFO_ADD} Server Name        : {white}{server_name}{red}
 {INFO_ADD} Channel ID         : {white}{channel_id}{red}
 {INFO_ADD} Channel Name       : {white}{channel_name}{red}
 {INFO_ADD} Channel Type       : {white}{channel_type}{red}
 {INFO_ADD} Server Description : {white}{server_descritpion}{red}
 {INFO_ADD} Server Icon        : {white}{server_icon}{red}
 {INFO_ADD} Server Features    : {white}{server_features}{red}
 {INFO_ADD} Server NSFW Level  : {white}{server_nsfw_level}{red}
 {INFO_ADD} Server NSFW        : {white}{server_nsfw}{red}
 {INFO_ADD} Flags              : {white}{flags}{red}
 {INFO_ADD} Server Verification Level         : {white}{server_verification_level}{red}
 {INFO_ADD} Server Premium Subscription Count : {white}{server_premium_subscription_count}{red}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

    if inviter_info:
        Slow(f"""{red}Inviter Information:
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} ID            : {white}{inviter_id}{red}
 {INFO_ADD} Username      : {white}{inviter_username}{red}
 {INFO_ADD} Global Name   : {white}{inviter_global_name}{red}
 {INFO_ADD} Avatar        : {white}{inviter_avatar}{red}
 {INFO_ADD} Discriminator : {white}{inviter_discriminator}{red}
 {INFO_ADD} Public Flags  : {white}{inviter_public_flags}{red}
 {INFO_ADD} Flags         : {white}{inviter_flags}{red}
 {INFO_ADD} Banner        : {white}{inviter_banner}{red}
 {INFO_ADD} Accent Color  : {white}{inviter_accent_color}{red}
 {INFO_ADD} Banner Color  : {white}{inviter_banner_color}{red}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")
    Continue()
    Reset()
except Exception as e:
    Error(e)