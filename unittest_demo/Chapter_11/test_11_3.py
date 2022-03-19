import pytest

'''
在函数中使用：
1、setup_module、teardown_module，在整个文件的开始和最后运行一次；
2、setup_function和teardown_function，在每个函数开始前后执行；
'''
def setup_module():
    print('setup_moudle')

def teardown_module():
    print('teardown_moudle')

def setup_function():
    print('setup_function')

def teardown_function():
    print('teardown_function')

def test_a():
    print('aaaa')
    assert 'a' == 'a'

def test_b():
    print('bbbb')
    assert 'b' == 'b'

if __name__ == '__main__':
    pytest.main(["-s", "./test_11_3.py"])