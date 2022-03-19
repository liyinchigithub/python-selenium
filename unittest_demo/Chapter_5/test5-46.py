from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.find_element_by_id('kw').send_keys('storm') # 输入文字
sleep(3)
driver.quit()