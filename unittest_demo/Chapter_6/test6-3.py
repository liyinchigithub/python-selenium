from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('storm')
driver.find_element_by_id('su').submit() # 对于submit按钮，可以使用submit方法
sleep(2)
driver.quit()