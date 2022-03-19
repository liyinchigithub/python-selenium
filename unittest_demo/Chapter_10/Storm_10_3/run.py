import unittest
import HTMLTestRunner
import time, os

if __name__ == '__main__':
    # 查找当前目录的测试用例文件
    testSuite = unittest.TestLoader().discover('.')
    # 这次将报告放到当前目录
    filename = os.getcwd() + os.sep + "Storm_{}.html".format(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    # 以wb的方式打开文件
    with open(filename, 'wb') as f:
        # 通过HTMLTestRunner来执行测试用例，并生成报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='Redmine测试报告',description='unittest线性测试报告')
        runner.run(testSuite)