from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
try:
    eles = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input'))) #检查元素是否找到
    print(len(eles)) # 返回列表中包含几个元素
    print(type(eles)) # 返回值类型
    print(eles) # 返回值
except Exception as e:
    raise e
finally:
    driver.quit()