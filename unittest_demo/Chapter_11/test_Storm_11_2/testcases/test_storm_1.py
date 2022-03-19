import pytest

class TestStorm1(object):
    @pytest.mark.L1
    def test_01(self):
        print('aaa')
        assert 'a'=='a'

if __name__ == '__main__':
    pytest.main(["-s", "test_storm_1.py", "--html=./report.html"])