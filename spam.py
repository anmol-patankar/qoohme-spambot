from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import random,time,string
count=1
def BrowserSetup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=options)
BrowserSetup()

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
while True:
    driver.get('http://qooh.me/why2jay')
    x=random.uniform(0.0,100000.0)
    time.sleep(0.5)
    text_area= driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div/div[1]/div[2]/form/textarea")
    text_area.send_keys(randomString(20))
    python_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div/div[1]/div[2]/form/input[2]")
    python_button.click()
    print(count)
    count+=1

#d:
#cd test
#python D:\Test\spam.py
