from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
title = driver.title # 打印当前网页的title，即“百度一下，你就知道”
print(title)
driver.quit()