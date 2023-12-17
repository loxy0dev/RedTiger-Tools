from Options.Options import *

TitrePage("Webhook Generator + Chekeur")

def send_embed_webhook(webhook_url, embed_content, username=None, url=None):
                payload = {
                'embeds': [embed_content],
                'username': username,
                'avatar_url': url
                 }

                headers = {
            'Content-Type': 'application/json'
             }

                response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
username = 'Red-Tiger'
url = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'


webhook = input(f"{couleur.RED}\nVoulez-vous annoncer un \"Webhook\" valable avec un Webhook ? (y, n) -> {couleur.RESET}")
if webhook in ['y']:
    webhook_url = input(f"{couleur.RED}\nEntrez le lien du Webhook -> {couleur.RESET}")

def send_webhook_message(webhook_url_Essai, content):
         payload = {
             'content': content
         }

         headers = {
             'Content-Type': 'application/json'
          }

         response = requests.post(webhook_url_Essai, data=json.dumps(payload), headers=headers)

         if response.status_code == 204:
             print(f"{couleur.GREEN}[+] | {couleur.CYAN}{webhook_url}{couleur.GREEN} | Webhook Trouvé | Tentative n°{nombre}{couleur.RESET}")

             embed_content = {
           'title': f'Webhook Trouvé, tentative n°{nombre}',
           'description': f"**__Lien Webhook:__**\n```{webhook_url}```\nIl se peut que le webhook ait été supprimé d'ici là.",
           'color': 0xf00020,
           'footer': {
            "text": "Red-Tiger",
            "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
             }
            }

             send_embed_webhook(webhook_url, embed_content, username, url)

         else:
             print(f"{couleur.RED}[X] | {couleur.CYAN}{webhook_url}{couleur.RED} | Webhook Faux | Tentative n°{nombre}{couleur.RESET}")

nombre = 0
while True:
    nombre += 1
    
    chiffres = ''.join(random.choices(string.digits, k=18))
    caracteres = ''.join(random.choices(string.ascii_letters + string.digits, k=64))

    webhook_partie_variable = f'{chiffres}/{caracteres}'

    webhook_url_Essai = f'https://discord.com/api/webhooks/{webhook_partie_variable}'

    message_content = 'Webhook trouvé By Red Tiger'

    send_webhook_message(webhook_url_Essai, message_content)
    TitrePage(f"Red-Tiger | Ip Générator + Chekeur | Tentative n°{nombre}")