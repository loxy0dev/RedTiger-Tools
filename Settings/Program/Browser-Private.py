from Config.Util import *
from Config.Config import *

Title("Browser Private")
print(f"\n{INFO} No marks, No saving, everything in this browser will be deleted when you close it.")
print(f"{INFO} Starting the browser..")
print(f"{INFO} Browser launched.")
print(f"{INFO} Logs:{color.RESET}")
Browser_Private(site="https://google.com", title="Browser Private")