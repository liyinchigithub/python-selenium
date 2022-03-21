
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# selenium
# https://selenium-python-zh.readthedocs.io/en/latest/
# https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html

import requests  # http客户端模块
import time,os  # 日期时间模块
import pytest  # 单元测试模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
# from webdriver_init import * # 导入封装selenium初始化自定义模块
# from logging_init import * # 导入封装logging初始化自定义模块
import logging  # 日志模块
import pytesseract  # 验证码识别
import json
import webdriver_init
import logging_init
T = time.strftime("%Y-%m-%d %X")
# 初始化
driver = webdriver_init.DriverConfig.driver_config(webdriver)
# 初始化
logger = logging_init.LoggingConfig(
    logging, "./log/{}.txt".format(T)).logging_config()


'''
    [By类-可用属性]
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector

    [一次查找多个元素 (这些方法会返回一个list列表)]:

    find_elements_by_name
    find_elements_by_xpath
    find_elements_by_link_text
    find_elements_by_partial_link_text
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector
'''


# 每个模块（文件）之前执行
def setup_module():
    logger.info("teardown_module():每个模块（文件）之前执行")

# 每个类之前执行


def setup_class():
    logger.info("setup_class():每个类之前执行")

# 每个类之后执行


def teardown_class():
    logger.info("teardown_class():每个类之后执行")


'''
# 每个方法之前执行
def setup_function():
    logger.info("setup_function():非类中的方法，每个方法之前执行")

# 每个方法之后执行
def teardown_function():
    logger.info("teardown_function():非类中的方法，每个方法之后执行")
'''
# 类中的方法，每个方法之前执行


def setup_method():
    logger.info("setup_method():类中的方法，每个方法之前执行")

# 类中的方法，每个方法之后执行


def teardown_method():
    logger.info("teardown_method():类中的方法，每个方法之后执行")

# 每个模块（文件）之后执行


def teardown_module():
    driver.quit()
    logger.info("teardown_module():每个模块（文件）之后执行")


# 参数化数据
data = [("http://www.baidu.com", "百度搜索"), ("http://www.bing.com", "必应搜索")]
'''
    DDT 数据驱动（参数化）
'''


@pytest.mark.skip
@pytest.mark.parametrize("url,search_text", data)
def test_baidu_search(url, search_text):
    driver.maximize_window()
    driver.get_window_size()
    driver.set_window_size(500, 500)
    driver.set_window_position(800, 800)
    driver.get_window_position()

    driver.get(url)
    try:
        if("baidu" in url):
            driver.find_element_by_id("kw").send_keys(search_text)
            driver.find_element_by_id('su').click()
        elif("bing" in url):
            driver.find_element_by_id("sb_form_q").send_keys("python")
            driver.find_element_by_id('search_icon').click()
    except(ValueError):
        print(ValueError)
    time.sleep(10)
    # 截图-输出控制台
    file = driver.get_screenshot_as_png
    logger.info(file)
    # 截图-保存本地
    save_screenshot()
    logger.info("测试数据为{}".format(url))
    logger.info("测试数据为{}".format(search_text))


'''
    跳过的测试用例c
'''


@pytest.mark.skip
@pytest.mark.test
@pytest.mark.smoke
def test_bing_search():
    driver.maximize_window()
    url = "http://www.bing.com"
    driver.get(url)
    driver.find_element_by_id("sb_form_q").send_keys("python")
    driver.find_element_by_id('search_icon').click()
    time.sleep(2)
    # 截图-输出控制台
    file = driver.get_screenshot_as_png
    logger.info(file)
    # 截图-保存本地
    save_screenshot()


'''
    鼠标拖动（从A拖到B）
'''


@pytest.mark.skip
@pytest.mark.test
@pytest.mark.smoke
def test_mouse_drag_and_drop():
    driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
    source1 = driver.find_element_by_xpath(
        './/div[contains(text(),"Drag me")]')  # 起点元素
    target1 = driver.find_element_by_xpath(
        './/div[contains(text(),"Item 2")]')  # 终点元素
    ActionChains(driver).drag_and_drop(source1, target1).perform()
    time.sleep(2)
    source2 = driver.find_element_by_xpath(
        './/div[contains(text(),"Drag me")]')  # 起点元素
    time.sleep(2)
    target2 = driver.find_element_by_xpath(
        './/div[contains(text(),"Item 4")]')  # 终点元素
    ActionChains(driver).drag_and_drop(source2, target2).perform()


