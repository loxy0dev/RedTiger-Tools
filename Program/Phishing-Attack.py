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
    import os
    import concurrent.futures
except Exception as e:
    ErrorModule(e)

Title("Phishing Attack")

try:
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}

    Slow(phishing_banner)
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Selected User-Agent: {white + user_agent}")
    website_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Website Url -> {reset}")
    Censored(website_url)
    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url

    def CssAndJs(html_content, base_url):
        soup = BeautifulSoup(html_content, 'html.parser')

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Css recovery..")
        css_links = soup.find_all('link', rel='stylesheet')
        all_css = []
        css_urls = [urljoin(base_url, link['href']) for link in css_links]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            css_responses = executor.map(requests.get, css_urls)
            for css_response in css_responses:
                if css_response.status_code == 200:
                    all_css.append(css_response.text)
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error retrieving css.")
        
        if all_css:
            style_tag = soup.new_tag('style')
            style_tag.string = "\n".join(all_css)
            soup.head.append(style_tag)
            for link in css_links:
                link.decompose()

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Javascript recovery..")
        script_links = soup.find_all('script', src=True)
        all_js = []
        js_urls = [urljoin(base_url, script['src']) for script in script_links]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            js_responses = executor.map(requests.get, js_urls)
            for js_response in js_responses:
                if js_response.status_code == 200:
                    all_js.append(js_response.text)
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error retrieving javascript.")

        if all_js:
            script_tag = soup.new_tag('script')
            script_tag.string = "\n".join(all_js)
            soup.body.append(script_tag)
            for script in script_links:
                script.decompose()

        return soup.prettify()

    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Html recovery..")
    session = requests.Session()
    response = session.get(website_url, headers=headers, timeout=5)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        file_name = re.sub(r'[\\/:*?"<>|]', '-', soup.title.string if soup.title else 'Phishing')

        file_html_relative = f'\\1-Output\\PhishingAttack\\{file_name}.html'
        file_html = os.path.join(tool_path, "1-Output", "PhishingAttack", f"{file_name}.html")

        final_html = CssAndJs(html_content, website_url)

        with open(file_html, 'w', encoding='utf-8') as file:
            file.write(final_html)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Phishing attack successful. The file is located in the folder \"{white}{file_html_relative}{red}\"")
        Continue()
        Reset()
    else:
        ErrorUrl()
except Exception as e:
    Error(e)
