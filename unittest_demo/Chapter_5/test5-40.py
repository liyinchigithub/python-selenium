from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
ele = driver.find_element_by_link_text('新闻')
ele.click()  # 左键的单击
sleep(2)
driver.quit()