from selenium import webdriver
from time import sleep

'''
browser.download.dir：指定下载路径
browser.download.folderList：设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
browser.download.manager.showWhenStarting：在开始下载时是否显示下载管理器
browser.helperApps.neverAsk.saveToDisk：对所给出文件类型不再弹出框进行询问
'''
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', 'd:\\')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
sleep(3)
driver.quit()