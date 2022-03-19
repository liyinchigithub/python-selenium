from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
pagesource = driver.page_source # 获取页面源码
print(pagesource)
driver.quit()