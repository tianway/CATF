from tools.read_json import ReadJson
from driver.web_driver import MyWebDriver


class Login:

    def __init__(self):
        self.login_ele = ReadJson.read_json('../config/ele.conf')["login"]

    def input_account(self, username):
        uname = MyWebDriver.wait_element_present(self.login_ele["input_username"]["prop"], self.login_ele["input_username"]["value"])
        MyWebDriver.input(uname, username)

    def input_password(self, password):
        upass = MyWebDriver.wait_element_present(self.login_ele["input_password"]["prop"], self.login_ele["input_password"]["value"])
        MyWebDriver.input(upass, password)

    def input_verifycode(self, verifycode):
        vfcode = MyWebDriver.wait_element_present(self.login_ele["input_verifycode"]["prop"], self.login_ele["input_verifycode"]["value"])
        MyWebDriver.input(vfcode, verifycode)

    def click_login_button(self):
        login_button = MyWebDriver.wait_element_present(self.login_ele["button_login"]["prop"], self.login_ele["button_login"]["value"])
        login_button.click()

    def login(self, login_data):
        self.input_account(login_data['username'])
        self.input_password(login_data['password'])
        self.input_verifycode(login_data['verifycode'])
        self.click_login_button()
