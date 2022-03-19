import pytest


# class TestStorm: # 这种写法也是可以的
class TestStorm(object):
    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'

if __name__ == '__main__':
    pytest.main(["-s", "test_11_1.py"])