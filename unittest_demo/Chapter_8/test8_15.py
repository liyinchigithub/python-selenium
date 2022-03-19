from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7_6.html'
driver.get(html_file)
ele = driver.find_element_by_id('id1')
ele.click()

try:
    # ele1 = WebDriverWait(driver, 10).until(EC.element_located_selection_state_to_be((By.ID, 'id1'), is_selected=True))
    ele1 = WebDriverWait(driver, 10).until(EC.element_selection_state_to_be(ele, is_selected=True))
    sleep(2)
    print(ele1)
    print(type(ele1))
except Exception as e:
    raise e
finally:
    driver.quit()