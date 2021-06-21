import requests
import discord
import urllib3
from discord import Webhook, RequestsWebhookAdapter
from time import sleep


WEBHOOK_ID = '837170084853317632'
WEBHOOK_TOKEN = 'IIMM3kaqkCTo00wsBoFoZ0fIbzLexYFxMkrcaByZRCLsdktoi5PoyU6JoViASlSNe_Yc'
webhook_URL = 'https://discord.com/api/webhooks/837170084853317632/IIMM3kaqkCTo00wsBoFoZ0fIbzLexYFxMkrcaByZRCLsdktoi5PoyU6JoViASlSNe_Yc'




api_key = '#####'
testurl = 'https://api.bestbuy.com/v1/products((search=squadrons))?apiKey=dGhkpuFjamBybnaKftrxRitU&sort=onlineAvailability.asc&show=name,addToCartUrl,onlineAvailability&format=json'

def check():
    url = f'https://api.bestbuy.com/v1/products((search=nvidia&search=3070fe))?apiKey={api_key}&sort=description.asc&show=onlineAvailability,addToCartUrl,shortDescription,url&format=json'
    try:
        items = requests.get(url)
        items.raise_for_status()
    except:
        raise
    return items.json()

for i in check()['products']:
    print(i)

def check_status():
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())

    for item in check()['products']:
        if item['onlineAvailability'] == True:
            msg = '<@&850583388486238209>', item['name'],'is available!', item['addToCartUrl']
            webhook.send(str(msg))
            print(item['name'],'is available!', item['addToCartUrl'])
    return


def ps5_check():
    ps5_url = 'https://api.bestbuy.com/v1/products((search=nvidia&search=3080fe))?apiKey='+api_key+'&sort=onlineAvailability.asc&show=onlineAvailability,sku,name,addToCartUrl&format=json'
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
            msg = '<@&850583388486238209>', item['name'], 'is available!', item['addToCartUrl']
            webhook.send(str(msg))
            print(item['name'], 'is available!', item['addToCartUrl'])
    return




def xbox_check():
    xbox_url = 'https://api.bestbuy.com/v1/products((search=6419029))?apiKey='+api_key+'&sort=onlineAvailability.asc&show=onlineAvailability,sku,name,addToCartUrl&format=json'
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
            msg = "<@&850583388486238209>", item['name'], 'is available!', item['addToCartUrl']
            webhook.send(fuck me man >:(((()
            print(item['name'], 'is available!', item["addToCartUrl"])

    return






