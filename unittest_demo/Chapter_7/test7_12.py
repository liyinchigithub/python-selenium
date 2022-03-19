from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('Storm')
ele = driver.find_element_by_id('kw')
print(ele.get_attribute('value')) # 获取输入框中的值
driver.quit()