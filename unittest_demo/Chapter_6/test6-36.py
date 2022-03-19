from selenium import webdriver
from time import sleep
import os
from Chapter_6.get_file_md5 import get_md5

if os.path.exists("D:\\A\\storm.rar"): # 先判断文件是否存在
    os.remove("D:\\A\\storm.rar")      # 如果存在删除

chromeOptions = webdriver.ChromeOptions() # 定义变量，存储Chrome设置项
prefs = {"download.default_directory": "D:\\A\\"}  # 指定默认下载目录
chromeOptions.add_experimental_option("prefs", prefs) # 将prefs定义的下载目录设置装填到浏览器设置
driver = webdriver.Chrome(chrome_options=chromeOptions) # 以自定义的设置项启动浏览器
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-13.html'
driver.get(html_file)
sleep(2)
driver.find_element_by_tag_name('a').click()
sleep(5)  # 等待下载完成，然后再去判断文件是否存在
if os.path.exists("D:\\A\\storm.rar"): # 先判断文件是否存在
    file_md5 = get_md5("D:\\A\\storm.rar")
    if file_md5=="6c17852b255374e8d9dc7c7c6a8c2b0d":
        print('下载文件的md5值正确')
driver.quit()
