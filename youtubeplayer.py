from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

def Player(video):
    chromedriver = "/Users/martinkodada/Documents/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.youtube.com/")
    time.sleep(2)
    python_input = driver.find_element_by_id('search')
    python_input.send_keys(video)
    python_input.send_keys(Keys.ENTER)
    time.sleep(3.5)
    duration = driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span')[0].text
    leng = re.findall(r'\d+', duration)
    i = len(leng)
    duration = 0
    for z in range(0, i):
        i = i - 1
        if z == 0:
            square = int(leng[i])
        else:
            z = z - 1
            square = (10**z*60)*int(leng[i])
        print(square)
        duration = duration + square
    driver.find_elements_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')[0].click()
    print(duration)
    time.sleep(duration)
    driver. quit()
arg = ["Callifornia", "Girls", "Katty", "Perry"]
arg = " ".join(arg)
Player("Callifornia Girls Katty")
