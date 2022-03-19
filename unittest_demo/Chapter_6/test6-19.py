from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-6.html'
driver.get(html_file)
text1 = driver.find_element_by_id('CellWithId').text  # 该单元格有id
print(text1)
driver.quit()