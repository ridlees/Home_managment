# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import os

def ScrapPVKAjax(url,headers,Address):
    page = requests.get(url, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    lisT = soup.findAll("p", {"class": "list"})
    if  lisT[0].text.find(Address) != -1:
        SendAlert()

def ScrapPVK(Address):
    URL = "https://www.pvk.cz/aktuality/havarie-vody/aktualni-havarie/"
    subURL = "https://www.pvk.cz"
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}

    page = requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    rows = soup.findAll("div", {"class": "hrow"})
    ''' Input example
    <div class="hrow">
    <div class="hcol hcol-s">Praha-Lysolaje<span class="hnoweb hyesmob">, </span></div>
    <div class="hcol hcol-s">Lysolaje<span class="hnoweb hyesmob">, </span></div>
    <div class="hcol hcol-s">Lysolajské údolí 92/68</div>
    <div class="hcol"><strong class="hnoweb hyesmob">Přehled výluk zásobování: </strong>-</div>
    <div class="hcol"><strong class="hnoweb hyesmob">Přehled náhradního zásobování: </strong>-</div>
    <div class="hcol hsm"><strong class="hnoweb hyesmob">Upřesnění: </strong>předpoklad do 15:00</div>
    </div>
    '''
    for row in rows[1:len(rows)]:
        a = row.findAll("div", {"class": "hcol"})[3].findAll("a")
        try:
            link = a[0].get("href")
            url = subURL + link
            ScrapPVKAjax(url,headers,Address)
            
        except:
            print("")
            
        if row.text.find(Address) != -1:
            return('Alert - Waterbroke')

if __name__ == '__main__':
    
    import api
    payload = {
            'chat_id': api.cid,
            'text': ScrapPVK("Tuchorazská 426/9"),
            'parse_mode': 'HTML'
        }
    requests.post(f"https://api.telegram.org/bot{api.api}/sendMessage",data=payload)

        
    
    
