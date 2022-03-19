from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-6.html'
driver.get(html_file)
table = driver.find_element_by_xpath('/html/body/table[1]')
rows = table.find_elements_by_tag_name('tr')
cols = rows[0].find_elements_by_tag_name('td')
for i in range(len(rows)):
    for j in range(len(cols)):
        cell = rows[i].find_elements_by_tag_name('td')[j]
        print(cell.text)

driver.quit()