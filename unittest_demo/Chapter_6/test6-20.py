from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-6.html'
driver.get(html_file)
# text1 = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[4]').text #注意这个xpath不合理
text1 = driver.find_element_by_xpath('//table//tr[2]/td[4]').text # 这个稍好，你还能写出更好的xpath吗？
print(text1)
driver.quit()