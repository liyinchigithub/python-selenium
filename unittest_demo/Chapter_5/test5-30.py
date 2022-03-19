from selenium import webdriver
import os

"""
通过弟弟定位哥哥
"""

driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-4.html'
driver.get(html_file)

# 1.xpath,通过父节点获取其哥哥节点
mytext = driver.find_element_by_xpath("//div[@id='D']/../div[1]").text
print(mytext)

# 2.xpath轴 preceding-sibling
mytext1 = driver.find_element_by_xpath("//div[@id='D']/preceding-sibling::div[1]").text
print(mytext1)

driver.quit()