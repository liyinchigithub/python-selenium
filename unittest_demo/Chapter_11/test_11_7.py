import pytest


def test_c(): # 这里没有self
    print('cccc')
    assert 'c' == 'c'

class Test01():
    def test_a(self): # 这里有self
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'


if __name__ == '__main__':
    pytest.main(["-s", "./test_11_7.py"])