from Options.Options import *

Title("Info")

LAPprint(f"""\n{color.RED}Informations:
{color.YELLOW}Username      :  {color.CYAN}{username_user}
{color.YELLOW}Theme         :  {color.CYAN}{theme}
{color.YELLOW}Name Tool     :  {color.CYAN}{name_tool}
{color.YELLOW}Version       :  {color.CYAN}{version_tool}
{color.YELLOW}Coding        :  {color.CYAN}{coding_tool}
{color.YELLOW}Language      :  {color.CYAN}{language_tool}
{color.YELLOW}Virus         :  {color.CYAN}None
{color.YELLOW}Token Grab    :  {color.CYAN}None
{color.YELLOW}By            :  {color.CYAN}{creator}
{color.YELLOW}Discord [02]  :  {color.CYAN}{discord}
{color.YELLOW}Site    [02]  :  {color.CYAN}{website}
""" + color.RESET)

Continue()
Reset()