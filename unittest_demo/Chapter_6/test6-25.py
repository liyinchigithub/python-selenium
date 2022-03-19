from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-8.html'
driver.get(html_file)
ele = driver.find_element_by_xpath('//*[@id="another"]/iframe') # 定位iframe元素
driver.switch_to.frame(ele) # 直接传递元素
driver.find_element_by_id('kw').send_keys('storm')
sleep(2)
driver.quit()