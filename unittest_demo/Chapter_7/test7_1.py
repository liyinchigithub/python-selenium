from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.sogou.com/')

ele1 = driver.find_element_by_id('query')
ele1.click()
sleep(1)
ele1.send_keys(Keys.ARROW_DOWN)
ele1.send_keys(Keys.ARROW_DOWN)
ele1.send_keys(Keys.ARROW_DOWN)
sleep(5)
driver.quit()
