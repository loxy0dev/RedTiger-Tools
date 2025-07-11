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

Title("Google Dorking")

try:
    url = "https://www.google.com/search?q="
    inurl = None
    intitle = None
    site = None
    keyword = None
    filetype = None
    database = []

    def AddDataBase(request):
        database.append(request)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The query has been successfully added to the database.")

    Slow(f"""{osint_banner}
 {BEFORE}00{AFTER} Research
 {BEFORE}01{AFTER}{white} Keyword in the url of a site
 {BEFORE}02{AFTER}{white} Keyword in the title of a site
 {BEFORE}03{AFTER}{white} Specify a website
 {BEFORE}04{AFTER}{white} Keyword in pages
 {BEFORE}05{AFTER}{white} Keyword except in pages
 {BEFORE}06{AFTER}{white} File extension
    """)
 
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Several choices are possible, when you have finished put \"0\" to do the search.")
    while True:
        choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Research method -> {reset}")

        if choice in ['0', '00']:
            break

        elif choice in ['1', '01']:
            request = "inurl:" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Keyword -> {reset}")
            AddDataBase(request)

        elif choice in ['2', '02']:
            request = "intitle:" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Keyword -> {reset}")
            AddDataBase(request)

        elif choice in ['3', '03']:
            request = "site:" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Domain -> {reset}")
            AddDataBase(request)
        
        elif choice in ['4', '04']:
            request = '"' + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Keyword -> {reset}") + '"'
            AddDataBase(request)

        elif choice in ['5', '05']:
            request = "-" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Keyword -> {reset}")
            AddDataBase(request)

        elif choice in ['6', '06']:
            request = "filetype:" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Extension -> {reset}")
            AddDataBase(request)

    total_request = " ".join(database)
    url = url + total_request

    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Total Request: {white + total_request}")
    webbrowser.open(url.replace(" ", "%20").replace("\"", "%22"))
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The Google page is launched.")

    Continue()
    Reset()
except Exception as e:
    Error(e)