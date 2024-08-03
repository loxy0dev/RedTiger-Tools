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
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
   ErrorModule(e)

Title("Username Tracker (Osint)")

try:
    sites = {
        "Twitter": "https://twitter.com/{}",
        "Instagram": "https://www.instagram.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Tumblr": "https://{}.tumblr.com",
        "YouTube": "https://www.youtube.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "About.me": "https://about.me/{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "Medium": "https://medium.com/@{}",
        "Blogger": "https://{}.blogspot.com",
        "Goodreads": "https://www.goodreads.com/{}",
        "Keybase": "https://keybase.io/{}",
        "VK": "https://vk.com/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Last.fm": "https://www.last.fm/user/{}",
        "Slideshare": "https://www.slideshare.net/{}",
        "Dribbble": "https://dribbble.com/{}",
        "Behance": "https://www.behance.net/{}",
        "AngelList": "https://angel.co/{}",
        "ProductHunt": "https://www.producthunt.com/@{}",
        "500px": "https://500px.com/{}",
        "LinkedIn": "https://www.linkedin.com/in/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "WhatsApp": "https://wa.me/{}",
        "Discord": "https://discord.com/users/{}",
        "Telegram": "https://t.me/{}",
        "Quora": "https://www.quora.com/profile/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Patreon": "https://www.patreon.com/{}",
        "Weibo": "https://weibo.com/{}",
        "OKCupid": "https://www.okcupid.com/profile/{}",
        "Meetup": "https://www.meetup.com/members/{}",
        "Myspace": "https://myspace.com/{}",
        "Kaggle": "https://www.kaggle.com/{}",
        "CodePen": "https://codepen.io/{}",
        "StackOverflow": "https://stackoverflow.com/users/{}",
        "HackerRank": "https://www.hackerrank.com/{}",
        "Xing": "https://www.xing.com/profile/{}",
        "Deezer": "https://www.deezer.com/en/user/{}",
        "Mix": "https://mix.com/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "Periscope": "https://www.pscp.tv/{}",
        "Tidal": "https://tidal.com/{}",
        "Yelp": "https://www.yelp.com/user_details?userid={}",
        "Disqus": "https://disqus.com/by/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Ravelry": "https://www.ravelry.com/people/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Vine": "https://vine.co/u/{}",
        "Foursquare": "https://foursquare.com/user/{}",
        "Mastodon": "https://mastodon.social/@{}",
        "Ello": "https://ello.co/{}",
        "GitLab": "https://gitlab.com/{}",
        "Giphy": "https://giphy.com/{}",
        "Hootsuite": "https://hootsuite.com/{}",
        "LiveJournal": "https://{}.livejournal.com",
        "Linktree": "https://linktr.ee/{}",
        "Prezi": "https://prezi.com/{}",
        "Groupon": "https://www.groupon.com/profile/{}",
        "Liveleak": "https://www.liveleak.com/c/{}",
        "Joomla": "https://www.joomla.org/user/{}",
        "StackExchange": "https://stackexchange.com/users/{}",
        "Weebly": "https://{}.weebly.com",
        "CodeWars": "https://www.codewars.com/users/{}",
        "Taringa": "https://www.taringa.net/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Shopify": "https://{}.myshopify.com",
        "8tracks": "https://8tracks.com/{}",
        "Couchsurfing": "https://www.couchsurfing.com/people/{}",
        "OpenSea": "https://opensea.io/{}",
        "Trello": "https://trello.com/{}",
        "Tinder": "https://www.tinder.com/@{}",
        "Strava": "https://www.strava.com/athletes/{}",
        "Fiverr": "https://www.fiverr.com/{}",
        "Coursera": "https://www.coursera.org/user/{}",
        "Badoo": "https://badoo.com/profile/{}",
        "Rumble": "https://rumble.com/user/{}",
        "Wix": "https://www.wix.com/website/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "Tinder": "https://www.tinder.com/@{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Mix": "https://mix.com/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "Medium": "https://medium.com/@{}",
        "GitHub": "https://github.com/{}",
        "VK": "https://vk.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Instagram": "https://www.instagram.com/{}",
        "Twitter": "https://twitter.com/{}",
        "GitHub": "https://github.com/{}",
    }


    number_site = 0
    number_found = 0
    username = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {reset}")
    Censored(username)
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Account search..")
    username_lower = username.lower()
    for site, url_template in sites.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, timeout=2)
            number_site += 1
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                page_text = soup.get_text().lower()
                if username_lower in page_text:
                    number_found += 1
                    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {site}: {white + url}")
        except: pass

    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Total Website: {white}{number_site}{red}, Found: {white}{number_found}{red}")
    Continue()
    Reset()
except Exception as e:
    Error(e)