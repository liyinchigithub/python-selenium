from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.implicitly_wait(20)
driver.find_element_by_link_text('登录').click()
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
sleep(2)
driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('Storm')

sleep(3)
driver.quit()
