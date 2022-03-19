# 要使用webdriver提供的API，首先要导入包
from selenium import webdriver
from time import sleep

# 定义一个变量，用来存储实例化后的浏览器，这里打开Chrome浏览器
driver1 = webdriver.Chrome()
sleep(2) # 这里等待2秒钟，看效果
# 关闭Chrome浏览器
driver1.close() # 关闭当前浏览器窗口
# 定义一个变量driver2，用来打开Firefox浏览器
driver2 = webdriver.Firefox()
sleep(2)
driver2.quit() # 退出浏览器进程

