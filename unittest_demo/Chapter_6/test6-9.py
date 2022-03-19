from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
ele = driver.find_element_by_link_text('新闻')
print(ele.text)
ele.click()
sleep(2)
driver.quit()