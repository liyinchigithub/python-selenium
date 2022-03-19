from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
ele = driver.find_element_by_id('kw')
print(type(ele)) # webdriverElement
eles = driver.find_elements_by_id('kw')
ele.find_element_by_css_selector()
print(type(eles))
driver.quit()












