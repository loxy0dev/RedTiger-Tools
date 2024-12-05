from Config.Util import *
from Config.Config import *
try:
    from selenium import webdriver
except Exception as e:
   ErrorModule(e)
   

Title("Roblox Cookie Login")

try:

    cookie = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Cookie -> {white}")
    print(f"""
 {BEFORE}01{AFTER}{white} Chrome (Windows / Linux)
 {BEFORE}02{AFTER}{white} Edge (Windows)
 {BEFORE}03{AFTER}{white} Firefox (Windows)
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
