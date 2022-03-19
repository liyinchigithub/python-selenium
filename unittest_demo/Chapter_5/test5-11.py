from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/index.htm')
print(driver.current_window_handle)  # 查看当前window handle
driver.find_element_by_link_text('Window Open Test').click()  # 打开新window1
print(driver.window_handles)  # 查看所有window handles
sleep(2)
driver.close()
print(driver.window_handles)  # 查看现在的所有window handles，可以看到第一个window关闭，第二个window还在
sleep(2)
driver.quit()  # 看到所有windows都被关闭