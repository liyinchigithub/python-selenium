import pytest


class Test01():
    @pytest.mark.skipif(2>1, reason='这里是原因')
    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'


if __name__ == '__main__':
    pytest.main(["-s", "./test_11_14.py"])