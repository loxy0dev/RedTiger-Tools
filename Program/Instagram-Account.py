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
    import instaloader
    import sys
    import os
    import contextlib
except Exception as e:
   ErrorModule(e)
   
Title("Instagram Account")

try:
    def Search(username):
        @contextlib.contextmanager
        def Output():
            with open(os.devnull, 'w') as devnull:
                old_stdout = sys.stdout
                old_stderr = sys.stderr
                sys.stdout = devnull
                sys.stderr = devnull
                try:
                    yield
                finally:
                    sys.stdout = old_stdout
                    sys.stderr = old_stderr

        with Output():
            loader  = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, username)
        
        return loader, profile

    Slow(osint_banner)
    username = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Instagram Username -> {reset}")

    try:
        loader, profile = Search(username)
    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} You have exceeded your limit or the user does not exist, try again in a few minutes.")
        Continue()
        Reset()
    
    Slow(f"""    
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {INFO_ADD} Full Name       : {white}{profile.full_name}
 {INFO_ADD} Username        : {white}{profile.username}
 {INFO_ADD} Instagram Id    : {white}{profile.userid}
 {INFO_ADD} Biography       : {white}{profile.biography}
 {INFO_ADD} Profile Url     : {white}https://instagram.com/{profile.username}
 {INFO_ADD} Profile Photo   : {white}{profile.profile_pic_url}
 {INFO_ADD} Publications    : {white}{profile.mediacount}
 {INFO_ADD} Subscribers     : {white}{profile.followers}
 {INFO_ADD} Subscriptions   : {white}{profile.followees}
 {INFO_ADD} Verified        : {white}{'True' if profile.is_verified else 'False'}
 {INFO_ADD} Private Account : {white}{'True' if profile.is_private else 'False'}
 {INFO_ADD} Pro Account     : {white}{'True' if profile.is_business_account else 'False'}""")

    if profile.is_business_account:
        print(f"    {INFO_ADD} Category Pro    : {white}{profile.business_category_name}")

    print(f"{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    if not profile.is_private or loader.context.username == profile.username:
        try:
            posts = profile.get_posts()
            for i, post in enumerate(posts):
                Slow(f"""    
 {INFO_ADD} Publication n°{i+1}
 {INFO_ADD} URL        : {white}https://www.instagram.com/p/{post.shortcode}/
 {INFO_ADD} Date       : {white}{post.date}
 {INFO_ADD} Likes      : {white}{post.likes}
 {INFO_ADD} Comments   : {white}{post.comments}
 {INFO_ADD} Legend     : {white}{post.caption}
{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
                if i == 4:
                    break
            print()
        except Exception as e:
            print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Error retrieving posts.")
    
    Continue()
    Reset()
except Exception as e:
    Error(e)