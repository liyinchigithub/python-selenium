import pytest


class Test01():
    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'

class Test02():
    def test_c(self):
        print('cccc')
        assert 'c' == 'c3'  # 让其运行失败

    def test_d(self):
        print('dddd')
        assert 'd' == 'd'

if __name__ == '__main__':
    pytest.main(["-s", "./test_11_8.py::Test02"])