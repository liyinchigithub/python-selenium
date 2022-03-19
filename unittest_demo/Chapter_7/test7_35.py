from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/iframesTest.htm")
sleep(2)
driver.switch_to.frame(1)
js5 = "window.scrollTo(0,200)"
driver.execute_script(js5)  #向下移动200像素
sleep(2)
driver.quit()