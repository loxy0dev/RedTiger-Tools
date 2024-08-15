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
    import os
    import requests
    from bs4 import BeautifulSoup
    import re
    from urllib.parse import urljoin
except Exception as e:
    ErrorModule(e)

Title("Phishing Attack")

try:
    Slow(phishing_banner)
    website_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Website Url -> {reset}")
    Censored(website_url)
    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url

    def css_and_js(html_content, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Css recovery..")
        css_links = soup.find_all('link', rel='stylesheet')
        all_css = ""

        for link in css_links:
            css_url = urljoin(base_url, link['href'])
            try:
                css_response = requests.get(css_url)
                if css_response.status_code == 200:
                    all_css += css_response.text + "\n"
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error retrieving css.")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error retrieving css.")
        
        if all_css:
            style_tag = soup.new_tag('style')
            style_tag.string = all_css
            soup.head.append(style_tag)
            for link in css_links:
                link.decompose()

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Javascript recovery..")
        script_links = soup.find_all('script', src=True)
        all_js = ""

        for script in script_links:
            js_url = urljoin(base_url, script['src'])
            try:
                js_response = requests.get(js_url)
                if js_response.status_code == 200:
                    all_js += js_response.text + "\n"
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error retrieving javascript.")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error retrieving javascript.")
        
        if all_js:
            script_tag = soup.new_tag('script')
            script_tag.string = all_js
            soup.body.append(script_tag)
            for script in script_links:
                script.decompose()

        return soup.prettify()

    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Html recovery..")
    response = requests.get(website_url, timeout=5)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        file_name = re.sub(r'[\\/:*?"<>|]', '-', soup.title.string if soup.title else 'Phishing')

        file_html_relative = f'\\1-Output\\PhishingAttack\\{file_name}.html'
        file_html = os.path.join(tool_path, "1-Output", "PhishingAttack", f"{file_name}.html")

        final_html = css_and_js(html_content, website_url)

        with open(file_html, 'w', encoding='utf-8') as file:
            file.write(final_html)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Phishing attack successful. The file is located in the folder \"{white}{file_html_relative}{red}\"")
        Continue()
        Reset()
    else:
        ErrorUrl()
except Exception as e:
    Error(e)