from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(2)
driver.get('https://www.ptpress.com.cn/')
driver.quit()