from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.sogou.com/')
driver.find_element_by_id('query').send_keys('storm')
sleep(1)
sercont = driver.find_element_by_xpath('//*[@id="vl"]/div[1]/ul/li[2]').click() # li[2]选择第二项
sleep(5)
driver.quit()
