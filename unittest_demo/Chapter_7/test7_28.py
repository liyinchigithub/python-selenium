from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.find_element_by_id('su').screenshot('d:\\A\\button.png') # 定位元素，然后截图
driver.quit()