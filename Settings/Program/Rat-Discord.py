from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
    ErrorModule(e)

Title("Rat Discord (Paid)")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} This product is paid for and available on our website.")
    webbrowser.open_new_tab(f"https://{website}")
    Continue()
    Reset()
except Exception as e:
    Error(e)
