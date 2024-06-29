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
    import random
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from deep_translator import GoogleTranslator
    from selenium.webdriver.common.keys import Keys
except Exception as e:
   ErrorModule(e)

Title("Username Tracker (OSINT)")

try:
    username = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {reset}")

    if censored in username:
        print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find username "{white}{username}{red}".')
        Continue()
        Reset()

    print(f"""
{white}[{red}01{white}] {red}->{white} Chrome (Windows / Linux)
{white}[{red}02{white}] {red}->{white} Edge (Windows)
{white}[{red}03{white}] {red}->{white} Firefox (Windows)
    """)
    browser = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Browser -> {reset}")
 
    if browser in ['1', '01']:
        try:
            navigator = "Chrome"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Chrome()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()

    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Edge"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
                driver = webdriver.Edge()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
                Continue()
                Reset()

    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Firefox"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
                driver = webdriver.Firefox()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
                Continue()
                Reset()
    else:
        ErrorChoice()

    driver.set_window_size(900, 600)

    def text_page():
        page_text = driver.execute_script("return document.documentElement.innerText")
        return page_text
        
    def text_translated(text):
        try:
            translated_text = GoogleTranslator(source='auto', target='en').translate(text)
        except: 
            translated_text = text
        return translated_text

    def tiktok_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Tiktok..{blue}")
        try:
            link = r"https://www.tiktok.com/@" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "This account cannot be found" in text_translated(text_page()):
                tiktok = False
            else:
                tiktok = link
        except Exception as e:
            tiktok = f"Error: {e}"
        return tiktok

    def instagram_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Instagram..{blue}")
        try:
            link = r"https://instagram.com/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "This page is unfortunately not available" in text_translated(text_page()):
                instagram = False
            else:
                instagram = link
        except Exception as e:
            instagram = f"Error: {e}"
        return instagram

    def giters_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Giters..{blue}")
        try:
            link = r"https://giters.com/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "This page could not be found" in text_translated(text_page()):
                giters = False
            elif username in text_page():
                giters = link
            else:
                giters = False

        except Exception as e:
            giters = f"Error: {e}"
        return giters

    def github_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Github..{blue}")
        try:
            link = r"https://github.com/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "Find code, projects, and people on GitHub" in text_translated(text_page()):
                github = False
            else:
                github = link
        except Exception as e:
            github = f"Error: {e}"
        return github

    def paypal_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Paypal..{blue}")
        try:
            link = r"https://www.paypal.com/paypalme/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "We cannot find this profile" in text_translated(text_page()):
                paypal = False
            elif "We were not able to process your request. Please try again later" in text_translated(text_page()):
                paypal = f"Error: Rate Limit"
            else:
                paypal = link
        except Exception as e:
            paypal = f"Error: {e}"
        return paypal

    def telegram_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Telegram..{blue}")
        try:
            link = r"https://t.me/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "If you have Telegram, you can contact" in text_translated(text_page()):
                telegram = False
            elif "a new era of messaging" in text_translated(text_page()):
                telegram = False
            else:
                telegram = link
        except Exception as e:
            telegram = f"Error: {e}"
        return telegram

    def snapchat_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Snapchat..{blue}")
        try:
            link = r"https://www.snapchat.com/add/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "This content could not be found" in text_translated(text_page()):
                snapchat = False
            else:
                snapchat = link
        except Exception as e:
            snapchat = f"Error: {e}"
        return snapchat

    def linktree_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Linktree..{blue}")
        try:
            link = r"https://linktr.ee/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "The page you’re looking for doesn’t exist" in text_translated(text_page()):
                linktree = False
            else:
                linktree = link
        except Exception as e:
            linktree = f"Error: {e}"
        return linktree

    def roblox_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Roblox..{blue}")
        try:
            link = r"https://www.roblox.com/search/users?keyword=" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "No results available for" in text_translated(text_page()):
                roblox = False
            else:
                roblox = link
        except Exception as e:
            roblox = f"Error: {e}"
        return roblox

    def streamlabs_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Streamlabs..{blue}")
        try:
            link = r"https://streamlabs.com/" + username + r"/tip"
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "UNAUTHORIZED" in text_translated(text_page()):
                streamlabs = False
            elif "401" in text_translated(text_page()):
                streamlabs = False
            else:
                streamlabs = link
        except Exception as e:
            streamlabs = f"Error: {e}"
        return streamlabs


    Slow(f"""
{BEFORE + current_time_hour() + AFTER} {INFO} The username "{white}{username}{red}" was found:

    {INFO_ADD} Tiktok     : {white}{tiktok_search()}{red}
    {INFO_ADD} Instagram  : {white}{instagram_search()}{red}
    {INFO_ADD} Snapchat   : {white}{snapchat_search()}{red}
    {INFO_ADD} Giters     : {white}{giters_search()}{red}
    {INFO_ADD} Github     : {white}{github_search()}{red}
    {INFO_ADD} Paypal     : {white}{paypal_search()}{red}
    {INFO_ADD} Telegram   : {white}{telegram_search()}{red}
    {INFO_ADD} Linktree   : {white}{linktree_search()}{red}
    {INFO_ADD} Roblox     : {white}{roblox_search()}{red}
    {INFO_ADD} Streamlabs : {white}{streamlabs_search()}{red}
    """)

    driver.quit()

    Continue()
    Reset()
except Exception as e:
    Error(e)