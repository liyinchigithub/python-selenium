from selenium import webdriver

url = 'http://www.baidu.com/'
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)
baidu_id_cookie = driver.get_cookie('BAIDUID') # 获取'BAIDUID'cookie
print(type(baidu_id_cookie))  # 打印类型
print(baidu_id_cookie) # 打印值
driver.quit()
