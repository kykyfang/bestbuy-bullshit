from discord import Webhook, RequestsWebhookAdapter
import requests
from datetime import datetime


WEBHOOK_ID = 783790355803799622
WEBHOOK_TOKEN = 'Ec_rg_52vUHYql2a4h5x2R2rT-Ptfs58Zxx57EBc3cNfwoXnh1gYsDuVrF6BGCtT85yP'
webhook_URL = 'https://discord.com/api/webhooks/783790355803799622/Ec_rg_52vUHYql2a4h5x2R2rT-Ptfs58Zxx57EBc3cNfwoXnh1gYsDuVrF6BGCtT85yP'



webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())


api_key = 'N5yCPpxI8mL0cAnaz6AFsyLI'

def check():
    testurl = 'https://api.bestbuy.com/v1/products((search=squadrons))?apiKey=N5yCPpxI8mL0cAnaz6AFsyLI&sort=onlineAvailability.asc&show=name,addToCartUrl,onlineAvailability&format=json'
    try:
        items = requests.get(testurl)
        items.raise_for_status()
    except:
        raise
    return items.json()

def check_status():
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())

    for item in check()['products']:
        if item['onlineAvailability'] == True:
            msg = '@everyone', item['name'],'IS AVAILABLE!!!!!!', item['addToCartUrl']
            webhook.send(str(msg))
            print(item['name'],'IS AVAILABLE!!!!!!', item['addToCartUrl'])
    return

print(datetime.now().strftime('%m-%d-%y %H:%M'))