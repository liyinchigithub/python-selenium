from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
ele1 = driver.find_element_by_id('kw')
driver.refresh() # 这里刷新页面
try:
    ele = WebDriverWait(driver, 10).until(EC.staleness_of(ele1))
    sleep(2)
    print(ele)
    print(type(ele))
except Exception as e:
    raise e
finally:
    driver.quit()