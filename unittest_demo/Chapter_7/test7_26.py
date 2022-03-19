from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
a = driver.get_screenshot_as_base64()  # 当前窗口截图，输入截图对应base64的字符信息
print(type(a))
print(a)
driver.quit()