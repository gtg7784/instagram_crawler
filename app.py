import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import json
import time

url = "https://www.instagram.com/"
url_login = "https://www.instagram.com/accounts/login/"
url_hashtag = "https://www.instagram.com/explore/tags/"

hashtag_list = ["streetlook", "amekajilook", "dandylook", "casuallook"]

username = ""
password = "!"

selector = "#react-root > section > main > article > div > div > div > div > a > div > div > img"

base_path = os.path.dirname(os.path.abspath(__file__))

data_json = {}
data_list = []

driver = webdriver.Chrome("./driver/chromedriver")

driver.implicitly_wait(3)

driver.get(url_login)

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()

for index, item in enumerate(hashtag_list):
        driver.get(url_hashtag + item)

        for i in range(100):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(.5)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        image_div = soup.select(selector)

        for i in image_div:
                print(i, end="\n\n")
                data_list.append(i.get('src'))
        
        data_json.update({item: data_list})

        data_list = []
        
with open("data.json", "w") as f:
        f.write(json.dumps(data_json, sort_keys=True, indent=4))
