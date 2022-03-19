from selenium import webdriver

url = 'http://www.baidu.com/'
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)
print(len(driver.get_cookies()))  # 删除前cookies数量
driver.delete_all_cookies()
print(len(driver.get_cookies()))  # 删除后cookies数量
driver.quit()
