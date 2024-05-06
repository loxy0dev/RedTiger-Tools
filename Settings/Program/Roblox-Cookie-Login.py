from Config.Util import *
from Config.Config import *
try:
    from selenium import webdriver
except Exception as e:
   ErrorModule(e)
   

Title("Roblox Cookie Login")

if sys.platform.startswith("linux"):
    "LINUX"
    OnlyWindows()

cookie = input(f"\n{INPUT} Cookie -> {color.WHITE}")
print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Chrome
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Firefox
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Edge
""")
choice = input(f"{INPUT} Browser -> {color.RESET}")
try:
    if choice == '1':
        navigator = "Chrome"
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
        driver = webdriver.Chrome()
        print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")

    elif choice == '2':
        navigator = "Firefox"
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
        driver = webdriver.Firefox()
        print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")

    elif choice == '3':
        navigator = "Edge"
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
        driver = webdriver.Edge()
        print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")

    else:
        ErrorChoice()


    driver.get("https://www.roblox.com/home")
    print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Cookie Connection..{blue}")
    driver.add_cookie({"name" : ".ROBLOSECURITY", "value" : f"{cookie}"})
    print(f"{red}[{white}{current_time_hour()}{red}] {INFO} Connected Cookie !{blue}")
    print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Refresh The Page..{blue}")
    driver.refresh()
    print(f"{red}[{white}{current_time_hour()}{red}] {INFO} Connected !{blue}")
    print(f"{INFO} If you leave the tool, {navigator} will close!{blue}")
    Continue()
    Reset()
except:
    print(f"{color.RED}{ERROR} {navigator} not installed or driver not up to date.")
    Continue()
    Reset()