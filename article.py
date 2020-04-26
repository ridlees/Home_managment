# -*- coding: UTF-8 -*-

#Created by Martin Kodada, 30.06.2019

#Used frameworks

import requests
from bs4 import BeautifulSoup
import time
import re

URL = 'https://www.eurozine.com/essays/'
URLR = 'https://www.respekt.cz/politika'
URLRe = 'https://www.reflex.cz/kategorie/2984/komentare'
URLG = "https://www.theguardian.com/world"
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}

def euro():
    page = requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    Articles = soup.find_all('article')
    readable = Articles[0].text.replace("\n\n","")
    link =  Articles[0].find("a")["href"]
    text = link +"\n\n" + readable
    return text

def guardian():
    page = requests.get(URLG, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    Articles = soup.findAll("h3", {"class": "fc-item__title"})
    readable = Articles[0].text.replace("\n\n","")
    link =  Articles[0].find("a")["href"]
    text = link +"\n\n" + readable
    return text

def respekt():
    page = requests.get(URLR, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    Articles = soup.find_all('article')
    readable = Articles[0].text.replace("\n\n","")
    link =  "https://www.respekt.cz/" + Articles[0].find("a")["href"]
    text = link +"\n\n" + readable
    return text
    
def reflex():
    page = requests.get(URLRe, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    Articles = soup.find_all('article')
    readable = Articles[0].text.replace("\n\n","")
    link =  Articles[0].find("a")["href"]
    text = link +"\n\n" + readable
    return text


def Help():
    text="This is Telegram Articles grabber \n Use /ar euro \n Use /ar reflex \n Use /ar guardian \n Use /ar respekt"
    return text

def select(arg):
    text = ""
    if "help" in arg:
         text = text + Help() + "\n\n"
    if "respekt" in arg:
        text = text + respekt() + "\n\n"
    if "guardian" in arg:
        text = text + guardian() + "\n\n"
    if "euro" in arg:
        text = text + euro() + "\n\n"
    if "reflex" in arg:
        text = text + reflex() + "\n\n"
    if text == "":
        text = "arguments are wrong, check /ar help"
    return text
        
    
