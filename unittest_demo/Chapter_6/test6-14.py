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
s1.select_by_index(1)
s1.select_by_index(2)
s1.select_by_index(3)
first = s1.first_selected_option.text
print('第一个被选中的选项文字是：{}'.format(first))
sleep(2)
driver.quit()
