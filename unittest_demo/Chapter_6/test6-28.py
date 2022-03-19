from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-10.html'
driver.get(html_file)
driver.find_element_by_name('b1').click() # 点击按钮打开Confirm弹窗
sleep(2)
print(driver.switch_to.alert.text) # 打印Confirm弹窗文字
sleep(2)
driver.switch_to.alert.accept() # 点击Confirm弹窗上的确定按钮
sleep(2)
driver.find_element_by_name('b1').click() # 点击按钮打开Confirm弹窗
sleep(1)
driver.switch_to.alert.dismiss() # 点击Confirm弹窗上的取消按钮
sleep(2)
driver.quit()