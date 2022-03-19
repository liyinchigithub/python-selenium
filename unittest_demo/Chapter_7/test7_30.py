from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
ele1JS = "document.getElementById('kw').value='storm'"
ele2JS = "document.getElementById('su').click()"
driver.execute_script(ele1JS)
sleep(3)
driver.execute_script(ele2JS)
sleep(3)
driver.quit()
