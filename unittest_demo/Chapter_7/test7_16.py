from selenium import webdriver

url = 'http://www.baidu.com/'
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)
cur_cookies = driver.get_cookies()
print(type(cur_cookies)) # 打印返回值类型——列表
print(type(cur_cookies[0])) # 打印单个cookie类型——字典
print(len(cur_cookies))  # 打印cookie的数量
print(cur_cookies) # 打印cookie值
driver.quit()
