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
sleep(2)
s1.deselect_by_index(1)# 通过index，取消选择第二项选项：o1
sleep(2)
s1.select_by_value("o2")
sleep(2)
s1.deselect_by_value("o2") # 通过value值，取消选择value="o2"的项
sleep(2)
s1.select_by_visible_text("o3")
sleep(2)
s1.deselect_by_visible_text("o3") # 通过可见text，取消选择text="o3"的值，
sleep(2)
s1.select_by_index(1)
s1.select_by_index(2)
s1.select_by_index(3)
sleep(2)
s1.deselect_all() # 取消选择上面选中的3个选项
sleep(2)
driver.quit()
