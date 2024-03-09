from Config.Config import *
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

Title("Discord Token Login")

token = input(f"{color.RED}\n[?] | Token -> {color.RESET}")
try:
    webdriver_path = './Driver/msedgedriver.exe'

    edge_options = EdgeOptions()
    edge_options.use_chromium = True

    edge_service = EdgeService(webdriver_path)

    driver = webdriver.Edge(service=edge_service, options=edge_options)
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
    print(f"{color.RED}[!] | Edge Starting..")
    driver.get("https://discord.com/login")
    print(f"{color.RED}[!] | Edge Ready !")
    print(f"{color.RED}[!] | Token Connection..")
    driver.execute_script(script + f'\nlogin("{token}")')
    print(f"{color.RED}[!] | Connected Token !")
    print(f"{color.YELLOW}[!] | If you leave the tool, edge will close!")
    input(f"{color.RED}[?] | Leave Edge (enter) -> {color.WHITE}")
    Reset()
except:
    print(f"{color.RED}[X] | Edge not installed or driver not up to date.")
    Continue()
    Reset()