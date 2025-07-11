# Copyright (c) RedTiger 
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
   
Title("Dark Web Links")

try:
    links = {
        "Search Engine": {
            "Torch": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
            "Danex": "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/",
            "Sentor": "http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/",
            "Hidden Answers": "http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/",
            "riseup searx": "http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/",
        },
        "Bitcoin Anonymity": {
            "Dark Mixer": "http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/",
            "Mixabit": "http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/",
            "EasyCoin": "http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/",
            "Onionwallet": "http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/",
            "VirginBitcoin": "http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/",
            "Cryptostamps": "http://lgh3eosuqrrtvwx3s4nurujcqrm53ba5vqsbim5k5ntdpo33qkl7buyd.onion/",
        },
        "DDoS": {
            "Stresser": "http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/",
        },
        "Market": {
            "Deep Market": "http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/",
            "DrChronic": "http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/",
            "TomAndJerry": "http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/",
            "420prime": "http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/",
            "DeDope": "http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/",
            "AccMarket": "http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/",
            "Cardshop": "http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/",
            "Darkmining": "http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/",
            "MobileStore": "http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/",
            "EuroGuns": "http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/",
            "UKpassports": "http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/",
            "ccPal": "http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/",
            "Webuybitcoins": "http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/",
            "ASAP Market": {
                "ASAP Market 1": "http://asap4u7rq4tyakf5gdahmj2c77blwc4noxnsppp5lzlhk7x34x2e22yd.onion/",
                "ASAP Market 2": "http://asap2u4pvplnkzl7ecle45wajojnftja45wvovl3jrvhangeyq67ziid.onion/",
                "ASAP Market 3": "http://asap4u2ihsunfdsumm66pmado3mt3lemdiu3fbx5b7wj5hb3xpgmwkqd.onion/",
            },
            "Cannahome": {
                "Cannahome 1": "http://cannabmgae3mkekotfzsyrx5lqg7lj7hgcn6t4rumqqs5vnvmuzsmfqd.onion/",
                "Cannahome 2": "http://cannaczy4w2nwu6d2vi5ugudrs23a4lpto2crxjl2tdvyxncsa7uwaid.onion/",
                "Cannahome 3": "http://cannabmuc64fbglolpkvnmqynsx226pg27rgimfe3gye3emgtgodohqd.onion/",
            },
            "Hydra": "http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/",
            "The Versus Project": "http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/",
            "Tor Market": "http://rrlm2f22lpqgfhyydqkxxzv6snwo5qvc2krjt2q557l7z4te7fsvhbid.onion/",
            "Drug Stores": {
                "DCdutchconnectionUK": "http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/",
                "CanabisUK": "http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/",
                "Bitpharma": "http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion/",
                "EuCanna": "http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion/",
                "Smokeables": "http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/",
                "WeedShop": "http://marijuanaman43fi4t7el66di7vdpbfyhvkgk4mt7wxkg6erfkv65npy3d.onion/",
            },
            "Cartel": "http://7myb7itqew5ffqftvxjh2k7qxwrh7imavxlpn3fxa32d3rvw32e3s7ad.onion/",
            "Kingdom Market": "http://hdfozcnzivftjokvkdjzl6fhq3c7ltyct6db4efov2w4p7xb6rmhlfqd.onion/",
        },
        "Cooks": {
            "Recipes": "http://7gppr7tlr6twnr2whsqj7scfhdeu37tnhwb5t5kffmrfzzvj7hfgowd.onion/",
        },
        "Torrents": {
            "The Pirate Bay": "http://uj3wazyk5kz5rzs.onion/",
            "1337x": "http://1337xwlc2c8sf3d7.onion/",
        },
        "Social Media": {
            "Foxy": "http://foxy6vayr5g5hwwx.onion/",
        },
        "Wikis": {
            "Hidden Wiki": "http://wikitjerrta4qgz4.onion/",
            "Deep Web Wiki": "http://wikicbtbf7rgjjbqe.onion/",
        },
        "Government": {
            "UK Passport Renewal": "http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/",
        },
        "Communities": {
            "The Versus Project": "http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/",
        },
        "Educational": {
            "EDU": "http://edu.onion/",
        },
    }

    def format_links(links):
        display_link = ""
        
        for category, sites in links.items():
            display_link += "\n" + MainColor2(category) + "\n"
            
            def add_sites(prefix, sites_dict):
                nonlocal display_link
                for i, (site, url) in enumerate(sites_dict.items()):
                    if isinstance(url, dict):
                        display_link += f"{prefix}├─ {red + site}\n"
                        add_sites(prefix + "│   ", url)
                    else:
                        if i == len(sites_dict) - 1:
                            display_link += f"{prefix}└─ {red + site}: {white + url}" + "\n"
                        else:
                            display_link += f"{prefix}├─ {red + site}: {white + url}" + "\n"
            
            add_sites("", sites)
        
        return display_link

    formatted_links = format_links(links)
    Slow(tor_banner + MainColor(formatted_links))
    Continue()
    Reset()
except Exception as e:
    Error(e)