from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(2)
driver.maximize_window()  #最大化
sleep(2)
driver.minimize_window()  #最小化
sleep(2)
driver.quit()