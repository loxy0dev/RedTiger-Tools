from Config.Util import *
from Config.Config import *
from selenium import webdriver

Title("Discord Token Login")

token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")

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
    
    script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
    driver.get("https://discord.com/login")
    print(f"{color.RED}[!] | Token Connection..")
    driver.execute_script(script + f'\nlogin("{token}")')
    time.sleep(4)
    print(f"{color.RED}[!] | Connected Token !")
    print(f"{color.YELLOW}[!] | If you leave the tool, edge will close!")
    input(f"{color.RED}[?] | Leave Edge (enter) -> {color.WHITE}")
    Reset()
except:
    print(f"{color.RED}[X] | {navigator} not installed or driver not up to date.")
    Continue()
    Reset()