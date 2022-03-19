import pytest,allure

@allure.feature("测试场景2")      #标记代码
class TestDemo():
    @allure.story("测试用例2-1")
    @allure.severity("minor")
    def test_2_1(self):
        """
        用例描述：这是第一条用例的描述
        """
        #allure.MASTER_HELPER.description("11111111111111")
        a = 1 + 1
        assert a == 3  # 断言失败

    @allure.story("测试用例2-2")
    @allure.severity("minor")
    @allure.step('用例2:重要步骤')
    def test_2_2(self):
        assert 2 == 2

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/'])