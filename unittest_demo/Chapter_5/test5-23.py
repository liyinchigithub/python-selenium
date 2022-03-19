from selenium import webdriver
from selenium.webdriver.common.by import By# 导入By
from time import sleep

driver = webdriver.Chrome()
driver.get('D:\\Love\\Chapter-4\\4-2\\test4-2-4.html')
# 通过引入common.by的包，可以完美支持前面讲过的八种方法
# driver.find_element(By.ID,'myid').send_keys('id') # 支持id
# driver.find_element(By.NAME, 'myname').send_keys('name') # 支持name
# driver.find_element(By.XPATH,'//*[@id="myid"]').send_keys('xpath') # 支持xpath
driver.find_element(By.TAG_NAME,'input').send_keys('tag name') # 支持tag name
sleep(3)
driver.quit()