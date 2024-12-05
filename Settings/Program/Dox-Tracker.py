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
    import webbrowser
except Exception as e:
   ErrorModule(e)
   
Title("Dox Tracker")

try:
    Slow(f"""{dox_banner}
 {BEFORE}00{AFTER} Back
 {BEFORE}01{AFTER}{white} Username
 {BEFORE}02{AFTER}{white} LastName, FirstName
 {BEFORE}03{AFTER}{white} Other
    """)

    search_type = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Search Type -> {reset}")

    if search_type in ['00', '0']:
        Reset()

    if search_type in ['01', '1']:
        search = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {reset}")
        Censored(search)
            
    elif search_type in ['02', '2']:
        name = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} LastName -> {reset}")
        first_name = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} FirstName -> {reset}")
        Censored(name)
        Censored(first_name)
        
    elif search_type in ['03', '3']:
        search = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Search -> {reset}")
        Censored(search)
    else:
        ErrorChoice()

    if search_type in ['1', '01','2','02','3','03']:
        print(f"""
{blue}[{white}00{blue}]{white}] {blue}-> Back
{blue}[{white}01{blue}]{white}] {blue}->{white} Facebook.com
{blue}[{white}02{blue}]{white}] {blue}->{white} Youtube.com
{blue}[{white}03{blue}]{white}] {blue}->{white} Twitter.com
{blue}[{white}04{blue}]{white}] {blue}->{white} Tiktok.com
{blue}[{white}05{blue}]{white}] {blue}->{white} Peekyou.com
{blue}[{white}06{blue}]{white}] {blue}->{white} Tumblr.com
{blue}[{white}07{blue}]{white}] {blue}->{white} PagesJaunes.fr
{blue}[{white}08{blue}]{white}] {blue}->{white} Doxbin
    """)
    while True:
        
        if search_type in ['1', '01','2','02','3','03']:
            choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Site -> {color.RESET}")

            if choice in ['0', '00']:
                break

            elif choice in ['01', '1']:
                if search_type in ['01', '1', '3', '03']:
                    webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={search}")
                elif search_type in ['02', '2']:
                    webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={name}%20{first_name}")

            elif choice in ['02', '2']:
                if search_type in ['01', '1', '3', '03']:
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
                elif search_type in ['02', '2']:
                    webbrowser.open(f"https://www.youtube.com/results?search_query={name}+{first_name}")
        
            elif choice in ['03', '3']:
                if search_type in ['01', '1', '3', '03']:
                    webbrowser.open(f"https://twitter.com/search?f=users&vertical=default&q={search}")
                elif search_type in ['02', '2']:
                    webbrowser.open(f"https://twitter.com/search?f=users&vertical=default&q={name}%20{first_name}")
        
            elif choice in ['04', '4']:
                if search_type in ['01', '1', '3', '03']:
                    webbrowser.open(f"https://www.tiktok.com/search?q={search}")
                elif search_type in ['02', '2']:
                    webbrowser.open(f"https://www.tiktok.com/search?q={name}%20{first_name}")

            elif choice in ['05', '5']:
                if search_type in ['01', '1', '3', '03']:
                    webbrowser.open(f"https://www.peekyou.com/{search}")
                elif search_type in ['02', '2']:
                    webbrowser.open(f"https://www.peekyou.com/{name}_{first_name}")

            elif choice in ['06', '6']:
                if search_type in ['01', '1', '3', '03']:
                    webbrowser.open(f"https://www.tumblr.com/search/{search}")
                elif search_type in ['02', '2']:
                    webbrowser.open(f"https://www.tumblr.com/search/{name}%20{first_name}")

            elif choice in ['07', '7']:
                if search_type in ['01', '1', '3', '03']:
                    webbrowser.open(f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={search}")
                elif search_type in ['02', '2']:
                    webbrowser.open(f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={name}%20{first_name}")

            elif choice in ['08', '8']:
                if search_type in ['01', '1', '3', '03']:
                    webbrowser.open(f"https://doxbin.org/search/{query}")
                elif search_type in ['02', '2']:
                    webbrowser.open(f"https://doxbin.org/search/{name}%20{first_name}")

except Exception as e:
    Error(e)
