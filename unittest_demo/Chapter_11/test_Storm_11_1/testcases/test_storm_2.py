import pytest


class TestStorm2(object):
    @pytest.mark.L2
    def test_02(self):
        print('bbb')
        assert 'b' == 'c'