from tools.read_json import ReadJson
from driver.web_driver import MyWebDriver


class Decrypt:
    def __init__(self):
        self.mainmenu_ele = ReadJson.read_json(
            '../config/ele.conf')["mainMenu"]

    def click_button_decrypt(self):
        ele = MyWebDriver.wait_element_present(
            self.mainmenu_ele["button_decrypt"]["prop"],
            self.mainmenu_ele["button_decrypt"]["value"])
        ele.click()

    def input_secondpass(self, secondpass):
        ele = MyWebDriver.wait_element_present(
            self.mainmenu_ele["input_secondpass"]["prop"],
            self.mainmenu_ele["input_secondpass"]["value"])
        MyWebDriver.input(ele, secondpass)

    def click_button_ok(self):
        ele = MyWebDriver.wait_element_present(
            self.mainmenu_ele["button_ok"]["prop"],
            self.mainmenu_ele["button_ok"]["value"])
        ele.click()

    def decrypt(self, secondpass):
        self.click_button_decrypt()
        self.input_secondpass(secondpass)
        self.click_button_ok()
