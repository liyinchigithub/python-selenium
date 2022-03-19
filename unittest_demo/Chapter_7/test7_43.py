from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #  complete
# caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps)
driver.get('https://www.ptpress.com.cn/')
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/div[2]/input').send_keys('Storm')
sleep(2)
driver.quit()