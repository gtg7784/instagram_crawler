import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.instagram.com/"
url_login = "https://www.instagram.com/accounts/login/"

username = ""
password = ""

selector = "#react-root > section > main > section > div > div > div > article > div.eo2As > div.KlCQn.EtaWk > ul > div > li > div > div > div > h2 > a"

driver = webdriver.Chrome("./driver/chromedriver")

driver.implicitly_wait(3)

driver.get(url_login)

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

image_div = soup.select(selector)

for i in image_div:
    print(i.text)