from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('Storm')
if driver.find_element_by_id('kw').text == "storm":
    pass
else:
    driver.save_screenshot('d:\\A\\a.png')
driver.quit()