import pytest
from driver.web_driver import MyWebDriver
from lib.test_login_gui import Login
from lib.test_decrypt_gui import Decrypt
import allure

driver = MyWebDriver.start()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item:测试用例
    :param call:测试步骤
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        # 添加allure报告截图
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图",
                          allure.attachment_type.PNG)


@pytest.fixture(scope='session', autouse=True)
def login():
    """
    启动浏览器打开项目主页并完成登录和解密操作
    :return:
    """
    driver = MyWebDriver.start()
    login_data = {
        "username": "wncd000",
        "password": "woniu123",
        "verifycode": "0000"
    }
    secondpass = "woniu123"
    if not MyWebDriver.is_element_present("link text", "[注销]"):
        with allure.step('成功登录'):
            Login().login(login_data)
    with allure.step('二级密码成功解密'):
        Decrypt().decrypt(secondpass)
    yield
    driver.quit()
