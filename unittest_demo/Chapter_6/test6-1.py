from selenium import webdriver
from time import sleep

'''
输入框常见操作
'''
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
#定位百度搜索框
ele = driver.find_element_by_id('kw')
ele.send_keys('storm') # 输入内容send_keys()
sleep(2)
ele.clear() # 清除输入框中的内容clear()
sleep(2)
ele.send_keys('storm') # 再次输入内容send_keys()
print(ele.get_property('value')) # 获取输入框中的内容:get_property('value')
print(ele.get_attribute('name')) # 获取元素的属性:get_attribute()
print(ele.tag_name) # 获取元素的tagname:tag_name
sleep(3)
driver.quit()