from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw1').send_keys('Storm')
driver.quit()