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
try:
    import requests
    from bs4 import BeautifulSoup
    import re
    import time
except Exception as e:
   ErrorModule(e)

Title("Username Tracker")

try:
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}
    number_site = 0
    number_found = 0
    sites_and_urls_found = []

    Slow(osint_banner)
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Selected User-Agent: {white + user_agent}")
    username = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {reset}").lower()
    Censored(username)

    sites = {
        "Steam": {
            "url": f"https://steamcommunity.com/id/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Telegram": {
            "url": f"https://t.me/{username}",
            "method": "get",
            "verification": "username",
            "except": [f"if you have telegram, you can contact @{username} right away.", f"resolve?domain={username}", f"telegram: contact @{username}"]
        },
        "TikTok": {
            "url": f"https://www.tiktok.com/@{username}",
            "method": "get",
            "verification": "username",
            "except": [f"\\u002f@{username}\""]
        },
        "Instagram": {
            "url": f"https://www.instagram.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Paypal": {
            "url": f"https://www.paypal.com/paypalme/{username}",
            "method": "get",
            "verification": "username",
            "except": [f"slug_name={username}", f"\"slug\":\"{username}\"", f"2F{username}&amp"]
        },
        "GitHub": {
            "url": f"https://github.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Pinterest": {
            "url": f"https://www.pinterest.com/{username}",
            "method": "get",
            "verification": "username",
            "except": [f"[\\\"username\\\",\\\"{username}\\\"]"]
        },
        "Snapchat": {
            "url": f"https://www.snapchat.com/add/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Blogger": {
            "url": f"https://{username}.blogspot.com",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Tumblr": {
            "url": f"https://{username}.tumblr.com",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "SoundCloud": {
            "url": f"https://soundcloud.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "DeviantArt": {
            "url": f"https://www.deviantart.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "About.me": {
            "url": f"https://about.me/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Flickr": {
            "url": f"https://www.flickr.com/people/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Keybase": {
            "url": f"https://keybase.io/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Last.fm": {
            "url": f"https://www.last.fm/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Behance": {
            "url": f"https://www.behance.net/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Quora": {
            "url": f"https://www.quora.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Patreon": {
            "url": f"https://www.patreon.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Myspace": {
            "url": f"https://myspace.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Kaggle": {
            "url": f"https://www.kaggle.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Periscope": {
            "url": f"https://www.pscp.tv/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Disqus": {
            "url": f"https://disqus.com/by/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Mastodon": {
            "url": f"https://mastodon.social/@{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "GitLab": {
            "url": f"https://gitlab.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "LiveJournal": {
            "url": f"https://{username}.livejournal.com",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "CodeWars": {
            "url": f"https://www.codewars.com/users/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Gumroad": {
            "url": f"https://gumroad.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Spotify": {
            "url": f"https://open.spotify.com/user/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Weebly": {
            "url": f"https://{username}.weebly.com",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "YouTube": {
            "url": f"https://www.youtube.com/@{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "ProductHunt": {
            "url": f"https://www.producthunt.com/@{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Mix": {
            "url": f"https://mix.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Facebook": {
            "url": f"https://www.facebook.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Strava": {
            "url": f"https://www.strava.com/athletes/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Linktree": {
            "url": f"https://linktr.ee/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Xbox": {
            "url": f"https://www.xboxgamertag.com/search/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Vimeo": {
            "url": f"https://vimeo.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Twitch": {
            "url": f"https://www.twitch.tv/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Goodreads": {
            "url": f"https://www.goodreads.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "VK": {
            "url": f"https://vk.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "TripAdvisor": {
            "url": f"https://www.tripadvisor.com/members/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Dribbble": {
            "url": f"https://dribbble.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "AngelList": {
            "url": f"https://angel.co/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "500px": {
            "url": f"https://500px.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "LinkedIn": {
            "url": f"https://www.linkedin.com/in/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Weibo": {
            "url": f"https://weibo.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "OKCupid": {
            "url": f"https://www.okcupid.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Meetup": {
            "url": f"https://www.meetup.com/members/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "CodePen": {
            "url": f"https://codepen.io/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "StackOverflow": {
            "url": f"https://stackoverflow.com/users/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "HackerRank": {
            "url": f"https://www.hackerrank.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Xing": {
            "url": f"https://www.xing.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Deezer": {
            "url": f"https://www.deezer.com/en/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Snapfish": {
            "url": f"https://www.snapfish.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Ravelry": {
            "url": f"https://www.ravelry.com/people/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "ReverbNation": {
            "url": f"https://www.reverbnation.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Vine": {
            "url": f"https://vine.co/u/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Foursquare": {
            "url": f"https://foursquare.com/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Ello": {
            "url": f"https://ello.co/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Hootsuite": {
            "url": f"https://hootsuite.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Prezi": {
            "url": f"https://prezi.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Groupon": {
            "url": f"https://www.groupon.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Liveleak": {
            "url": f"https://www.liveleak.com/c/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Joomla": {
            "url": f"https://www.joomla.org/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "StackExchange": {
            "url": f"https://stackexchange.com/users/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Taringa": {
            "url": f"https://www.taringa.net/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Shopify": {
            "url": f"https://{username}.myshopify.com",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "8tracks": {
            "url": f"https://8tracks.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Couchsurfing": {
            "url": f"https://www.couchsurfing.com/people/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "OpenSea": {
            "url": f"https://opensea.io/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Trello": {
            "url": f"https://trello.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Fiverr": {
            "url": f"https://www.fiverr.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Badoo": {
            "url": f"https://badoo.com/profile/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Rumble": {
            "url": f"https://rumble.com/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Wix": {
            "url": f"https://www.wix.com/website/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "ReverbNation": {
            "url": f"https://www.reverbnation.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Gumroad": {
            "url": f"https://gumroad.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Vimeo": {
            "url": f"https://vimeo.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "TripAdvisor": {
            "url": f"https://www.tripadvisor.com/members/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Snapfish": {
            "url": f"https://www.snapfish.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "DeviantArt": {
            "url": f"https://www.deviantart.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "VK": {
            "url": f"https://vk.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "allmylinks": {
            "url": f"https://allmylinks.com/{username}",
            "method": "get",
            "verification": "status",
            "except": ["This page is missing"]
        },
        "Medium": {
            "url": f"https://medium.com/@{username}",
            "method": "get",
            "verification": "status",
            "except": ["Out of nothing, something."]
        },
        "Reddit": {
            "url": f"https://reddit.com/user/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Sorry, nobody on Reddit goes by that name."]
        },
        "Twitter": {
            "url": f"https://x.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None  
        },
        "Fosstodon": {
            "url": f"https://fosstodon.org/@{username}",
            "method": "get",
            "verification": "status",
            "except": ["The user could not be found"]
        },
        "Bugcrowd": {
            "url": f"https://bugcrowd.com/{username}",
            "method": "get",
            "verification": "status",
            "except": ["The requested page was not found"]
        },
        "HackerOne": {
            "url": f"https://hackerone.com/{username}",
            "method": "post",
            "verification": "status",
            "except": ["User does not exist"]
        },
        "HackTheBox": {
            "url": f"https://app.hackthebox.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": ["User not found"]
        },
        "Apple Developer": {
            "url": f"https://developer.apple.com/forums/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": ["The page you’re looking for can’t be found"]
        },
        "Apple Discussions": {
            "url": f"https://discussions.apple.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": ["The page you tried was not found. You may have used an outdated link or may have typed the address (URL) incorrectly."]
        },
        "Hacker News": {
            "url": f"https://news.ycombinator.com/user?id={username}",
            "method": "get",
            "verification": "status",
            "except": ["No such user."]
        },
        "Bitbucket": {
            "url": f"https://bitbucket.org/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Repository not found"]
        },
        "Slack": {
            "url": f"https://{username}.slack.com",
            "method": "get",
            "verification": "status",
            "except": ["This workspace doesn’t exist"]
        },
        "Slide Share": {
            "url": f"https://www.slideshare.net/{username}",
            "method": "get",
            "verification": "status",
            "except": ["This username"]
        },
        "Wattpad": {
            "url": f"https://www.wattpad.com/user/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Oops! That page can’t be found."]
        },
        "Codecademy": {
            "url": f"https://www.codecademy.com/profiles/{username}",
            "method": "get",
            "verification": "status",
            "except": ["This profile could not be found"]
        },
        "Gravatar": {
            "url": f"https://gravatar.com/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Uh oh. Page not found"]
        },
        "Dev To": {
            "url": f"https://dev.to/{username}",
            "method": "get",
            "verification": "status",
            "except": ["This page does not exist"]
        },
        "Kaskus": {
            "url": f"https://www.kaskus.co.id/profile/@{username}",
            "method": "get",
            "verification": "status",
            "except": ["We can't find the page you are looking for"]
        },
        "Crunchbase": {
            "url": f"https://www.crunchbase.com/person/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Page Not Found"]
        }
    }

    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..")

    session = requests.Session()

    for site, data in sites.items():
        try:
            number_site += 1
            url = data["url"]
            method = data["method"]
            verification = data["verification"]
            page_except = data["except"]

            try:
                found = False
                if method == "get":
                    response = session.get(url, timeout=5, headers=headers)

                if response.status_code == 200:
                    page_content = re.sub(r'<[^>]*>', '', response.text.lower().replace(url, "").replace(f"/{username}", ""))
                    soup = BeautifulSoup(response.text, 'html.parser')
                    page_text = soup.get_text().lower().replace(url, "")
                    page_title = soup.title.string.lower() if soup.title and soup.title.string else ""

                    if "status" in verification:
                        found = True
                        if page_except:
                            for page_content_except in page_except:
                                if page_content_except.lower() in page_content or page_content_except.lower() in page_text or page_content_except.lower() in page_title:
                                    found = False

                    elif "username" in verification:
                        if page_except:
                            for page_content_except in page_except:
                                page_content = page_content.replace(page_content_except.lower(), '')
                                page_text = page_text.replace(page_content_except.lower(), '')
                                page_title = page_title.replace(page_content_except.lower(), '')
                        found = username in page_title or username in page_content or username in page_text


                    if found:
                        number_found += 1
                        sites_and_urls_found.append({site: url})
                        print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} {site}: {white + url}")
                    else:
                        print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} {site}:{white} Not Found")

                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} {site}:{white} Not Found")

            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {site}: {white}Error: {e}")
        except:
            pass
    
    if number_found > 0:
        print(f"\n{red}Total Found:{reset}")
        for site_and_url_found in sites_and_urls_found:
            for site, url in site_and_url_found.items():
                time.sleep(0.1)
                print(f"{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                print(f"{ADD} Name: {white + site}")
                print(f"{ADD} Link: {white + url}")
        print(f"{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Total Website: {white}{number_site}{red} Total Found: {white}{number_found}{red}")
    Continue()
    Reset()

except Exception as e:
    Error(e)