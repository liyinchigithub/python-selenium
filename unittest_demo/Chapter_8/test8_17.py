from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/')
cur_window_handles = driver.window_handles  # 获取当前窗口句柄
print("当前窗口句柄：{}".format(cur_window_handles))
driver.find_element_by_link_text('Window Open Test').click()

try:
    ele1 = WebDriverWait(driver, 10).until(EC.new_window_is_opened(cur_window_handles))
    sleep(2)
    print(ele1)
    print(type(ele1))
except Exception as e:
    raise e
finally:
    driver.quit()