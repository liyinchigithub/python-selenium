import pytest

'''
pytest的断言更灵活
'''
class Test01():
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    def test_a(self):
        print('aaaa')
        assert 5 > 3

    def test_b(self):
        print('bbbb')
        assert 'Storm' in 'Hello Storm'


if __name__ == '__main__':
    pytest.main(["-s", "./test_11_8.py"])