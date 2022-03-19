from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
try:
    ele = WebDriverWait(driver, 10).until(EC.title_is("百度一下，你就知道"))  # 判断title是XXX
    print(type(ele)) # 打印返回值类型
    print(ele) # 打印返回值
    driver.find_element_by_link_text('地图').click() # 如果title是XXX，就执行该语句
except Exception as e:
    raise e #有异常抛出
finally:
    driver.quit() # 最后退出driver