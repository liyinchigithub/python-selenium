from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
ele = driver.find_element_by_link_text('新闻')
# ele.click()  # 左键的单击
ActionChains(driver).click(ele).perform()
sleep(2)
driver.quit()