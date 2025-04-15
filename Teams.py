import requests
import json

# URL tvého Teams webhooku
WEBHOOK_URL = 'https://ssinfis.webhook.office.com/webhookb2/c81b2ea5-0c5d-4fdf-a98a-17ec4637b77c@1543f07f-30f9-407a-9eb5-8a7aec418fff/IncomingWebhook/9d608fd5bbb849f18cf8c132f77f469d/a2ec5848-53df-4ac2-a471-ec402a2dd3f8/V2WCNZkQ0_N6zH6id_pRB8L01OLjiXs_dOgqCSAA2hwmk1'

# Tvoji zprávu
message = {
    "text": "Ahoj, toto je testovací zpráva z Pythonu na Microsoft Teams!"
}

# Odeslání POST požadavku na Teams Webhook
response = requests.post(WEBHOOK_URL, data=json.dumps(message), headers={'Content-Type': 'application/json'})

# Kontrola, zda byla zpráva úspěšně odeslána
if response.status_code == 200:
    print("Zpráva byla úspěšně odeslána!")
else:
    print(f"Chyba při odesílání zprávy: {response.status_code}")