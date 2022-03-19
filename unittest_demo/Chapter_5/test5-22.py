from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('D:\\Love\\Chapter-4\\4-2\\test4-2-4.html')
# 直接传递locate type的方式只支持4种，id、name、xpath、css
# driver.find_element('id', 'myid').send_keys('id') # 支持id
# driver.find_element('name', 'myname').send_keys('name') # 支持name
# driver.find_element('xpath','//*[@id="myid"]').send_keys('xpath') # 支持xpath
driver.find_element('css','#myid').send_keys('css') # 支持css
# driver.find_element('tagname', 'input').send_keys('input') # 不支持
sleep(3)
driver.quit()