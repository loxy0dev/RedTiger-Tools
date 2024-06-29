# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)
   
Title("Illegal Website")

try:
    fr = f"{color.GREEN}FREE{color.RED}"
    pa = f"{color.YELLOW}PAID{color.RED}"
    w = color.WHITE
    r = color.RED
    y = color.YELLOW
    print(f"""
 {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 {w}┃                 {r}DDOS{w}                 ┃                  {r}IP{w}                  ┃              {r}OSINT/DOX{w}               ┃
 {w}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
 {w}┃[{r}01{w}] {fr} https://ddosnow.com/{w}        ┃[{r}07{w}]{r} https://iplogger.org/{w}            ┃[{r}13{w}]{r} https://doxbin.net/{w}              ┃
 {w}┃[{r}02{w}] {fr} https://stresser.zone/{w}      ┃[{r}08{w}]{r} https://grabify.link/{w}            ┃[{r}14{w}]{r} https://osint.industries{w}         ┃
 {w}┃[{r}03{w}] {fr} https://stresse.ru/{w}         ┃[{r}09{w}]{r} https://grabify.icu/{w}             ┃[{r}15{w}]{r} https://epieos.com/{w}              ┃
 {w}┃[{r}04{w}] {pa} https://stresse.cat/{w}        ┃[{r}10{w}]{r} https://whatstheirip.tech/{w}       ┃[{r}16{w}]{r} https://nuwber.fr/{w}               ┃
 {w}┃[{r}05{w}] {pa} https://starkstresser.net/{w}  ┃[{r}11{w}]{r} https://www.spylink.net/{w}         ┃[{r}17{w}]{r} https://osintframework.com{w}       ┃
 {w}┃[{r}06{w}] {pa} https://ddos.services/{w}      ┃[{r}12{w}]{r} https://ipinfo.io/{w}               ┃[{r}18{w}]{r} https://whatsmyname.app/{w}         ┃
 {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            {w}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {w}┃                                          {r}Dark Web{w}                                         ┃
            {w}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {w}┃{y}Search Engine:{w}                                                                             ┃
            {w}┃[{r}Torch{w}]        : {r}http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/{w}    ┃
            {w}┃[{r}Danex{w}]        : {r}http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/{w}    ┃
            {w}┃[{r}Sentor{w}]       : {r}http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/{w}    ┃
            {w}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {w}┃{y}Bitcoin Anonymity:{w}                                                                         ┃
            {w}┃[{r}Dark Mixer{w}]   : {r}http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/{w}    ┃
            {w}┃[{r}Mixabit{w}]      : {r}http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/{w}    ┃
            {w}┃[{r}EasyCoin{w}]     : {r}http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/{w}    ┃
            {w}┃[{r}Onionwallet{w}]  : {r}http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/{w}    ┃
            {w}┃[{r}VirginBitcoin{w}]: {r}http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/{w}    ┃
            {w}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {w}┃{y}Stresser / Ddos:{w}                                                                           ┃
            {w}┃[{r}Stresser{w}]     : {r}http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/{w}    ┃
            {w}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {w}┃{y}Market:{w}                                                                                    ┃
            {w}┃[{r}Deep Market{w}]  : {r}http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/{w}    ┃
            {w}┃[{r}DrChronic{w}]    : {r}http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/{w}    ┃
            {w}┃[{r}TomAndJerry{w}]  : {r}http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/{w}    ┃
            {w}┃[{r}420prime{w}]     : {r}http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/{w}    ┃
            {w}┃[{r}Can*abisUK{w}]   : {r}http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/{w}    ┃
            {w}┃[{r}DeDope{w}]       : {r}http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/{w}    ┃
            {w}┃[{r}AccMarket{w}]    : {r}http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/{w}    ┃
            {w}┃[{r}Cardshop{w}]     : {r}http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/{w}    ┃
            {w}┃[{r}Darkmining{w}]   : {r}http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/{w}    ┃
            {w}┃[{r}MobileStore{w}]  : {r}http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/{w}    ┃
            {w}┃[{r}EuroGuns{w}]     : {r}http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/{w}    ┃
            {w}┃[{r}UKpassports{w}]  : {r}http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/{w}    ┃
            {w}┃[{r}ccPal{w}]        : {r}http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/{w}    ┃
            {w}┃[{r}Webuybitcoins{w}]: {r}http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/{w}    ┃
            {w}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {w}┃{y}DataBase:{w}                                                                                  ┃
            {w}┃[{r}Database{w}]     : {r}http://breachdbsztfykg2fdaq2gnqnxfsbj5d35byz3yzj73hazydk4vq72qd.onion/{w}    ┃
            {w}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

 {white}[{red}00{white}] {red}->{white} Back
""")

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Site -> {color.WHITE}")
    if choice in ['01', '1']:
        webbrowser.open("https://ddosnow.com")

    if choice in ['02', '2']:
        webbrowser.open("https://stresser.zone")

    if choice in ['03', '3']:
        webbrowser.open("https://stresse.ru")

    if choice in ['04', '4']:
        webbrowser.open("https://stresse.cat")

    if choice in ['05', '5']:
        webbrowser.open("https://starkstresser.net")

    if choice in ['06', '6']:
        webbrowser.open("https://ddos.services")

    if choice in ['07', '7']:
        webbrowser.open("https://iplogger.org/")

    if choice in ['08', '8']:
        webbrowser.open("https://grabify.link/")

    if choice in ['09', '9']:
        webbrowser.open("https://grabify.icu/")

    if choice in ['10']:
        webbrowser.open("https://whatstheirip.tech/")

    if choice in ['11']:
        webbrowser.open("https://www.spylink.net/")

    if choice in ['12']:
        webbrowser.open("https://ipinfo.io/")

    if choice in ['13']:
        webbrowser.open("https://doxbin.net/")

    if choice in ['14']:
        webbrowser.open("https://www.geocreepy.com/")

    if choice in ['15']:
        webbrowser.open("https://epieos.com/")
except Exception as e:
    Error(e)