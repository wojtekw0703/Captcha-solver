from selenium import webdriver
import requests
import time

#run a website by Google Chrome
pageurl = 'https://www.google.com/recaptcha/api2/demo'
driver = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe")
driver.get(pageurl)

#a unique key that every site has when the reCaptcha is integrated
site_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"

#key from 2captcha that allows me to use API
api_key = "b2e30cda325371e0f3954a1db0af613"

#preparing unnecessary data send to 2captcha (according to guide)
form = {"method": "userrecaptcha",
        "googlekey": site_key,
        "key": api_key,
        "pageurl": pageurl,
        "json": 1}

#sending a 'form'
response = requests.post('http://2captcha.com/in.php', data=form)
#getting the request id
request_id = response.json()['request']
url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

status = 0
while not status:
    #check the result of 2captcha work
    res = requests.get(url)
    if res.json()['status'] == 0:
        time.sleep(1)
    else:
        #if status !=0 then automatically it injects a result to the textarea 'g-recaptcha-response'
        requ = res.json()['request']
        js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
        driver.execute_script(js)
        driver.find_element_by_id("recaptcha-demo-submit").submit()
        status = 1
