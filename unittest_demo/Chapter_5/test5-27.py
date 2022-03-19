from selenium import webdriver
import os

'''
通过父元素定位子元素
'''
driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-2.html'
driver.get(html_file)
mytext = driver.find_element_by_xpath("//div[@id='B']/div").text
print(mytext)
driver.quit()