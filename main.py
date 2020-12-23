from selenium import webdriver
import requests
import time

pageurl = 'https://www.google.com/recaptcha/api2/demo'

driver = webdriver.Chrome(executable_path=r'chromedriver_win32\chromedriver.exe')
driver.get(pageurl)
site_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"

with open(r"api_key.txt", "r") as f:
  api_key = f.read()

form = {"method": "userrecaptcha",
        "googlekey": site_key,
        "key": api_key,
        "pageurl": pageurl,
        "json": 1}

response = requests.post('http://2captcha.com/in.php', data=form)
request_id = response.json()['request']
