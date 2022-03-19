from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/') # 打开百度首页
sleep(2)
driver.get('https://www.ptpress.com.cn/') # 打开人邮首页
sleep(2)
driver.back() # 通过back，后退到百度首页
sleep(2)
driver.forward() # 通过forward，前进到人邮首页
sleep(2)
driver.quit()