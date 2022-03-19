import unittest
import HTMLTestRunner
import time

if __name__ == '__main__':
    # 查找当前目录的测试用例文件
    testSuite = unittest.TestLoader().discover('.')
    # 定义一个文件名，文件名已年月日时分秒结尾，方便查找
    filename = "D:\\Storm_{}.html".format(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    # 以wb的方式打开文件
    with open(filename, 'wb') as f:
        # 通过HTMLTestRunner来执行测试用例，并生成报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='这里是报告的标题',description='这里是报告的描述信息')
        runner.run(testSuite)