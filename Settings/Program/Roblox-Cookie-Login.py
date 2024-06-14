"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    from selenium import webdriver
except Exception as e:
   ErrorModule(e)
   

Title("Roblox Cookie Login")

try:
    if sys.platform.startswith("linux"):
        "LINUX"
        OnlyWindows()

    cookie = input(f"\n{INPUT} Cookie -> {color.WHITE}")
    print(f"""
{white}[{red}01{white}] {red}->{white} Chrome (Linux)
{white}[{red}02{white}] {red}->{white} Chrome (Windows)
{white}[{red}03{white}] {red}->{white} Firefox (Windows)
{white}[{red}04{white}] {red}->{white} Edge (Windows)
    """)
    browser = input(f"{red}{INPUT} Browser -> {reset}")

    try:
        if browser == '1':
            if sys.platform.startswith("win"):
                OnlyLinux()
            navigator = "Chrome Linux"
            print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
            chrome_driver_path = os.path.abspath("./Driver/chromedriverlinux")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
            driver = webdriver.Chrome(options=chrome_options)
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")
        if browser == '2':
            if sys.platform.startswith("linux"):
                OnlyLinux()
            navigator = "Chrome"
            print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Chrome()
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")
        elif browser == '3':
            if sys.platform.startswith("linux"):
                OnlyLinux()
            navigator = "Firefox"
            print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Firefox()
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")
        elif browser == '4':
            if sys.platform.startswith("linux"):
                OnlyLinux()
            navigator = "Edge"
            print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Edge()
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")
        else:
            ErrorChoice()

        driver.get("https://www.roblox.com/Login")
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Cookie Connection..{blue}")
        driver.add_cookie({"name" : ".ROBLOSECURITY", "value" : f"{cookie}"})
        print(f"{red}[{white}{current_time_hour()}{red}] {INFO} Connected Cookie !{blue}")
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Refresh The Page..{blue}")
        driver.refresh()
        print(f"{red}[{white}{current_time_hour()}{red}] {INFO} Connected !{blue}")
        time.sleep(1)
        driver.get("https://www.roblox.com/users/profile")
        print(f"{INFO} If you leave the tool, {navigator} will close!{blue}")
        Continue()
        Reset()
    except:
        print(f"{ERROR} {navigator} not installed or driver not up to date.")
        Continue()
        Reset()
except Exception as e:
    Error(e)