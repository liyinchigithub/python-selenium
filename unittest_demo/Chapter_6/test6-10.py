from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-2.html'
driver.get(html_file)
s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select
sleep(2)
s1.select_by_index(1)  # 通过index，选择第二项选项：o1
sleep(2)
s1.select_by_value("o2")  # 通过value值，选择value="o2"的项
sleep(2)
s1.select_by_visible_text("o3")  # 通过可见text，选择text="o3"的值，即在下拉时我们可以看到的文本
sleep(2)
driver.quit()
