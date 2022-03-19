from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/clicks.htm")
driver.find_element_by_xpath("/html/body/form/input[3]").click()
# driver.find_element_by_xpath("/html/body/form/input[3]").submit()
sleep(2)
text = driver.find_element_by_name("t2").get_attribute('value')
if text == '[CLICK]':
    print('pass')
driver.quit()