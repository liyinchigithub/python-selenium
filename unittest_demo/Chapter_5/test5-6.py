from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
winsize = driver.get_window_size() # 获取当前窗口的大小
print(winsize)
print(type(winsize)) # 打印一下winsize变量的类型
sleep(2)
driver.set_window_size(500,800) # 设置窗口的大小
sleep(2)
driver.quit()