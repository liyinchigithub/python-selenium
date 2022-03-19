from selenium import webdriver
from time import sleep
import json

'''
该文件用来保存cookie
'''
driver = webdriver.Chrome()
driver.get('http://mail.163.com/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id('switchAccountLogin').click()
driver.switch_to.frame(0)   #然后切到这个 iframe 页面
driver.find_element_by_name('email').send_keys('apitest333@163.com')
driver.find_element_by_name('password').send_keys('abcd1234')
driver.find_element_by_id('dologin').click()
sleep(3)
mycookies = driver.get_cookies()  # 获取全部cookie
jsoncookies = json.dumps(mycookies) # 转换成json
with open("mycookie.json", 'w') as f: # 保存到文件
    f.write(jsoncookies)
driver.quit()