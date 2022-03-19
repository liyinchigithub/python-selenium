from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('Storm')
try:
    ele = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'kw'), 'Storm'))
    sleep(2)
    print(ele)
    print(type(ele))
except Exception as e:
    raise e
finally:
    driver.quit()