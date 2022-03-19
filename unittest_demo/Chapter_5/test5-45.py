from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
source = driver.find_element_by_xpath('//*[@id="dragger"]')
target = driver.find_element_by_xpath('/html/body/div[5]')

sleep(2)
# 通过drag_and_drop()模拟鼠标的拖拽动作
ActionChains(driver).drag_and_drop(source, target).perform()

sleep(3)
driver.quit()