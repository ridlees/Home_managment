# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import json




def Get():
    apikey = '5130e7c307b20224c3186546dcb9a540'
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat=50.489772&lon=14.771335&units=metric&appid={apikey}'
    page = requests.get(url)
    return(Dictionary(page))
def Dictionary(page):
    #creating dictionary out of jason
    newDictionary=json.loads(str(page.text))
    current = newDictionary["current"]
    daily = newDictionary["daily"]
    today = daily[0]["temp"]["min"]
    tomorrow = daily[1]["temp"]["min"]
    if today <= 5.0:
        return("chladno je dnes, odnes rostliny dovnitř")
    elif tomorrow <= 5.0:
        return("chladno je zítra, odnes rostliny dovnitř")
    else:
        return("teplo - jahody mohou být na balkóně")



if __name__ == '__main__':
    import api
    payload = {
            'chat_id': api.cid,
            'text': Get(),
            'parse_mode': 'HTML'
        }
    requests.post(f"https://api.telegram.org/bot{api.api}/sendMessage",data=payload)
