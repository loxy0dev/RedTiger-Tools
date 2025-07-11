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
    from urllib.parse import urljoin
    import re
except Exception as e:
    ErrorModule(e)

Title("Website Url Scanner")

try:
    all_links = []
    
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}

    def IsValidExtension(url):
        return re.search(r'\.(html|xhtml|php|js|css)$', url) or not re.search(r'\.\w+$', url)

    def ExtractLinks(base_url, domain, tags):
        global all_links
        extracted_links = []
        for tag in tags:
            attr = tag.get('href') or tag.get('src') or tag.get('action')
            if attr:
                full_url = urljoin(base_url, attr)
                if full_url not in all_links and domain in full_url and IsValidExtension(full_url):
                    extracted_links.append(full_url)
                    all_links.append(full_url)
        return extracted_links

    def ExtractLinksFromScript(scripts, domain):
        global all_links
        extracted_links = []
        for script in scripts:
            if script.string:
                urls_in_script = re.findall(r'(https?://\S+)', script.string)
                for url in urls_in_script:
                    if url not in all_links and domain in url and IsValidExtension(url):
                        extracted_links.append(url)
                        all_links.append(url)
        return extracted_links

    def FindSecretUrls(website_url, domain):
        global all_links
        response = requests.get(website_url, headers=headers)
        if response.status_code != 200:
            return
        soup = BeautifulSoup(response.content, 'html.parser')
        tags = soup.find_all(['a', 'link', 'script', 'img', 'iframe', 'button', 'form'])
        extracted_links = ExtractLinks(website_url, domain, tags)
        extracted_links += ExtractLinksFromScript(soup.find_all('script'), domain)
        for link in extracted_links:
            print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Url: {white}{link}")

    def FindAllSecretUrls(website_url, domain):
        FindSecretUrls(website_url, domain)
        visited_links = set()
        while True:
            new_links = [link for link in all_links if link not in visited_links]
            if not new_links:
                break
            for link in new_links:
                try:
                    if requests.get(link, headers=headers).status_code == 200:
                        FindSecretUrls(link, domain)
                        visited_links.add(link)
                except:
                    pass

    Slow(scan_banner)
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Selected User-Agent: {white + user_agent}")
    website_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Website Url -> {reset}")
    Censored(website_url)
    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url
    domain = re.sub(r'^https?://', '', website_url).split('/')[0]
    print(f"""
 {BEFORE}01{AFTER}{white} Only Url
 {BEFORE}02{AFTER}{white} All Website
    """)
    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Choice -> {reset}")
    if choice in ['1', '01']:
        FindSecretUrls(website_url, domain)
    elif choice in ['2', '02']:
        FindAllSecretUrls(website_url, domain)
    Continue()
    Reset()
except Exception as e:
    Error(e)
