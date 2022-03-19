from selenium import webdriver
from time import sleep
import os

'''
通过js的方式修改span中间的值
js = 'document.getElementById("span_id").innerText="aaaa"'
'''
driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7_3.html'
driver.get(html_file)
sleep(2)
js1 = "document.getElementById('span_id').innerText='aaa'"
driver.execute_script(js1)
sleep(2)
driver.quit()