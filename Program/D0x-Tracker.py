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
 {BEFORE}00{AFTER} Back
 {BEFORE}01{AFTER}{white} Facebook.com
 {BEFORE}02{AFTER}{white} Youtube.com
 {BEFORE}03{AFTER}{white} Twitter.com
 {BEFORE}04{AFTER}{white} Tiktok.com
 {BEFORE}05{AFTER}{white} Peekyou.com
 {BEFORE}06{AFTER}{white} Tumblr.com
 {BEFORE}07{AFTER}{white} PagesJaunes.fr
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

except Exception as e:
    Error(e)