from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
ele = driver.find_element_by_xpath('//*[@id="kw"]') # 通过xpath定位搜索框
ele.send_keys('storm')
sleep(2)
# 释放浏览器，关闭浏览器
driver.quit()