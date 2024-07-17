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
    import random
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from deep_translator import GoogleTranslator
    from selenium.webdriver.common.keys import Keys
except Exception as e:
   ErrorModule(e)

Title("Email Tracker (Osint)")

try:
    email = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Email -> {reset}")
    Censored(email)

    print(f"""
{white}[{red}01{white}] {red}->{white} Chrome (Windows / Linux)
{white}[{red}02{white}] {red}->{white} Edge (Windows)
{white}[{red}03{white}] {red}->{white} Firefox (Windows)
    """)
    browser = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Browser -> {reset}")
 
    if browser in ['1', '01']:
        try:
            navigator = "Chrome"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Chrome()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()

    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Edge"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
                driver = webdriver.Edge()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
                Continue()
                Reset()

    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Firefox"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
                driver = webdriver.Firefox()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
                Continue()
                Reset()
    else:
        ErrorChoice()

    driver.set_window_size(900, 600)

    def text_page():
        page_text = driver.execute_script("return document.documentElement.innerText")
        return page_text
        
    def text_translated(text):
        try:
            translated_text = GoogleTranslator(source='auto', target='en').translate(text)
        except: 
            translated_text = text
        return translated_text

    def twitter_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Twitter..{blue}")
        try:
            driver.get(r"https://twitter.com/i/flow/login")
            driver.implicitly_wait(10)
            time.sleep(2)
            email_enter = driver.find_element(By.XPATH, '//input[contains(@class, "r-30o5oe") and @name="text"]')
            email_enter.send_keys(email)
            email_enter.send_keys(Keys.RETURN)
            time.sleep(2)
            if "Sorry, we couldn't find your account" in text_translated(text_page()):
                twitter = False
            else:
                twitter = True
        except Exception as e:
            twitter = f"Error: {e}"
        return twitter

    def google_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Google..{blue}")
        try:
            driver.get(r"https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmyaccount.google.com%2F&ec=GAlAwAE&hl=fr&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-1241433703%3A1715014494878825&theme=mn&ddm=0")
            driver.implicitly_wait(10)
            time.sleep(2)
            email_enter = driver.find_element(By.XPATH, '//input[contains(@class, "whsOnd") and contains(@class, "zHQkBf") and @type="email" and @name="identifier"]')
            email_enter.send_keys(email)
            email_enter.send_keys(Keys.RETURN)
            time.sleep(2)
            if "Enter a valid email address or phone number" in text_translated(text_page()):
                google = False
            elif "Can't find your Google account" in text_translated(text_page()):
                google = False
            else:
                google = True
        except Exception as e:
            google = f"Error: {e}"
        return google

    def instagram_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Instagram..{blue}")
        try:
            driver.get(r"https://www.instagram.com/accounts/emailsignup/")
            driver.implicitly_wait(10)
            time.sleep(2)
            number = random.randint(9999099999999, 999999999999999999999999999)
            email_enter = driver.find_element(By.XPATH, '//input[contains(@class, "_aa4b") and contains(@class, "_add6") and contains(@class, "_ac4d") and contains(@class, "_ap35") and @type="text" and @name="emailOrPhone"]')
            email_enter.send_keys(email)
            email_enter.send_keys(Keys.RETURN)
            name_enter = driver.find_element(By.XPATH, '//div[contains(@class, "x6s0dn4") and contains(@class, "x1nk0tez") and contains(@class, "x1xp9za0") and contains(@class, "x1hm1hlx") and contains(@class, "x1npaq5j") and contains(@class, "x1c83p5e") and contains(@class, "x199158v") and contains(@class, "x13fuv20") and contains(@class, "x1q0q8m5") and contains(@class, "x26u7qi") and contains(@class, "x178xt8z") and contains(@class, "xso031l") and contains(@class, "xy80clv") and contains(@class, "x9f619") and contains(@class, "x5n08af") and contains(@class, "x78zum5") and contains(@class, "x1q0g3np") and contains(@class, "xvs91rp") and contains(@class, "x1n2onr6") and contains(@class, "xh8yej3")]//input[@name="fullName"]')
            name_enter.send_keys("Red Tiger")
            name_enter.send_keys(Keys.RETURN)
            username_enter = driver.find_element(By.XPATH, '//div[contains(@class, "x6s0dn4") and contains(@class, "xnz67gz") and contains(@class, "x19gtwsn") and contains(@class, "x1nk0tez") and contains(@class, "x1xp9za0") and contains(@class, "x1hm1hlx") and contains(@class, "x1npaq5j") and contains(@class, "x1c83p5e") and contains(@class, "x1enjb0b") and contains(@class, "x199158v") and contains(@class, "x13fuv20") and contains(@class, "xu3j5b3") and contains(@class, "x1q0q8m5") and contains(@class, "x26u7qi") and contains(@class, "x178xt8z") and contains(@class, "xm81vs4") and contains(@class, "xso031l") and contains(@class, "xy80clv") and contains(@class, "x9f619") and contains(@class, "x5n08af") and contains(@class, "x78zum5") and contains(@class, "x1q0g3np") and contains(@class, "xvs91rp") and contains(@class, "x1n2onr6") and contains(@class, "xh8yej3")]//input[@name="username"]')
            username_enter.send_keys(f"redtiger{number}")
            username_enter.send_keys(Keys.RETURN)
            password_enter = driver.find_element(By.XPATH, '//div[contains(@class, "x6s0dn4") and contains(@class, "xnz67gz") and contains(@class, "x19gtwsn") and contains(@class, "x1nk0tez") and contains(@class, "x1xp9za0") and contains(@class, "x1hm1hlx") and contains(@class, "x1npaq5j") and contains(@class, "x1c83p5e") and contains(@class, "x1enjb0b") and contains(@class, "x199158v") and contains(@class, "x13fuv20") and contains(@class, "xu3j5b3") and contains(@class, "x1q0q8m5") and contains(@class, "x26u7qi") and contains(@class, "x178xt8z") and contains(@class, "xm81vs4") and contains(@class, "xso031l") and contains(@class, "xy80clv") and contains(@class, "x9f619") and contains(@class, "x5n08af") and contains(@class, "x78zum5") and contains(@class, "x1q0g3np") and contains(@class, "xvs91rp") and contains(@class, "x1n2onr6") and contains(@class, "xh8yej3")]//input[@name="password"]')
            password_enter.send_keys(f"RedTiger.{number}")
            password_enter.send_keys(Keys.RETURN)
            time.sleep(2)
            if "Another account uses the same email address" in text_translated(text_page()):
                instagram = True
            else:
                instagram = False
        except Exception as e:
            instagram = f"Error: {e}"
        return instagram

    def snapchat_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Snapchat..{blue}")
        try:
            driver.get(r"https://www.snapchat.com/?original_referrer=none")
            driver.implicitly_wait(10)
            time.sleep(2)
            email_enter = driver.find_element(By.XPATH, '//input[@id="ai_input" and contains(@class, "sidebar_input__AVHKi")]')
            email_enter.send_keys(email)
            email_enter.send_keys(Keys.RETURN)
            time.sleep(2)
            if "We can't find an account matching this username" in text_translated(text_page()):
                snapchat = False
            elif "We can't find an account matching this email address" in text_translated(text_page()):
                snapchat = False
            elif "Confirm it's you" in text_translated(text_page()):
                snapchat = "Error: Captcha"
            else:
                snapchat = True
        except Exception as e:
            snapchat = f"Error: {e}"
        return snapchat

    def microsoft_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Microsoft..{blue}")
        try:
            driver.get(r"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?scope=service%3A%3Aaccount.microsoft.com%3A%3AMBI_SSL%20openid%20profile%20offline_access&response_type=code&client_id=81feaced-5ddd-41e7-8bef-3e20a2689bb7&redirect_uri=https%3A%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin-oauth&client-request-id=61ddde4f-db57-4b1a-a700-ba7c7805ba76&x-client-SKU=MSAL.Desktop&x-client-Ver=4.58.1.0&x-client-OS=Windows%20Server%202019%20Datacenter&prompt=select_account&client_info=1&state=H4sIAAAAAAAEAA3NS4JDMAAA0LvMtgu0SC3rU5Voqe_IjqJCKhm_weln3gXel8xul3EBneq48lrUc0c_NdoTd7O6JtZEDbvfyIprH7znfVwMjdqParx-9uQuNRW0w9lihW6eHEA4r00aDk8UnA769wokAScYDogZCZkWEm7tmXGuvUYHY09VR_NH0JFuJHLhQoTGLbCH8PIb1zHUnySbyyxtfDvY1eljrmRhspZZQl-lsExXmBORPSGgWZb5fax4F7rmUuoHcj5Q0CFRbaK2VRBQTtJdukZI1zQuyFv0f7_dH15iwZtQ2QuwOR3E-2bkoEV9UJf-5ATnX-Pqn8clW56WL-0OcZt3_lJpf-ZTqBbo9WDabQtvHIulB6YCBoGcZolLGVo8RawoWpJjK3k4iipSeaFIhmsx2AzndvcazJorRwU68x267ObPX39XKEYaggEAAA&msaoauth2=true&lc=1036&ru=https%3A%2F%2Faccount.microsoft.com%2Faccount%3Flang%3Dfr-fr%26refd%3Dwww.google.com")
            driver.implicitly_wait(10)
            time.sleep(2)
            email_enter = driver.find_element(By.XPATH, '//input[@type="email" and @name="loginfmt" and @id="i0116"]')
            email_enter.send_keys(email)
            email_enter.send_keys(Keys.RETURN)
            time.sleep(2)
            if "This Microsoft account does not exist" in text_translated(text_page()):
                microsoft = False
            elif "Enter a valid email address, phone number, or Skype ID" in text_translated(text_page()):
                microsoft = False
            else:
                microsoft = True
        except Exception as e:
            microsoft = f"Error: {e}"
        return microsoft

    def spotify_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Spotify..{blue}")
        try:
            driver.get(r"https://www.spotify.com/fr/signup?flow_id=8f84ffe4-cbe3-481c-99c7-944f17ec3405%3A1715044537&forward_url=https%3A%2F%2Faccounts.spotify.com%2Ffr%2Fstatus")
            driver.implicitly_wait(10)
            time.sleep(2)
            email_enter = driver.find_element(By.XPATH, '//input[@id="username" and @type="email" and @autocomplete="username"]')
            email_enter.send_keys(email)
            email_enter.send_keys(Keys.RETURN)
            time.sleep(1)
            try:
                if "COOKIE" in text_translated(text_page()):
                    driver.execute_script('document.getElementById("onetrust-accept-btn-handler").click();')
            except:
                pass
            time.sleep(1)
            if "This address is already linked to an existing account" in text_translated(text_page()):
                spotify = True
            elif "This email address is invalid" in text_translated(text_page()):
                spotify = False
            else:
                spotify = False
        except Exception as e:
            spotify = f"Error: {e}"
        return spotify

    def pornhub_search():
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search in Pornhub..{blue}")
        try:
            driver.get(r"https://fr.pornhub.com/signup")
            driver.implicitly_wait(10)
            time.sleep(2)
            email_enter = driver.find_element(By.ID, 'createEmail')
            email_enter.send_keys(email)
            email_enter.send_keys(Keys.RETURN)
            time.sleep(2)
            if "Incorrect email format" in text_translated(text_page()):
                pornhub = False 
            elif "Email already taken" in text_translated(text_page()):
                pornhub = True
            else:
                pornhub = False
        except Exception as e:
            pornhub = f"Error: {e}"
        return pornhub

    Slow(f"""
{BEFORE + current_time_hour() + AFTER} {INFO} The email "{white}{email}{red}" was found:

    {INFO_ADD} Spotify   : {white}{spotify_search()}{red}
    {INFO_ADD} Snapchat  : {white}{snapchat_search()}{red}
    {INFO_ADD} Instagram : {white}{instagram_search()}{red}
    {INFO_ADD} Pornhub   : {white}{pornhub_search()}{red}
    {INFO_ADD} Twitter   : {white}{twitter_search()}{red}
    {INFO_ADD} Google    : {white}{google_search()}{red}
    {INFO_ADD} Microsoft : {white}{microsoft_search()}{red}
    """)

    driver.quit()

    Continue()
    Reset()
except Exception as e:
    Error(e)