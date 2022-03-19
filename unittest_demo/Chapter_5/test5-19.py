from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 点击百度首页上右上角，“新闻”链接
ele = driver.find_element_by_partial_link_text("闻")#  html 链接元素 <a>新闻</a> 文字部分匹配
ele.click() # 点击该超链接
sleep(2)
# 释放浏览器，关闭浏览器
driver.quit()