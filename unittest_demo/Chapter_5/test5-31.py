from selenium import webdriver
import os

"""
哥哥定位弟弟示例
"""

driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-4.html'
driver.get(html_file)

# 1.xpath，通过父节点获取其弟弟节点
mytext = driver.find_element_by_xpath("//div[@id='D']/../div[3]").text
print(mytext)

# 2.xpath轴 following-sibling
mytext1 = driver.find_element_by_xpath("//div[@id='D']/following-sibling::div[1]").text
print(mytext1)

driver.quit()