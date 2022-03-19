# 导入webdriver包
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 定位百度搜索框
myinput = driver.find_element_by_id('kw')
# 对其进行操作，输入“storm”
myinput.send_keys("storm")
# 等待2秒钟，让你看到输入框确实输入内容了
sleep(2)
# 释放浏览器，关闭浏览器
driver.quit()