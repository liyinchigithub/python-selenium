from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

try:
    ele = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.ID, 'kw')))
    # ele = WebDriverWait(driver, 5).until(EC.visibility_of_any_elements_located((By.TAG_NAME, 'input')))
    print(ele)
    print(len(ele))
    print(type(ele))
except Exception as e:
    raise e
finally:
    driver.quit()