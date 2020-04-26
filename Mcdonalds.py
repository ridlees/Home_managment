
import requests
from bs4 import BeautifulSoup
import time
import driver

URL = 'https://survey.fast-insight.com/mcd/cz/coupon.php'
URL2 ='https://script.google.com/macros/s/AKfycbxbOwY81lQUa08jX6uyOfu8sJDkuoOJ5qQz_joACzbhue5_6lo/exec'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
proxies = {'http': 'http://159.89.227.145:80', 'https': 'http://35.245.145.147:8080'} #vymyslet, jak je přidat:/
chromedriver = api.driver

def Fries():
    page = requests.post(URL, headers=headers,)
    soup = BeautifulSoup(page.content, 'html.parser')
    Link = soup.find_all('a')
    link =  Link[1]
    text = link.get('href')
    return text
    
def Drink():
    from selenium import webdriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(URL2)
    time.sleep(8)
    driver.switch_to.frame("sandboxFrame")
    driver.switch_to.frame("userHtmlFrame")
    python_button = driver.find_element_by_tag_name('button')
    python_button.click()
    time.sleep(8)
    soup=BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    code = soup.find_all('span')
    text = code[0].text
    return text

def Help():
    text="This is Telegram McDonald's reward system \n Use /mc drink to get drink code \n Use /mc drink to get voucher for fries or pie \n Use /credits to get credits for this app \n If you find any bugs in this app, contact me at dersteppen-wofl@tutanota.com"
    return text

def select(arg):
    text = ""
    if "help" in arg:
         text = text + Help() + "\n\n"
    if "drink" in arg:
        text = text + Drink() + "\n\n"
    if "fries" in arg:
        text = text + Fries() + "\n\n"
    if text == "":
        text = "arguments are wrong, check /mc help"
    return text
        
    
