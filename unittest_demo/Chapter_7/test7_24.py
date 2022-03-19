from selenium import webdriver
import os
import time

script_name = os.path.basename(__file__).split('.')[0]
file_name = script_name + '_' + str(time.time()) + '.png'
# print(file_name)
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.save_screenshot(file_name) # 截取当前页面，当前目录，保存成png类型文件
driver.quit()