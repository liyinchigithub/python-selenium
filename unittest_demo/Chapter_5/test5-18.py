# 导入webdriver包
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 点击百度首页上右上角，“新闻”链接
ele = driver.find_element_by_link_text("新闻")
ele.click() # 点击该超链接
sleep(2)
# 释放浏览器，关闭浏览器
driver.quit()