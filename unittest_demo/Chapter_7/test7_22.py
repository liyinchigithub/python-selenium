from selenium import webdriver
import time
import json
from time import sleep

'''
通过导入cookies的方式来实现登录，注意刷新页面；
'''
driver = webdriver.Chrome()
driver.get("http://mail.163.com/")
cookies_file_path = "mycookie.json"
with open(cookies_file_path, "r") as f:   # 读取本地的cookie文件
    cookies_str = f.readline()
    cookies_dict = json.loads(cookies_str)

driver.delete_all_cookies()   # 删除当前网址的所有cookie
for cookie in cookies_dict:  # 循环读取cookie
    for k in cookie.keys():  # 这里要判断一下
        if k == "expiry":
            cookie[k] = int(cookie[k])  # expiry参数必须为整型
    driver.add_cookie(cookie)

time.sleep(2)
driver.refresh()
sleep(5)
driver.quit()