from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# 通过get方法访问网址，这里访问人民邮电出版社官网
driver.get('https://www.ptpress.com.cn/')
sleep(2)
driver.quit()