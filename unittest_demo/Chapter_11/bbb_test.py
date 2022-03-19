import pytest

class Test01:
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'


if __name__ == '__main__':
    pytest.main(["-s"])
