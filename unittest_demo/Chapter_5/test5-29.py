from selenium import webdriver
import os

# "由子节点定位父节点"
driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-3.html'
driver.get(html_file)

# 1.xpath: `.`代表当前节点; '..'代表父节点
mytext = driver.find_element_by_xpath("//div[@id='C']/../..").text
print(mytext)

# 2.xpath轴 parent
mytext1 = driver.find_element_by_xpath("//div[@id='C']/parent::div/parent::div").text
print(mytext1)

driver.quit()