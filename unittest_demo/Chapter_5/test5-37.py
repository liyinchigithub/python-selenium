from selenium import webdriver
from time import sleep
import os

"""
判断页面元素是否可见
"""
driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-13.html'
driver.get(html_file)
ele1 = driver.find_element_by_id('div1')
ele2 = driver.find_element_by_id('div2')
ele3 = driver.find_element_by_id('div3')
ele4 = driver.find_element_by_id('div4')

# 判断页面元素是否可见，is_displayed()
# 对于style="display: none;style="visibility: hidden;页面不可见
print("ele1 is display: {}".format(ele1.is_displayed()))
print("ele2 is display: {}".format(ele2.is_displayed()))
print("ele3 is display: {}".format(ele3.is_displayed()))
print("ele4 is display: {}".format(ele4.is_displayed()))

driver.find_element_by_id('button1').click()
driver.find_element_by_id('button2').click()
print("————————————————")

print("ele1 is display: {}".format(ele1.is_displayed()))
print("ele2 is display: {}".format(ele2.is_displayed()))
print("ele3 is display: {}".format(ele3.is_displayed()))
print("ele4 is display: {}".format(ele4.is_displayed()))

driver.quit()