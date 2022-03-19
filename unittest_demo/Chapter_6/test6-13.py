from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-3.html'
driver.get(html_file)
s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select
sleep(2)
all_options = s1.options
for i in range(0,len(all_options)): # 通过len方法取得选项数量，通过range将其变为一个整数列表
    s1.select_by_index(i)
sleep(2)
driver.quit()
