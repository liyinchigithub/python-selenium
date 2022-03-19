from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/clicks.htm")

ele = driver.find_element_by_xpath('/html/body/ul//input')
ele.click()
sleep(2)
if ele.is_selected():
    print('pass')
sleep(2)
ele.send_keys(Keys.SPACE)  #自己可以手动实验下，按space键，可以选中或取消选中复选框
sleep(2)
driver.quit()