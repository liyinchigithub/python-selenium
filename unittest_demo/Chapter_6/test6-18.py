from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''
1、Firefox成功，Chrome失败；
2、Firefox打开本地文件的话，要加"File:///"
'''
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-5.html'
driver.get(html_file)
driver.find_element_by_id('select').send_keys('b')
sleep(3)
driver.find_element_by_id('select').send_keys(Keys.ARROW_DOWN)
sleep(3)
driver.find_element_by_id('select').send_keys(Keys.ENTER)

sleep(5)
driver.quit()