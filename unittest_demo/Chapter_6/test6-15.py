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
mylist = []
all = s1.all_selected_options
for i in all:
    mylist.append(i.text)
print('所有被选中的选项文字是：{}'.format(mylist))
sleep(2)
driver.quit()
