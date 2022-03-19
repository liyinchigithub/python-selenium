from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/clickCombo.htm")
ele = driver.find_element_by_xpath('/html/body/div/div')
# 按下control键，不松开
ActionChains(driver).key_down(Keys.CONTROL).perform()
# 然后点击
ele.click()
sleep(3)
driver.quit()