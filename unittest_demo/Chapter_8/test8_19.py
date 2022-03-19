from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

try:
    ele1 = WebDriverWait(driver, 10).until(lambda x:x.find_element_by_id('kw'))
    ele1.send_keys('Storm')
except Exception as e:
    raise e
finally:
    driver.quit()