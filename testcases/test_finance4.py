import pytest
import allure
from lib.test_finance_gui4 import Finance
from tools.read_excel import ReadExcel
from tools.read_json import ReadJson
from driver.web_driver import MyWebDriver


@allure.feature('财务管理模块测试')
class TestFinance4:
    driver = MyWebDriver.start()

    eles = ReadJson.read_json("../config/ele4.conf")["finance"]
    finance_data = ReadExcel.read_excel_gui("../data/testdata_gui.xlsx",
                                            "财务管理4", 1, 3)

    @allure.story('账户管理使用名字模糊查询')
    @pytest.mark.parametrize('data', finance_data["finance"][0:1])
    def test_001_account_query_name(self, data):
        testdata = data["data"]
        expect = data["expect"]
        Finance().account_query_name(testdata)
        if MyWebDriver.is_element_present(
                "xpath",
                "//table[@id='account-table']/tbody//td[contains(text(),'西安基本户')]"
        ):
            actual = 'query ok'
        else:
            actual = 'query fail'
        assert actual == expect

    @allure.story('账户管理使用账户号码模糊查询')
    @pytest.mark.parametrize('data', finance_data["finance"][1:2])
    def test_002_account_query_no(self, data):
        testdata = data["data"]
        expect = data["expect"]
        Finance().account_query_no(testdata)
        if MyWebDriver.is_element_present(
                "xpath",
                "//table[@id='account-table']/tbody//td[contains(text(),'100000')]"
        ):
            actual = 'query ok'
        else:
            actual = 'query fail'
        assert actual == expect

    def teardown_method(self):
        self.driver.refresh()


if __name__ == '__main__':
    pytest.main(['-s', 'test_finance4.py'])
