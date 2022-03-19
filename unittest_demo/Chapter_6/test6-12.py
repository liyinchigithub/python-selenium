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
all_options = s1.options # 返回的是一个列表，列表包括所有选项的元素
print("options的返回值类型：{}".format(type(all_options)))
mylist = [] # 定义一个空列表
for i in all_options:
    mylist.append(i.text)  # 将options的文字存储到mylist这个列表
print('这个下拉列表的选项包括：{}'.format(mylist))

driver.quit()