'''
    文字输入
'''
@pytest.mark.skip
@pytest.mark.test
@pytest.mark.smoke
def test_text_input():
    # 打开网页会弹出一个Alert弹窗，需要先关闭弹窗才能输入
    driver.get("http://sahitest.com/demo/formTest.htm")
    driver.switch_to.alert.accept()  # 切换至弹窗并点击关闭
    driver.find_element_by_class_name('bordercheck').send_keys("输入点东西")
    time.sleep(2)


'''
    弹窗Alert
'''
@pytest.mark.skip
@pytest.mark.test
@pytest.mark.smoke
def test_alert():
    # [Alert]
    # 打开网页会弹出一个Alert弹窗，需要先关闭弹窗才能输入
    driver.get("http://sahitest.com/demo/formTest.htm")
    driver.switch_to.alert.accept()# 切换至弹窗并点击关闭
    driver.find_element_by_class_name('bordercheck').send_keys("输入点东西")
    time.sleep(2)
    # [Confirm]
    # 打开网页会弹出一个Alert弹窗，需要先关闭弹窗才能输入
    # driver.get("http://sahitest.com/demo/formTest.htm")
    # driver.switch_to.alert.accept()# 切换至弹窗并点击关闭
    # driver.find_element_by_class_name('bordercheck').send_keys("输入点东西")
    # time.sleep(2)
    # [Prompt]
    # 打开网页会弹出一个Alert弹窗，需要先关闭弹窗才能输入
    driver.get("http://sahitest.com/demo/promptTest.htm")
    time.sleep(2)
    driver.find_element_by_name("b1").click()
    print(driver.switch_to.alert.text)# 获取警告弹窗文本信息
    time.sleep(2)
    driver.switch_to.alert.accept()# 切换至弹窗并点击【确定】按钮
    time.sleep(2)
    driver.get("http://sahitest.com/demo/promptTest.htm")
    driver.find_element_by_name("b1").click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()# 切换至弹窗并点击【取消】按钮
    driver.get("http://sahitest.com/demo/promptTest.htm")
    driver.find_element_by_name("b1").click()
    time.sleep(1)
    driver.switch_to.alert.send_keys("输入内容")
    time.sleep(1)
    driver.switch_to.alert.accept()# 切换至弹窗并输入内容，点击【确定】按钮
    time.sleep(1)
    
    
'''
    select 下拉列表
'''
@pytest.mark.skip
@pytest.mark.test
@pytest.mark.smoke
def test_select():
    # select
    driver.get("http://sahitest.com/demo/selectTest.htm")
    s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select
    time.sleep(2)
    s1.select_by_index(1)  # 通过index，选择第二项选项：o1
    time.sleep(2)
    s1.select_by_value("o2")  # 通过value值，选择value="o2"的项
    time.sleep(2)
    s1.select_by_visible_text("o3")  # 通过可见text，选择text="o3"的值，即在下拉时我们可以看到的文本
    time.sleep(2)
    
    s1.deselect_by_index(0)# 根据选项索引位置取消
    s1.deselect_by_value("o2")# 根据选项value属性值取消选择
    s1.deselect_by_visible_text("o3")# 根据选项可见文本取消选择
    s1.deselect_all()#  取消全选
    
    if s1.is_multiple:
        print("可多选")
    else:
        print("不可多选")
    
    # input 下拉列表
    driver.find_element_by_id('select').send_keys("b")
    time.sleep(3)
    driver.find_element_by_id('select').send_keys(Key.ARROW_DOWN)
    time.sleep(3)
    driver.find_element_by_id('select').send_keys(Key.ENTER)
    
    
'''
    表格（遍历获取表格每个单元格的值）
'''
@pytest.mark.skip
@pytest.mark.test
@pytest.mark.smoke
def test_table():
    driver.get("http://sahitest.com/demo/tableTest.htm")
    table = driver.find_element_by_id('t2')
    rows = table.find_elements_by_tag_name('tr')# 基于表格父节点，查找地址下子节点tag_name为tr的元素
    cols = rows[0].find_elements_by_tag_name('td')# 查找地址下子节点tag_name为td的元素
    for i in range(len(rows)):
        for j in range(len(cols)):
            cell = rows[i].find_elements_by_tag_name('td')[j]
            print(cell.text)
    
'''
    文件下载
'''
@pytest.mark.skip
@pytest.mark.test
@pytest.mark.smoke
def test_file_download():
    print()


'''
    文件上传
'''

@pytest.mark.skip
@pytest.mark.test
@pytest.mark.smoke
def test_file_upload():
    print()


'''
    selenium 截图保存本地
'''


def save_screenshot():
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    if driver.get_screenshot_as_file('./save_images/%s.png' % now_time):
        logger.info('保存成功')
    else:
        logger.info('保存失败')
