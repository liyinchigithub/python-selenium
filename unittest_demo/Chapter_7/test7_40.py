from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Python\\Python36\\chromedriver.exe')
driver.get('https://www.baidu.com/')
sleep(2)
driver.quit()