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

    cookie = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Cookie -> {white}")
    print(f"""
{white}[{red}01{white}] {red}->{white} Chrome (Linux)
{white}[{red}02{white}] {red}->{white} Chrome (Windows)
{white}[{red}03{white}] {red}->{white} Firefox (Windows)
{white}[{red}04{white}] {red}->{white} Edge (Windows)
    """)
    browser = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Browser -> {reset}")

    if browser in ['1', '01']:
        if sys.platform.startswith("win"):
            OnlyWindows()
        try:
            navigator = "Chrome Linux"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
            chrome_driver_path = os.path.abspath("./Driver/chromedriverlinux")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
            driver = webdriver.Chrome(options=chrome_options)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()
            
    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Chrome"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Chrome()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()

    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Firefox"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Firefox()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()

    elif browser in ['4', '04']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Edge"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Edge()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()
    else:
        ErrorChoice()
    
    try:
        driver.get("https://www.roblox.com/Login")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Cookie Connection..{blue}")
        driver.add_cookie({"name" : ".ROBLOSECURITY", "value" : f"{cookie}"})
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Connected Cookie !{blue}")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Refresh The Page..{blue}")
        driver.refresh()
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Connected !{blue}")
        time.sleep(1)
        driver.get("https://www.roblox.com/users/profile")
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} If you leave the tool, {navigator} will close!{blue}")
        Continue()
        Reset()
    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
        Continue()
        Reset()
except Exception as e:
    Error(e)