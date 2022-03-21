# -*- coding: UTF-8 -*-
# 文件名：driver_init.py
from selenium import webdriver
from PIL import Image, ImageEnhance
from selenium.webdriver.support.wait import WebDriverWait   #
from selenium.webdriver.support import expected_conditions as EC    #
from selenium.webdriver.common.by import By #
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  #
from selenium.webdriver.chrome.options import Options # => 引入Chrome的配置
from webdriver_manager.chrome import ChromeDriverManager  # 自动更新下载chromedriver
from selenium.webdriver import Remote # 运行远程服务器webdriver
import platform;


class DriverConfig:
    # 构造函数
    def __init__(self):
        pass
    # 初始化webDriver
    def driver_config(self):
        
        # 设置默认下载目录
        download_file_path = './download_file/'
        prefs = {
            "download.prompt_for_download": False,
            "download.default_directory": download_file_path
        }
        options = webdriver.ChromeOptions()
        # 谷歌浏览器驱动路径
        options.binary_location = '/usr/bin/google-chrome-stable'
        # ChromeOptions
        options = webdriver.ChromeOptions()
        # 关闭浏览器提示信息
        options.add_argument('disable-infobars')
        # 浏览器全屏
        options.add_argument('start-fullscreen')
        # 无头模式
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')# 解决DevToolsActivePort文件不存在的报错
        options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        options.add_argument('--disable-gpu')# 谷歌文档提到需要加上这个属性来规避bug
        options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        options.add_argument('--disable-setuid-sandbox')
        options.add_experimental_option('prefs', prefs)
        # 获取谷歌浏览器所有控制台信息
        des = DesiredCapabilities.CHROME
        des['loggingPrefs'] = {'performance': 'ALL'}
        
        # 浏览器驱动（使用自动更新下载chromedriver）
        self.driver =webdriver.Chrome(ChromeDriverManager().install(
        ), options=options, desired_capabilities=options.to_capabilities())
        
        # 浏览器驱动（使用远程机器）
        # self.driver = webdriver.Remote(command_executor="http://10.224.2.98:4444/wd/hub", desired_capabilities=des,options=options)
        
        # 浏览器驱动（使用本地手动下载chromedriver）
        '''
        # 判断当前系统
        if(platform.system()=='Windows'):
            driverpath = './chromedriver/chromedriver.exe'
        else:    
            driverpath = './chromedriver/chromedriver'
        # 浏览器驱动
        self.driver = webdriver.Chrome(driverpath, options=options, desired_capabilities=des)# 运行本地chrome
        '''
        # 全局等待
        implicitly_wait = 60000
        self.driver.implicitly_wait(implicitly_wait)
        
        return self.driver

        '''
            chrome options
            https://note.youdao.com/s/ER8jfnYo
        '''