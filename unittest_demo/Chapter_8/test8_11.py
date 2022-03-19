from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
try:
    ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, '地图')))
    sleep(2)
    print(ele)
    print(type(ele))
except Exception as e:
    raise e
finally:
    driver.quit()