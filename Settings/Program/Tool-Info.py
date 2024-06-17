"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Tool Info")

try:
    print(f"\n{red}{WAIT} Information Recovery..{reset}")

    print(f"""{red}
    {white}[{red}+{white}]{red} Name Tool     :  {white}{name_tool}
    {white}[{red}+{white}]{red} Version       :  {white}{version_tool}
    {white}[{red}+{white}]{red} Copyright     :  {white}{copyright}
    {white}[{red}+{white}]{red} Coding        :  {white}{coding_tool}
    {white}[{red}+{white}]{red} Language      :  {white}{language_tool}
    {white}[{red}+{white}]{red} Creator       :  {white}{creator}
    {white}[{red}+{white}]{red} Platform      :  {white}{platform}
    {white}[{red}+{white}]{red} Discord  [02] :  {white}https://{discord_server}
    {white}[{red}+{white}]{red} Site     [02] :  {white}https://{website}
    {white}[{red}+{white}]{red} GitHub   [02] :  {white}https://{github_tool}
    {white}[{red}+{white}]{red} Telegram [02] :  {white}https://{telegram}
    {reset}""")

    license_read = input(f"{INPUT} Open 'LICENSE' ? (y/n) -> {reset}")
    if license_read in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webbrowser.open_new_tab(license)
    else:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)