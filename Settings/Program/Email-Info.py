from Config.Util import *
from Config.Config import *
try:
   import dns.resolver
   import requests
   import re
except Exception as e:
   ErrorModule(e)

Title("Email Info")

def get_email_info(email):
    info = {}
    try:
        domain_all = email.split('@')[-1]
    except:
        domain_all = None

    try:
        name = email.split('@')[0]
    except:
        name = None

    try:
        domain = re.search(r"@([^@.]+)\.", email).group(1)
    except:
        domain = None
    try:
        tld = f".{email.split('.')[-1]}"
    except:
        tld = None

    try:
        mx_records = dns.resolver.resolve(domain_all, 'MX')
        mx_servers = [str(record.exchange) for record in mx_records]
        info["mx_servers"] = mx_servers
    except dns.resolver.NoAnswer:
        info["mx_servers"] = None
    except dns.resolver.NXDOMAIN:
        info["mx_servers"] = None


    try:
        spf_records = dns.resolver.resolve(domain_all, 'SPF')
        info["spf_records"] = [str(record) for record in spf_records]
    except dns.resolver.NoAnswer:
        info["spf_records"] = None
    except dns.resolver.NXDOMAIN:
        info["spf_records"] = None

    try:
        dmarc_records = dns.resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
        info["dmarc_records"] = [str(record) for record in dmarc_records]
    except dns.resolver.NoAnswer:
        info["dmarc_records"] = None
    except dns.resolver.NXDOMAIN:
        info["dmarc_records"] = None

    if mx_servers:
        for server in mx_servers:
            if "google.com" in server:
                info["google_workspace"] = True
            elif "outlook.com" in server:
                info["microsoft_365"] = True

    try:
        response = requests.get(
            f"https://api.mailgun.net/v4/address/validate?address={email}",
            auth=("api", "YOUR_MAILGUN_API_KEY")
        )
        data = response.json()
        info["mailgun_validation"] = data
    except Exception as e:
        info["mailgun_validation"] = {"error": str(e)}

    return info, domain_all, domain, tld, name

email = input(f"\n{INPUT} Email -> {reset}")
print(f"{color.RED}{WAIT} Information Recovery..{reset}")
info, domain_all, domain, tld, name = get_email_info(email)

try:
    mx_servers = info["mx_servers"]
except Exception as e:
    mx_servers = None

try:
    spf_records = info["spf_records"]
except:
    spf_records = None

try:
    dmarc_records = info["dmarc_records"]
except:
    dmarc_records = None

try:
    google_workspace = info["google_workspace"]
except:
    google_workspace = None

try:
    mailgun_validation = info["mailgun_validation"]
except:
    mailgun_validation = None

print(f"""
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Email      : {color.WHITE}{email}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Name       : {color.WHITE}{name}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Domain     : {color.WHITE}{domain}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Tld        : {color.WHITE}{tld}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Domain All : {color.WHITE}{domain_all}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Servers    : {color.WHITE}{mx_servers}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Spf        : {color.WHITE}{spf_records}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Dmarc      : {color.WHITE}{dmarc_records}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Workspace  : {color.WHITE}{google_workspace}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Mailgun    : {color.WHITE}{mailgun_validation}{color.RED}
{color.RESET}""")



