from tools.read_json import ReadJson
from driver.web_driver import MyWebDriver
import allure


class Finance:
    def __init__(self):
        self.finance_ele = ReadJson.read_json('../config/ele4.conf')["finance"]

    @allure.step('点击导航栏中的财务管理')
    def click_link_finance(self):
        ele = MyWebDriver.wait_element_present(
            self.finance_ele["link_finance"]["prop"],
            self.finance_ele["link_finance"]["value"])
        ele.click()

    @allure.step('点击子模块账户管理')
    def click_link_account(self):
        ele = MyWebDriver.wait_element_present(
            self.finance_ele["link_account"]["prop"],
            self.finance_ele["link_account"]["value"])
        ele.click()

    def input_name(self, text):
        ele = MyWebDriver.wait_element_present(
            self.finance_ele["input_name"]["prop"],
            self.finance_ele["input_name"]["value"])
        MyWebDriver.input(ele, text)

    def input_no(self, text):
        ele = MyWebDriver.wait_element_present(
            self.finance_ele["input_no"]["prop"],
            self.finance_ele["input_no"]["value"])
        MyWebDriver.input(ele, text)

    @allure.step('点击搜索按钮')
    def click_button_search(self):
        ele = MyWebDriver.wait_element_present(
            self.finance_ele["button_search"]["prop"],
            self.finance_ele["button_search"]["value"])
        ele.click()

    def scroll_div_navigation(self):
        ele = MyWebDriver.wait_element_present(
            self.finance_ele["div_navigation"]["prop"],
            self.finance_ele["div_navigation"]["value"])
        MyWebDriver.scroll_top(ele)

    def account_query_name(self, data):
        self.click_link_finance()
        self.scroll_div_navigation()
        self.click_link_account()
        with allure.step(f'输入姓名：{data["input_name"]}'):
            self.input_name(data["input_name"])
        self.click_button_search()

    def account_query_no(self, data):
        with allure.step(f'输入账户号码：{data["input_no"]}'):
            self.input_no(data["input_no"])
        self.click_button_search()
