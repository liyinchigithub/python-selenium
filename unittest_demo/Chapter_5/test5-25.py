from selenium import webdriver

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
lsts = driver.find_elements_by_name("ids[]")
for lst in lsts:
    if lst.is_selected():
        print('pass')
    else:
        print('fail')