from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/clicks.htm')
sleep(3)
ele = driver.find_element_by_xpath('/html/body/ul/li/a/label/input')
print(ele.is_selected()) # 判断复选框是否选中，否，返回False
ele.click()              # 点击，使复选框处于选中状态
print(ele.is_selected()) # 判断复选框是否选中，是，返回True
driver.quit()