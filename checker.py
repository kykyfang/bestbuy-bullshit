import requests
import discord
from discord import Webhook, RequestsWebhookAdapter
from time import sleep


WEBHOOK_ID = 783757314267938836
WEBHOOK_TOKEN = 'YYySym1ai1F5upjnasGrxXy8GFJ2rvdyPHyqwfqIZA_jR3M7BOx6xJBeENqEwmzFMQkV'
webhook_URL = 'https://discord.com/api/webhooks/783757314267938836/YYySym1ai1F5upjnasGrxXy8GFJ2rvdyPHyqwfqIZA_jR3M7BOx6xJBeENqEwmzFMQkV'




api_key = 'FHJZXw6OmTXkwxaEkgwm4eDN'
testurl = 'https://api.bestbuy.com/v1/products((search=squadrons))?apiKey=dGhkpuFjamBybnaKftrxRitU&sort=onlineAvailability.asc&show=name,addToCartUrl,onlineAvailability&format=json'

def check():
    url = 'https://api.bestbuy.com/v1/products(search=nvidia&search=3060&search=3070)?format=json&show=sku,name,addToCartUrl,onlineAvailability&apiKey=' + api_key
    try:
        items = requests.get(url)
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


def ps5_check():
    ps5_url = 'https://api.bestbuy.com/v1/products((search=6426149))?apiKey='+api_key+'&sort=onlineAvailability.asc&show=onlineAvailability,sku,name,addToCartUrl&format=json'
    try:
        items = requests.get(ps5_url)
        items.raise_for_status()
    except:
        raise
    return items.json()

def ps5_status():
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())

    for item in ps5_check()['products']:
        if item['onlineAvailability'] == True:
            msg = '@everyone', item['name'], 'IS AVAILABLE!!!!!!', item['addToCartUrl']
            webhook.send(str(msg))
            print(item['name'], 'IS AVAILABLE!!!!!!', item['addToCartUrl'])
    return




def xbox_check():
    xbox_url = 'https://api.bestbuy.com/v1/products((search=6428324))?apiKey='+api_key+'&sort=onlineAvailability.asc&show=onlineAvailability,sku,name,addToCartUrl&format=json'
    try:
        items = requests.get(xbox_url)
        items.raise_for_status()
    except:
        raise
    return items.json()

def xbox_status():
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())

    for item in xbox_check()['products']:
        if item['onlineAvailability'] == True:
            msg = '@everyone', item['name'], 'IS AVAILABLE!!!!!!', item['addToCartUrl']
            webhook.send(str(msg))
            print(item['name'], 'IS AVAILABLE!!!!!!', item['addToCartUrl'])

    return






