from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
ele = driver.find_element_by_link_text("地图")
print(ele.text) # 获取元素本身的文字，夹在tag中间的文字。夹在<a> </a>中间的文字
driver.quit()