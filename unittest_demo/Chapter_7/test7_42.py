from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options = options)
driver.get('https://www.baidu.com/')
sleep(2)
driver.quit()