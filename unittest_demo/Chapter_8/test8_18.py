from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml8_3.html'
driver.get(html_file)
driver.find_element_by_name('b1').click()

try:
    ele1 = WebDriverWait(driver, 10).until(EC.alert_is_present())
    sleep(2)
    print(ele1)
    print(type(ele1))
    ele1.accept()
    # driver.switch_to.alert.accept()
    sleep(2)
except Exception as e:
    raise e
finally:
    driver.quit()