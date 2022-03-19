from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('.\\test4-2-4.html') # 绝对路径+HTML文件
ele = driver.find_element_by_class_name('myclass') # 通过class name定位元素
ele.send_keys('storm')
sleep(2)
driver.quit()