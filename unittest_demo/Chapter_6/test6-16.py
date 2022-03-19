from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-3.html'
driver.get(html_file)
s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select
res = s1.is_multiple # 返回True或False
print("该下拉列表是否multiple：{}".format(res))
sleep(2)
driver.quit()
