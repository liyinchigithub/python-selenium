from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
ele = driver.find_element_by_css_selector('#kw') # 通过css来定位元素
ele.send_keys('storm')
sleep(2)
driver.quit()