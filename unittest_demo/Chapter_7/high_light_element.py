def highLightElement(driver,element):
    '''
    #封装高亮显示页面元素的方法；使用js代码，将页面元素对象的背景颜色设置为绿色，边框设置为红色
    :param driver:
    :param element:
    :return:
    '''
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,"background: green; border: 2px solid red;")

if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep

    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    ele = driver.find_element_by_id('kw')
    highLightElement(driver, ele)
    sleep(3)
    driver.quit()