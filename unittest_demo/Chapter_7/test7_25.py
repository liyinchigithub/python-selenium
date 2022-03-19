from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
a = driver.get_screenshot_as_png()  # 截图，返回截图文件的二进制数据
print(type(a))
print(a)
driver.quit()