from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import os

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/php/fileUpload.htm")
sleep(2)
ele = driver.find_element_by_id('file')
ActionChains(driver).click(ele).perform()
sleep(2)
os.system('D:\\A\\upload.exe')
sleep(3)
driver.quit()


