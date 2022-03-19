from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
eles = driver.find_elements_by_tag_name('input')
print(len(eles)) # 我们打印一下该页面有多少个input标签
eles[7].send_keys('storm') # 通过下标从list中取单个元素进行操作
sleep(2)
driver.quit()