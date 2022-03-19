from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
ele = driver.find_element_by_id('kw')
print(ele.get_property('id'))  # 获取元素id属性值
driver.quit()