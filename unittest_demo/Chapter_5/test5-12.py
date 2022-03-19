from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/index.htm')
first_handle = driver.current_window_handle # 将第一个窗口句柄存储到变量first_handle
driver.find_element_by_link_text('Window Open Test').click()  # 打开新window1
all_handles = driver.window_handles # 将所有窗口句柄存储起来，是一个列表
# 接下来，我们要将当前窗口切换到句柄2，然后操作窗口2中的元素，比如点击链接“Link Test”
sleep(2)
driver.switch_to.window(all_handles[1])  # 切换句柄
driver.switch_to.frame(0) # 切换到第一个frame中，后续会细讲
driver.find_element_by_link_text('Link Test').click()
sleep(2)
driver.quit()  # 看到所有windows都被关闭