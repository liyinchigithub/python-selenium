from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-4.html'
driver.get(html_file)
s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select
s1.select_by_visible_text('   With spaces') # 当text以空格开头时，可以输入多个空格
sleep(2)
s1.deselect_all()
sleep(2)
s1.select_by_visible_text('With spaces')  # 当text以空格开头时，可以不加空格
sleep(2)
s1.select_by_visible_text('abc With spaces') # 当空格在中间时，只加1个空格
sleep(2)
s1.select_by_visible_text('abc   With nbsp') # 有几个nbsp，加几个空格
sleep(2)
driver.quit()
