# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup


def nevy_all():  #--> API? https://api.nevyhazujto.cz/api/v1/products/40737

    domain = 'https://www.nevyhazujto.cz'
    nevy_elektro ='https://www.nevyhazujto.cz/c/18/1207'
    nevy_sber = 'https://www.nevyhazujto.cz/c/59/1207'
    nevy_knihy = 'https://www.nevyhazujto.cz/c/38/1207'
    
    elektro = parse(get(nevy_elektro,["div","jss137 jss170 jss195"]),"a",False,domain)
    sber =parse(get(nevy_sber,["div","jss137 jss170 jss195"]),"a",False,domain)
    knihy = parse(get(nevy_knihy,["div","jss137 jss170 jss195"]),"a",False,domain)

    text = f'Sber:{sber} \n Knihy:{knihy} \n Elektro:{elektro}'
    return text

def vse_all():

    domain = 'https://vsezaodvoz.cz'
    
    vse_elektro = 'https://vsezaodvoz.cz/inzeraty/elektro?region=14'
    vse_knihy ='https://vsezaodvoz.cz/inzeraty/knihy-a-tiskoviny?region=14'
    vse_sber = 'https://vsezaodvoz.cz/inzeraty/umeni-a-sberatelstvi'

    '''div class="product-inline-item js-item-like-parent"
    alternativně skrz h3 class = product-inline-title v který je rovnou a bez classy
    '''
    sber = parse(get(vse_sber,["h3","product-inline-title"]),"a",False,domain)
    knihy = parse(get(vse_knihy,["h3","product-inline-title"]),"a",False,domain)
    elektro = parse(get(vse_elektro,["h3","product-inline-title"]),"a",False,domain)

    ''' získávání linku na obrázek
    print(get(vse_sber,["img","lazy"]).get("data-original")) 
    '''
    text = f'Sber:{sber} \n Knihy:{knihy} \n Elektro:{elektro}'
    return text

def sbaz_all(): 
    sbaz_knihy = 'https://www.sbazar.cz/hledej/za%20odvoz/31-knihy-literatura/praha'
    sbaz_antik = 'https://www.sbazar.cz/hledej/za%20odvoz/314-antikvariat-stare-tisky/praha'
    sbaz_elektro = 'https://www.sbazar.cz/hledej/za%20odvoz/30-elektro-pocitace/praha'
    
    knihy = parse(get(sbaz_knihy,["a","c-item__link"]),"",True,"")
    sber = parse(get(sbaz_antik,["a","c-item__link"]),"",True,"")
    elektro = parse(get(sbaz_elektro,["a","c-item__link"]),"",True,"")

    text = f'Sber:{sber} \n Knihy:{knihy} \n Elektro:{elektro}'
    return text

def get(url,search):
    freebie = requests.get(url)
    items= BeautifulSoup(freebie.content, 'html.parser')
    item = items.findAll(f"{search[0]}", {"class": f"{search[1]}"})
    return item[0]

def parse(item,arg,isBazar,domain):
    import re
    if  isBazar == True:
        text = item.text
        text = re.split('[\t\n]+', text.strip())
        href = item.get("href")
        return[text,href]
    else:
        link = item.findAll(f"{arg}")
        text = link[0].text
        text = re.split('[\t\n]+', text.strip())
        href = domain + link[0].get("href")
        return [text,href]
    
def Help():
    text = "use \fre sbaz, \fre vse \fre nevy"
    return text

def select(arg):
    text = ""
    if "help" in arg:
         text = text + Help() + "\n\n"
    if "nevy" in arg:
        text = text + nevy_all() + "\n\n"
    if "vse" in arg:
        text = text + vse_all() + "\n\n"
    if "sbaz" in arg:
        text = text + sbaz_all() + "\n\n"
    if text == "":
        text = "arguments are wrong, check /fre help"
    return text

def Get_all():
    return sbaz_all() +"\n"+ vse_all() +"\n"+ nevy_all()
    
if __name__ == '__main__':
    import api
    payload = {
            'chat_id': api.cid,
            'text': Get_all(),
            'parse_mode': 'HTML'
        }
    requests.post(f"https://api.telegram.org/bot{api.api}/sendMessage",data=payload)


    
