import pytest


def setup_module():
    print('setup_moudle')

def teardown_module():
    print('teardown_moudle')

def setup():
    print('setup')

def teardown():
    print('teardown')

def test_a():
    print('aaaa')
    assert 'a' == 'a'

def test_b():
    print('bbbb')
    assert 'b' == 'b'

if __name__ == '__main__':
    pytest.main(["-s", "./test_11_5.py"])