from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
ele = driver.find_element_by_link_text('新闻') #通过link_text定位新闻元素

#height,打印元素的高
print(ele.value_of_css_property('height'))
#width，打印元素的宽
print(ele.value_of_css_property('width'))
#font-family，打印元素所使用的字体
print(ele.value_of_css_property('font-family'))

driver.quit()