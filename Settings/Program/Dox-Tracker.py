from Config.Util import *
from Config.Config import *
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
Title("Dox Tracker")


print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Username
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Name, First Name
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Email
{color.WHITE}[{color.RED}04{color.WHITE}] {color.RED}->{color.WHITE} Other
""")

search_type = input(f"{color.RED}{INPUT} Search Type -> {color.RESET}")

if search_type in ['01', '1']:
    search = input(f"{color.RED}{INPUT} Username -> {color.RESET}")

elif search_type in ['02', '2']:
    name = input(f"{color.RED}{INPUT} Name -> {color.RESET}")
    first_name = input(f"{color.RED}{INPUT} First Name -> {color.RESET}")

elif search_type in ['04', '4']:
    search = input(f"{color.RED}{INPUT} Search -> {color.RESET}")

elif search_type in ['03', '3']:
    email = input(f"{color.RED}{INPUT} Email -> {color.RESET}")

else:
    ErrorChoice()

if search_type in ['3', '03']:
    print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Epieos.com
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}-> Back
""")
    
elif search_type in ['1', '01','2','02','4','04']:
    print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Facebook.com
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Youtube.com
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Twitter.com
{color.WHITE}[{color.RED}04{color.WHITE}] {color.RED}->{color.WHITE} Tiktok.com
{color.WHITE}[{color.RED}05{color.WHITE}] {color.RED}->{color.WHITE} Peekyou.com
{color.WHITE}[{color.RED}06{color.WHITE}] {color.RED}->{color.WHITE} Tumblr.com
{color.WHITE}[{color.RED}07{color.WHITE}] {color.RED}->{color.WHITE} PagesJaunes.fr
{color.WHITE}[{color.RED}08{color.WHITE}] {color.RED}-> Back
""")
while True:
    if search_type in ['3', '03']:
        choice = input(f"{color.RED}{INPUT} Site -> {color.RESET}")

        if choice in ['1', '01']:
            webbrowser.open(f"https://epieos.com/?q={email}")
        if choice in ['02', '2']:
            break
    
    elif search_type in ['1', '01','2','02','4','04']:
        choice = input(f"{color.RED}{INPUT} Site -> {color.RESET}")
        if choice in ['01', '1']:
            if search_type in ['01', '1', '4', '04']:
                webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={search}")
            elif search_type in ['02', '2']:
               webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={name}%20{first_name}")

        if choice in ['02', '2']:
            if search_type in ['01', '1', '4', '04']:
                webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.youtube.com/results?search_query={name}+{first_name}")
    
        if choice in ['04', '4']:
            if search_type in ['01', '1', '4', '04']:
                webbrowser.open(f"https://twitter.com/search?f=users&vertical=default&q={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://twitter.com/search?f=users&vertical=default&q={name}%20{first_name}")
    
        if choice in ['04', '4']:
            if search_type in ['01', '1', '4', '04']:
                webbrowser.open(f"https://www.tiktok.com/search?q={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.tiktok.com/search?q={name}%20{first_name}")

        if choice in ['05', '5']:
            if search_type in ['01', '1', '4', '04']:
                webbrowser.open(f"https://www.peekyou.com/{search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.peekyou.com/{name}_{first_name}")

        if choice in ['06', '6']:
            if search_type in ['01', '1', '4', '04']:
                webbrowser.open(f"https://www.tumblr.com/search/{search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.tumblr.com/search/{name}%20{first_name}")

        if choice in ['07', '7']:
            if search_type in ['01', '1', '4', '04']:
                webbrowser.open(f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={name}%20{first_name}")
        
        if choice in ['08', '8']:
            break

