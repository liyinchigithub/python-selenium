from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml6-1.html'
driver.get(html_file)
eles = driver.find_elements_by_name('a') # 通过name定位一组元素
for ele in eles: # 循环读取每个复选框
    ele.click()  # 单击
    sleep(2)

driver.quit()