from selenium import webdriver
from time import sleep


# 创建出启动浏览器所需要配置 -- 实例化ChromeOptions浏览器选项对象
chrome_options = webdriver.ChromeOptions()
# 构建配置信息 -- 通过浏览器选项对象调用配置方法
# 设置浏览器为无头模式
chrome_options.headless = True
# 将配置信息加入到浏览器启动 -- 实例化浏览器驱动对象添加属性option值
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.baidu.com")
sleep(2)
driver.quit()