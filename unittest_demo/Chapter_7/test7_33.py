from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("storm")
driver.find_element_by_id('su').click()
js1 = "window.scrollTo(0, document.body.scrollHeight)"# 滑动滚动条到底部
js2 = "window.scrollTo(0,0)"# 滑动到顶端
js3 = "window.scrollTo(0,200)"# 向下移动200像素
js4 = "arguments[0].scrollIntoView();"  # 滑动到指定元素
sleep(2) #等待页面加载完，注意观察滚动条目前处于最上方
driver.execute_script(js1) #执行js1，将滚动条滑到最下方
sleep(2) #加等待时间，看效果
driver.execute_script(js2) #执行js2，将滚动条滑到最上方
sleep(2) #加等待时间，看效果
driver.execute_script(js3) #执行js3，将滚动条向下滑到200像素
sleep(2) #加等待时间，看效果
driver.execute_script(js2) #执行js2，将滚动条滑到最上方
sleep(2)
ele = driver.find_element_by_id('con-ar')  #定位一个元素
driver.execute_script(js4,ele)  #滑动到上面定位的元素的地方
sleep(2)
driver.quit()
