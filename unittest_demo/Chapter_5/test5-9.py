from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
url = driver.current_url # 获取当前页面URL
print(url)
driver.quit()