# python-selenium


## 安装依赖

```shell
pip install requirement.txt
```

## 运行脚本

```shell
pytest test_selenium.py
```

## 运行脚本，仅运行指定标志的用例
```shell
pytest -m baidu
```

## 运行所有用例
```shell
pytest
```

```shell
pytest -v -m "指定标志"
```
-v 控制台详细输出

# 目录说明
* download_file
下载文件存放路径，通过chromeOptions capability设置
* save_images
selenium 截图保存图片路径
* conftest
初始化
* conftest
存放测试用例脚本（以test开头unittest单元测试脚本）

# selenium chrome options参数设置

>https://www.cnblogs.com/guapitomjoy/p/12150416.html

>https://www.cnblogs.com/clement-jiao/p/10889234.html

# allure配置环境变量

## 【window】
https://www.cnblogs.com/hl-2030/p/13690165.html?ivk_sa=1024320u

## 【mac、linux】

```shell
 cd ~
 vim .bash_profile 
 export ALLURE_HOME=/Users/liyinchi/workspace/python/python-learning/allure-2.17.2/
 export PATH=$PATH:ALLURE_HOME/bin
 allure --version
```

## 新建文件夹

在项目根目录下新建目录report，在report目录下，新建目录html，用于存放html报告

## 运行命令生成allure测试报告

### 执行命令（json）

```shell
pytest -s -q --alluredir ./report
```

### 执行命令（html）
```shell
allure generate ./report -o ./report/html
```