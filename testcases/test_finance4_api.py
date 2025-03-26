import pytest
import allure
from lib.test_api import TestAPI
from tools.read_excel import ReadExcel


@allure.feature('财务管理模块接口测试')
class TestFinance4API:

    login_data = ReadExcel.read_excel_api('../data/testdata_api.xlsx', 'login4', 1, 3)
    test_data = ReadExcel.read_excel_api('../data/testdata_api.xlsx', '财务管理4', 1, 44)

    def setup_class(self):
        for i in self.login_data:
            getattr(TestAPI, i['method'])(i)

    @pytest.mark.parametrize('testdata', test_data)
    def test_001_api(self, testdata):
        resp = getattr(TestAPI, testdata['method'])(testdata)
        actual = resp.text
        assert(testdata['expect'], actual)


if __name__ == '__main__':
    pytest.main(['-s', 'test_finance4_api.py'])
