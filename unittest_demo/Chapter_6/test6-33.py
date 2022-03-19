from selenium import webdriver
from time import sleep
import os

chromeOptions = webdriver.ChromeOptions() # 定义变量，存储Chrome设置项
prefs = {"download.default_directory": "D:\\A\\"}  # 指定默认下载目录
chromeOptions.add_experimental_option("prefs", prefs) # 将prefs定义的下载目录设置装填到浏览器设置
driver = webdriver.Chrome(chrome_options=chromeOptions) # 以自定义的设置项启动浏览器
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-13.html'
driver.get(html_file)
sleep(2)
driver.find_element_by_tag_name('a').click()
sleep(5)
driver.quit()
