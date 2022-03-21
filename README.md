# python-selenium

[![python](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-374/) [![pip](https://img.shields.io/badge/pip-22.0.4-yellow.svg)](https://pip.pypa.io/en/stable/)[![selenium](https://img.shields.io/badge/selenium-v4.1.0-blue.svg)](https://pypi.org/project/selenium/)

>该项目能够快速熟悉复习selenium webdriver

# 目录说明
* -src                    代码
* --package               顶包
* ---module               模块（package包下的模块）
* ----__init__.py         模块初始化
* ----test_selenium.py    模块
* -download_file          下载文件存放路径，通过chromeOptions capability设置
* -unittest_demo          unittest selenium 示例代码
* -allure-2.17.2          allure报告
* -save_images            webdriver 截图保存图片路径
* -webdriver_init.py      webdriver 初始化(本地、远程、chromeoptions参数配置)
* -logging_init.py        logging 初始化(日志初始化配置，每次触发写入本地文件和控制台)
* -report                 allure生成json、html报告存放位置
* -pytest.ini             pytest单元测试框架配置文件
* -requirements.txt       依赖

## 安装依赖

```shell
pip install requirement.txt
```

## 运行所有用例脚本
```shell
pytest
```

## 运行指定用例脚本

```shell
pytest src/package/module/test_selenium.py
```

## 仅运行指定标志的用例
```shell
# 运行标注@pytest.mark.test的测试用例
pytest -m test
```
## 控制台详细输出

```shell
pytest -v
```

# allure 配置

## 【allure window 配置环境变量】
>https://www.cnblogs.com/hl-2030/p/13690165.html?ivk_sa=1024320u

## 【mac、linux】

```shell
 cd ~
 vim .bash_profile 
 export ALLURE_HOME=/Users/liyinchi/workspace/python/python-learning/allure-2.17.2/
 export PATH=$PATH:ALLURE_HOME/bin
 allure --version
```

## 运行命令生成allure测试报告

>已在项目根目录下新建目录report，在report目录下html文件夹用于存放html报告

### 执行命令（生成json报告）

```shell
pytest -s -q --alluredir ./report
```

### 执行命令（生成html报告）
```shell
allure generate ./report -o ./report/html
```

# 测试页面
>http://sahitest.com/demo/index.htm

# selenium常用方法和属性

* 实例化
```python
form selenium import webdriver
driver=webdriver.Chrome()
```

* 打开、关闭、退出浏览器
```python
webdriver.Chrome()
webdriver.Firfox()

driver.close()
driver.quit()
```

* 访问网页
```python
driver.get("https://www.baidu.com")
```
* 网页后退、前进

访问多个不同域名或者路由地址后，可操作性
```python
driver.back()
driver.forward()
```

* 等待
```python
from time import sleep
sleep(2)# 等待2秒
```

* 刷新浏览器页面
```python
driver.refresh()
```

* 窗口操作
```python
    driver.maximize_window() # 窗口最大化
    driver.minimize_window()# 窗口最小化
    driver.fullscreen_window()# 窗口全屏

    driver.get_window_size() # 获取窗口大小
    driver.set_window_size(500,500)# 设置窗口大小
    driver.set_window_position(0,0) # 设置窗口位置
    driver.get_window_position() # 获取窗口位置
```

* 网页标题（属性）
```python
driver.title # 网页当前标题
driver.name # 当前实例浏览器名称

```

* 获取当前网页地址（属性）
```python
driver.current_url
```

* 获取网页源码
```python
driver.page_source
```

* 多窗口操作
```python
handle_all=driver.window_handles # 获取所有窗口句柄
handle=driver.current_window_handle # 获取当前窗口句柄 (存储原始窗口句柄)
driver.switch_to.window(handle) # 切换到指定句柄窗口
driver.switch_to.window(handle_all[0]) # 切换到指定句柄窗口

assert len(driver.window_handles)==1 # 检查当前有没有其他开启的窗口

wait.until(EC.number_of_windows_to_be(2))# 等待打开两个窗口

# 遍历循环，找到新的窗口（存储当前所有窗口A=》打开新窗口=》获取当前所有窗口B 并遍历A和B差异）新窗口索引位置一般在最后一个？？？

```

* 多窗口操作（selenium 4）
```python
driver.switch_to.new_window('tab') # 打开一个新标签时，并自动切换到新标签
driver.switch_to.new_window('window')# 打开一个新窗口时，并自动切换到新窗口
```

* 切换焦点
```python
driver.switch_to_alert() # 切换到弹窗
driver.switch_to_default_content() # 切换焦点到主窗口（相对iframe/frame来说）
```

* 切换到iframe 或frame
```python
driver.switch_to_frame(参数可以是frame的索引、名称或者元素) # 切换到frame或iframe
```

* 隐性等待
```python
driver.implicity_wait(10) # 等待10秒
```

* 设置页面完全加载完 超时时间
```python
driver.set_page_load_timeout(10)# 10秒
```

* 设置脚本执行的 超时时间
```python
driver.set_script_timeout(10)# 10秒
```

# selenium元素定位方法

8种单个元素定位方式，如果找到多个默认第一个
```python
driver.find_element_by_id()
driver.find_element_by_name()
driver.find_element_by_class_name()
driver.find_element_by_tag_name() # html <input> 即tag name为input
driver.find_element_by_link_text() # html <a>新闻</a> 文字全匹配
driver.find_element_by_partial_link_text()# html <a>新闻</a> 文字部分匹配
driver.find_element_by_xpath()
driver.find_element_by_css_selector() # F12 元素复制 cssSelector
```

8中多个元素定位方式，返回一个列表，通过切片、索引来使用元素

```python
driver.find_elements_by_id()
driver.find_elements_by_name()
driver.find_elements_by_class_name()
driver.find_elements_by_tag_name()
driver.find_elements_by_link_text()
driver.find_elements_by_partial_link_text()
driver.find_elements_by_xpath()
driver.find_elements_by_css_selector() # F12 元素复制 cssSelector
```

* find_element
```python
driver.find_element(By.ID,"").send_keys("")
driver.find_element(By.NAME,"").send_keys("")
driver.find_element(By.ID,"").send_keys("")
driver.find_element(By.ID,"").send_keys("")
driver.find_element(By.ID,"").send_keys("")
driver.find_element(By.ID,"").send_keys("")
```



* xpath几种格式

1.第一种格式：
![image](https://user-images.githubusercontent.com/19643260/159109014-4caff4ca-3d61-46e5-ae5f-2a5f167bbc1d.png)

.//标签[@属性名='属性值']

```xpath
.//span[@title='custom_link']
```
![image](https://user-images.githubusercontent.com/19643260/159109047-2a7fc2ab-432e-480f-a4f4-7c00c289bc41.png)

2.第二种格式：
![image](https://user-images.githubusercontent.com/19643260/159109062-6bf34e0e-eca2-43b1-a5f6-5ef8786aed06.png)

.//标签[contains(text(),"标签内容")]

```xpath
./span[contains(text(),"确定")]
```

注意：移动端 使用chrome://inspect/#devices工具定位H5元素，仅能使用第一种格式(.//标签[@属性="属性值"])，不能使用第二种(.//标签[contains(text(),"标签内容")])

![image](https://user-images.githubusercontent.com/19643260/159109070-72479a0e-286c-4466-8082-cb30b3fe8bad.png)

3.第三种格式：
![image](https://user-images.githubusercontent.com/19643260/159109075-73d21dcd-1204-48ed-92bf-eb97663b8d57.png)

.//标签名[contains(@属性名,'属性值')]

```xpath
//iframe[contains(@src,“http://vrmstest2.maimaiche.com/ucvrms/repair/maintenance/list.do_;jsessionid=a11e054a-953a-457b-b294-35a10753d0e8?isInit=true“)]
```

* 获取html标签元素内容
```python
driver.find_element_by_id(('div').text
```

* 复选框-判断是否选中状态（checkbox）
```python
driver.find_element_by_tag_name('id_01').is_selected()
```

* 串联查询（在已找到元素层级基础上在继续往下查找）
```python
driver.find_element_by_id('B').find_element_by_tag_name('div').text
```

* 通过父元素定位子元素
```python
driver.find_element_by_xpath("//div[@id='B']/div").text
```

* 通过子元素定位父元素
```python
# `.`代表当前节点; '..'代表父节点
mytext = driver.find_element_by_xpath("//div[@id='C']/../..").text
```

* xpath轴 （myhtml5-3.html）
```python
mytext1 = driver.find_element_by_xpath("//div[@id='C']/parent::div/parent::div").text
```


* 弟弟元素定位哥哥元素
```python
driver.find_element_by_xpath("//div[@id='D']/preceding-sibling::div[1]").text
```

# 获取元素信息

* 获取元素属性
```python
driver.find_element_by_id('kw').get_attribute('id')  #打印搜索按钮的id属性
```

* 获取元素标签
```python
driver.find_element_by_id('kw').tag_name
```

* 获取元素文本
```python
driver.find_element_by_id('kw').text
```


* 获取元素大小
```python
driver.find_element_by_id('kw').size
```

* 获取CSS属性值
```python
driver.value_of_css_property("height")
```


* 判断页面元素是否可见

有时候找能找到元素，但是页面不显示，导致脚本报错
```python
driver.find_element_by_id('kw').is_displayed()
```

* 判断页面元素是否可用

有时候找能找到元素，元素置灰不可点击，需要先判断是否可用，比如html元素加了属性disable 或者 元素被遮挡
```python
driver.find_element_by_id('kw').is_enabled()
```
* 判断页面元素是否被选中

单选框、多选框
```python
driver.find_element_by_id('kw').is_selected()
```


# 鼠标操作

需要先引入鼠标操作包

```python
from selenium.webdriver.common.action_chains import ActionChains
```

* 鼠标单击元素（左）
```python
ActionChains(driver).click(元素).perform() # 传递driver ActionChains(driver)；动作 click(元素)；执行 perform()
```

* 鼠标双击元素（左）
```python
ActionChains(driver).double_click(元素).perform() # 传递driver ActionChains(driver)；动作 click(元素)；执行 perform()
```

* 鼠标右击元素
```python
ActionChains(driver).context_click(元素).perform() # 传递driver ActionChains(driver)；动作 context_click(元素)；执行 perform()
```

* 鼠标悬浮
```python
ActionChains(driver).move_to_element(元素).perform() # 传递driver ActionChains(driver)；动作 move_to_element(元素)；执行 perform()
```

* 鼠标拖动
```python
ActionChains(driver).drag_and_drop(起点元素,终点元素).perform() # 传递driver ActionChains(driver)；动作 drag_and_drop(元素)；执行 perform()
```

* 模拟鼠标的悬浮动作
```python
driver.get("http://sahitest.com/demo/mouseover.htm")
ele = driver.find_element_by_xpath('/html/body/form/input[1]')
sleep(2)
# 通过move_to_element()来模拟鼠标的悬浮动作
ActionChains(driver).move_to_element(ele).perform()
ActionChains(driver).key_up()
```

# 按键操作

* 文字输入
```python
driver.find_element_by_id('bordercheck').send_keys("输入点东西")
```

* 组合键
（1）ctrl+c/a/v
```python
import selenium.webdriver.common.keys import Keys;
driver.find_element_by_id("").send_keys(Keys.CONTROL,'a')
driver.find_element_by_id("").send_keys(Keys.CONTROL,'c')
driver.find_element_by_id("").send_keys(Keys.CONTROL,'v')
```

（2）按住ctrl键
```python
import selenium.webdriver.common.keys import Keys;
import selenium.webdriver.common.action_chains import ActionChains;

ActionChains(driver).key_down(Keys.CONTROL).perform()

```

（3）空格键

可用于复选框选中 checkbox
```python
driver.find_element_by_id("checkbox").send_keys(Keys.SPACE)
```

# 控件实操

## 搜索框
* 
```python
driver.send_keys("输入的内容") # 输入文字
driver.clear() # 清除文字
driver.get_property("value") # 获取输入框的内容
driver.find_element_by_id("").attribute('name') # 获取元素属性
driver.find_element_by_id("").tag_name; # 获取元素tag name
```

## 按钮
* 
```python
driver.find_element_by_id("").click() # button
driver.find_element_by_id("").submit() # button
driver.find_element_by_xpath(".//input[@type='radio']").is_selected() # radio 是否被选中  input type 为radio
```

## 复选框

实用空格键选中复选框、使用鼠标点击选中复选框
```python
driver.find_element_by_id("checkbox").send_keys(Keys.SPACE)
driver.find_element_by_id("").click() # button
```

选中一组复选框（全选复选框）
```python
eles=driver.find_elements_by_xpath(".//input[@type='checkbox']") # 找到所有复选框
# 遍历点击
for ele in eles:
    ele.click()
```

## 链接
* 
```python
driver.find_element_by_xpath(".//a[@type='link']").text
```

## select下拉列表
* select 元素、option子元素
```python
# 两种方式
form selenium.webdriver.support.ui import Select
form selenium.webdriver.support.select import Select

# 3种选择方法
# 4种取消方法
# 3种属性，用于获取下拉列表选项
# 1种属性，判断是否可多选

```

## input下拉列表
* 
```python
from selenium.webdriver.common.action_chains import ActionsChains
from time import sleep
# 假设可输入，先输入后自动展开下拉列表，按键盘方向键向下，再按键盘回车键
driver.find_element_by_id('select').send_keys(b)
sleep(3)
driver.find_element_by_id('select').send_keys(Key.ARROW_DOWN)
sleep(3)
driver.find_element_by_id('select').send_keys(Key.ENTER)

```

## 表格
* 
```python
    driver.get("http://sahitest.com/demo/tableTest.htm")
    table = driver.find_element_by_id('t2')
    rows = table.find_elements_by_tag_name('tr')# 基于表格父节点，查找地址下子节点tag_name为tr的元素
    cols = rows[0].find_elements_by_tag_name('td')# 查找地址下子节点tag_name为td的元素
    for i in range(len(rows)):
        for j in range(len(cols)):
            cell = rows[i].find_elements_by_tag_name('td')[j]
            print(cell.text)
```

## frame 框架
* frame 用于全页面
```python
driver.
```

* iframe 只用于局部页面
```python
driver.switch_to.frame("iframe属性id")
driver.switch_to.frame("iframe属性name")
driver.switch_to.frame(0)
driver.switch_to.frame(iframe_element)

# 切换回主页面
driver.switch_to.default_content()
# 切回上一级页面
driver.switch_to.parent_frame()
```

## JavaScript 弹窗

1.警告类弹alert()        显示警告或其他信息，用于通知用户。   上方有【文本框】，下方只有一个【确认】按钮。
2.确认类弹窗confirm()    询问是否继续某种操作等功能。         上方有【文本框】，下方有【确认】和【取消】两种按钮。
3.消息类弹窗prompt()     需要输入一些信息。                 上方【文字信息】、【文本框】，下方会有【确认】和【取消】按扭

在 WebDriver 中处理 JavaScript 所生成的 alert、confirm 以及 prompt 是很简单的。

具体做法是使用switch_to_alert()方法定位到 alert/confirm/prompt。

|名称|	用法|
|-|-|
|accept()	                    |   点击Alert的【确认】按钮|
|authenticate(username,password)|	给需要验证的Alert发送账号和密码，默认点击OK|
|dismiss() 	                    |   点击Alert的【取消】按钮|
|send_keys(keysToSend)      	|   在Alert的输入框输入信息|
|text	                        |   获取Alert上的文言信息|
|switch_to.alert	            |   切换到Alert然后使用 text/accept/dismiss/send_keys 按需进行操做。|

4中常见操作：获取警告框的text消息、接受消息框(确定)、取消、输入值

* text属性，即返回alert/confirm/prompt 中的文字信息。
* accept方法，即点击确认按钮。
* dismiss方法，即点击取消按钮，如果有的话。
* send_keys方法，即输入值，这个 alert\confirm 没有对话框就不能用了，不然会报错。


```python
# 接受弹窗
driver.switch_to.alert.accept()
# 得到弹窗的文本消息,比如得到：请输入用户名！
driver.switch_to.alert.text
print(message)
# 取消按钮
driver.switch_to.alert.dismiss()
# 输入值
driver.switch_to.alert.send_keys("输入内容")
```


## 非JavaScript 弹窗
* 
当做正常元素去处理

## 文件下载
* 
```python
driver.
```

## 文件上传
* file类型

```python
driver.
```

# selenium高级应用

## 复杂控件的操作

### Ajax选项

* 
```python
driver.
```
### 操作富文本编辑器
* 
```python
driver.
```
### 滑动滑块操作
* 
```python
driver.
```

## webdriver特殊操作

### 
* 
```python
driver.
```

### 元素class值包含空格
* 
```python
driver.
```

### property、attribute、text的区别
* 
```python
driver.
```
* 
```python
driver.
```
* 
```python
driver.
```

### 操作cookie
* 
```python
driver.
```

### 截图
* 
```python
driver.
```

### 定位动态id
* 
```python
driver.
```

### 获取焦点元素
* 
```python
driver.
```

### 颜色验证
* 
```python
driver.
```

## JavaScript应用
* 
```python
driver.
```

### 操作页面元素
* 
```python
driver.
```

### 修改页面元素属性
* 
```python
driver.
```

### 操作滚动条
* 
```python
driver.
```

### 高亮显示正在被操作的页面元素
* 
```python
driver.
```

### 操作span类型元素
* 
```python
driver.
```

# 浏览器定制启动参数
* 
```python
driver.
```

# AutoIt的应用
* 
```python
driver.
```

# 重要异常
* 
```python
driver.
```

# selenium等待机制

## 影响元素加载的外部因素
* 
```python
driver.
```
## 强制等待
* 
```python
driver.
```

## 隐性等待
* 
```python
driver.
```

## 显性等待
* 
```python
driver.
```

# 线性测试脚本

## Redmine系统

Redmine是一个项目管理和曲线跟踪系统，其功能和我们常见的项目管理、缺陷跟踪系统诶西。
* 
```python
driver.
```



## 参考

1. [selenium chrome options参数设置](https://note.youdao.com/s/ER8jfnYo)
2. [csdn 博文](https://www.cnblogs.com/guapitomjoy/p/12150416.html)
3. [csdn 博文](https://www.cnblogs.com/clement-jiao/p/10889234.html)
