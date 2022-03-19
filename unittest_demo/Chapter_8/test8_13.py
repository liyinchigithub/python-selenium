from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml8_2.html'
driver.get(html_file)
ele = driver.find_element_by_id('id1')
ele.click()

try:
    ele1 = WebDriverWait(driver, 10).until(EC.element_to_be_selected(ele))
    sleep(2)
    print(ele1)
    print(type(ele1))
except Exception as e:
    raise e
finally:
    driver.quit()