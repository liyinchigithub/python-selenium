import pytest


class Test01():
    @pytest.mark.L1
    @pytest.mark.L2
    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    @pytest.mark.L2
    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'

class Test02():
    @pytest.mark.L1
    def test_c(self):
        print('cccc')
        assert 'c' == 'c'

    @pytest.mark.L3
    def test_d(self):
        print('dddd')
        assert 'd' == 'd'

if __name__ == '__main__':
    pytest.main(["-s", "./test_11_13.py"])