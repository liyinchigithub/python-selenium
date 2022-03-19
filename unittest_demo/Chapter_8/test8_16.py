from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

try:
    ele1 = WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))
    sleep(2)
    print(ele1)
    print(type(ele1))
except Exception as e:
    raise e
finally:
    driver.quit()