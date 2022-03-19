from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml8_1.html'
driver.get(html_file)
try:
    ele = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe1")))
    # ele = WebDriverWait(driver, 5).until(EC.visibility_of_any_elements_located((By.TAG_NAME, 'input')))
    driver.find_element_by_id('kw').send_keys('Storm')
    sleep(2)
    print(ele)
    print(type(ele))
except Exception as e:
    raise e
finally:
    driver.quit()