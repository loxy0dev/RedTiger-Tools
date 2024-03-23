from Config.Util import *
from Config.Config import *
import webbrowser
Title("Illegal Website")

fr = f"{color.GREEN}FREE{color.RED}"
pa = f"{color.YELLOW}PAID{color.RED}"
w = color.WHITE
r = color.RED
print(f"""
  {color.WHITE}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  {color.WHITE}┃                 {r}DDOS{w}                 ┃                  {r}IP{w}                  ┃                 {r}DOX{w}                  ┃
  {color.WHITE}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
  {color.WHITE}┃[{r}01{w}] {fr} https://ddosnow.com/{w}        ┃[{r}07{w}]{r} https://iplogger.org/{w}            ┃[{r}13{w}]{r} https://doxbin.net/{w}              ┃
  {color.WHITE}┃[{r}02{w}] {fr} https://stresser.zone/{w}      ┃[{r}08{w}]{r} https://grabify.link/{w}            ┃[{r}14{w}]{r} https://www.geocreepy.com/{w}       ┃
  {color.WHITE}┃[{r}03{w}] {fr} https://stresse.ru/{w}         ┃[{r}09{w}]{r} https://grabify.icu/{w}             ┃[{r}15{w}]{r} https://epieos.com/{w}              ┃
  {color.WHITE}┃[{r}04{w}] {pa} https://stresse.cat/{w}        ┃[{r}10{w}]{r} https://whatstheirip.tech/{w}       ┃[{r}16{w}]                                  ┃
  {color.WHITE}┃[{r}05{w}] {pa} https://starkstresser.net/{w}  ┃[{r}11{w}]{r} https://www.spylink.net/{w}         ┃[{r}17{w}]                                  ┃
  {color.WHITE}┃[{r}06{w}] {pa} https://ddos.services/{w}      ┃[{r}12{w}]{r} https://ipinfo.io/{w}               ┃[{r}18{w}]                                  ┃
  {color.WHITE}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
              {color.WHITE}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
              {color.WHITE}┃                                          {r}Dark Web{w}                                         ┃
              {color.WHITE}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
              {color.WHITE}┃[{r}Stresser{w}]     : {r}http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/{w}    ┃
              {color.WHITE}┃[{r}Deep Market{w}]  : {r}http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/{w}    ┃
              {color.WHITE}┃[{r}Torch{w}]        : {r}http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/{w}    ┃
              {color.WHITE}┃[{r}Danex{w}]        : {r}http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/{w}    ┃
              {color.WHITE}┃[{r}Database{w}]     : {r}http://breachdbsztfykg2fdaq2gnqnxfsbj5d35byz3yzj73hazydk4vq72qd.onion/{w}    ┃
              {color.WHITE}┃[{r}Sentor{w}]       : {r}http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/{w}    ┃
              {color.WHITE}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

 {color.WHITE}[{color.RED}00{color.WHITE}] {color.RED}->{color.WHITE} BACK
""")

choice = input(f"{color.RED}{INPUT} Site -> {color.WHITE}")
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