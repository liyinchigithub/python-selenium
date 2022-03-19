from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
try:
    ele = WebDriverWait(driver, 10).until(EC.url_contains('www.baidu.com/')) #检查url是否包含
    # ele = WebDriverWait(driver,10).until((EC.url_matches('www.baidu.com/'))) # 检查包含
    # ele = WebDriverWait(driver, 5).until(EC.url_to_be("https://www.baidu.com/")) # 检查完全匹配
    # ele = WebDriverWait(driver, 5).until(EC.url_changes("https://www.baidu.com/a")) # 检查不完全匹配
    print(ele)
    print(type(ele))
except Exception as e:
    raise e
finally:
    driver.quit()