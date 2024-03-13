from Config.Util import *
from Config.Config import *
import os
from selenium import webdriver

Title("Roblox Cookie Login")

cookie = input(f"{color.RED}\n[?] | Cookie -> {color.WHITE}")
print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Chrome
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Firefox
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Edge
""")
choice = input(f"{color.RED}-> {color.RESET}")
try:
    if choice == '1':
        navigator = "Chrome"
        print(f"{color.RED}[!] | {navigator} Starting..{color.RESET}")
        driver = webdriver.Chrome()
        print(f"{color.RED}[!] | {navigator} Ready !{color.RESET}")

    elif choice == '2':
        navigator = "Firefox"
        print(f"{color.RED}[!] | {navigator} Starting..{color.RESET}")
        driver = webdriver.Firefox()
        print(f"{color.RED}[!] | {navigator} Ready !{color.RESET}")

    elif choice == '3':
        navigator = "Edge"
        print(f"{color.RED}[!] | {navigator} Starting..{color.RESET}")
        driver = webdriver.Edge()
        print(f"{color.RED}[!] | {navigator} Ready !{color.RESET}")

    else:
        ErrorChoice()


    driver.get("https://www.roblox.com/home")
    print(f"{color.RED}[!] | Cookie Connection..{color.RESET}")
    driver.add_cookie({"name" : ".ROBLOSECURITY", "value" : f"{cookie}"})
    print(f"{color.RED}[!] | Connected Cookie !{color.RESET}")
    print(f"{color.RED}[!] | Refresh The Page..{color.RESET}")
    driver.refresh()
    print(f"{color.RED}[!] | Connected !{color.RESET}")
    print(f"{color.YELLOW}[!] | If you leave the tool, {navigator} will close!{color.RESET}")
    input(f"{color.RED}[?] | Leave {navigator} (enter) -> {color.WHITE}")
    Reset()
except:
    print(f"{color.RED}[X] | {navigator} not installed or driver not up to date.")
    Continue()
    Reset()