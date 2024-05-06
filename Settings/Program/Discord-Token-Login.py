from Config.Util import *
from Config.Config import *
try:
    from selenium import webdriver
except Exception as e:
   ErrorModule(e)

Title("Discord Token Login")

if sys.platform.startswith("linux"):
    "LINUX"
    OnlyWindows()
    
print()
token = Choice1TokenDiscord()

print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Chrome
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Firefox
{color.WHITE}[{color.RED}03{color.WHITE}] {color.RED}->{color.WHITE} Edge
""")
choice = input(f"{color.RED}{INPUT} Browser -> {color.RESET}")

try:
    if choice == '1':
        navigator = "Chrome"
        print(f"{red}[{white}{current_time_hour()}{red}] {color.RED}{WAIT} {navigator} Starting..{blue}")
        driver = webdriver.Chrome()
        print(f"{red}[{white}{current_time_hour()}{red}] {color.RED}{INFO} {navigator} Ready !{blue}")

    elif choice == '2':
        navigator = "Firefox"
        print(f"{red}[{white}{current_time_hour()}{red}] {color.RED}{WAIT} {navigator} Starting..{blue}")
        driver = webdriver.Firefox()
        print(f"{red}[{white}{current_time_hour()}{red}] {color.RED}{INFO} {navigator} Ready !{blue}")

    elif choice == '3':
        navigator = "Edge"
        print(f"{red}[{white}{current_time_hour()}{red}] {color.RED}{WAIT} {navigator} Starting..{blue}")
        driver = webdriver.Edge()
        print(f"{red}[{white}{current_time_hour()}{red}] {color.RED}{INFO} {navigator} Ready !{blue}")

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
    print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Token Connection..{blue}")
    driver.execute_script(script + f'\nlogin("{token}")')
    time.sleep(4)
    print(f"{red}[{white}{current_time_hour()}{red}] {INFO} Connected Token !{blue}")
    print(f"{INFO} If you leave the tool, edge will close!{blue}")
    Continue()
    Reset()
except:
    print(f"{color.RED}{ERROR} {navigator} not installed or driver not up to date.")
    Continue()
    Reset()