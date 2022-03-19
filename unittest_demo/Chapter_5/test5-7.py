from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
pos = driver.get_window_position() # 获取窗口的位置
print(pos)
sleep(2)
driver.set_window_position(500,300) # 设置窗口的位置
sleep(2)
print(driver.get_window_position()) # 再次打印窗口位置
driver.quit()