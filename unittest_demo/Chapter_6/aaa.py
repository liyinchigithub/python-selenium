from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get('https://www.sina.com.cn/')
driver.quit()