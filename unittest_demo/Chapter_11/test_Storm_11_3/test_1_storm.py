import pytest,allure

@allure.feature("测试场景1")      #标记场景
class TestDemo():
    @allure.story("测试用例1-1") # 标记测试用例
    @allure.severity("trivial") # 标记用例级别
    def test_1_1(self): # 用例1
        a = 1 + 1
        assert a == 2

    @allure.story("测试用例1-2")
    @allure.severity("critical")
    @allure.step('用例2:重要步骤')
    def test_1_2(self):
        assert 2 == 2

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/'])