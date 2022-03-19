from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/clicks.htm")
ele = driver.find_element_by_xpath('/html/body/form/input[2]')
sleep(2)
# 通过double_click()来模拟鼠标左键双击的动作
ActionChains(driver).double_click(ele).perform()
sleep(3)
driver.quit()