import pytest

'''
在class中使用：
1、setup_class、teardown_class，在整个class的开始和最后运行一次；
2、setup_method和teardown_method，在每个函数开始前后执行；
'''
class Test01():
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'


if __name__ == '__main__':
    pytest.main(["-s", "./test_11_4.py"])