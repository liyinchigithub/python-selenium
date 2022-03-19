from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://passport.ctrip.com/user/reg/home')
driver.find_element_by_xpath('//*[@id="agr_pop"]/div[3]/a[2]').click()
sleep(2)
# 获取滑块
slider = driver.find_element_by_xpath('//*[@id="slideCode"]/div[1]/div[2]')
# 获取整个滑块框
ele = driver.find_element_by_id('slideCode')
# 需要使用到Actions的方法来进行拖动；
ActionChains(driver).drag_and_drop_by_offset(slider,ele.size['width'], ele.size['height']).perform()
# 这样也行,向右滑动一定的距离,长度是滑块框的宽度
# ActionChains(driver).drag_and_drop_by_offset(slider,ele.size['width'], 0).perform()
sleep(2)
driver.quit()