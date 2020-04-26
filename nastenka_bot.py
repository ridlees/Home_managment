# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import json
import api
def Send(payload):
    
    webhook = api.discord
    headers = {'Content-Type': "application/json;"}
    message = requests.post(webhook,json.dumps(payload), headers=headers)
    if str(message) == "<Response [400]>":
        time.sleep(600)
        Loop()
    

def Loop():
        with open("workfile.txt","r+") as f:
            last_payload = f.read()
            URL = 'https://upol.ff.cuni.cz/category/nastenka/'
    
            page = requests.get(URL)
            board= BeautifulSoup(page.content, 'html.parser')
            item = board.findAll("div", {"class": "article-info"})
            h3 = item[0].findAll("h3")[0].text
            p = item[0].findAll("p")[0].text
            a = item[0].findAll("a")[0].get("href")
            payload = {
"content": f"**{h3}**\n{a}\n{p}"
    }
            if a != last_payload:
                Send(payload)
                f.write(a)
                return(payload)

                
if __name__ == '__main__':
    
    import api
    payload = {
            'chat_id': api.cid,
            'text': Loop()
            'parse_mode': 'HTML'
        }
    requests.post(f"https://api.telegram.org/bot{api.api}/sendMessage",data=payload)

        
    
    

