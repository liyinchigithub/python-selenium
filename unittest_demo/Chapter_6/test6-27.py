from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-9.html'
driver.get(html_file)
driver.find_element_by_name('b1').click() # 点击按钮打开Alert弹窗
sleep(1)
print(driver.switch_to.alert.text) # 打印Alert弹窗文字
driver.switch_to.alert.accept() # 点击Alert弹窗上的确定按钮
sleep(2)
driver.quit()