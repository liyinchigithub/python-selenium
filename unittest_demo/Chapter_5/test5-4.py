from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.ptpress.com.cn/') # 打开人邮首页
sleep(2)
driver.refresh() # refresh,刷新页面
sleep(2)
driver.quit()