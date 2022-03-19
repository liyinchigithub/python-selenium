from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' : {
        'images' : 2
    }
}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options = options)
driver.get("http://www.baidu.com/")
sleep(2)
driver.quit()