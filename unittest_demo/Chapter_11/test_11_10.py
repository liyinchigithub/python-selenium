import pytest


def test_b():
    print('test_11_10')
    assert 'Storm' in 'Hello Storm'


if __name__ == '__main__':
    pytest.main(["-s", "test_11_10.py"])