from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.save_screenshot('a.png') # 截取当前页面，当前目录，保存成png类型文件
driver.quit()