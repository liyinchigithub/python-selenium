from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("storm")
driver.find_element_by_id('su').click()
driver.set_window_size(500,500) #缩小浏览器窗口，使之出现横向滚动条
js5 = "window.scrollTo(document.body.scrollWidth,0)"
js6 = "window.scrollTo(0,0)"
js7 = "window.scrollTo(200,0)"
driver.execute_script(js5)  #移动到最右边
sleep(2)
driver.execute_script(js6) #移动到最左边
sleep(2)
driver.execute_script(js7) #向右移动200像素
sleep(2)
driver.quit()