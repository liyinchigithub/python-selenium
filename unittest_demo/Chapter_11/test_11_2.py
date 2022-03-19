import pytest

def test_a():
    print('aaaa')
    assert 'a' == 'a'

def test_b():
    print('bbbb')
    assert 'b' == 'b'

if __name__ == '__main__':
    pytest.main(["-s", "test_11_2.py"])