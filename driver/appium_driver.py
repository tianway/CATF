from selenium.common.exceptions import TimeoutException
from tools.logger import Logger
from tools.read_yaml import ReadYaml
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


class AppiumDriver:
    # 类变量，用于存放driver对象
    driver = None

    logger = Logger.get_logger()
    config = ReadYaml.read_yaml()['appium']

    @classmethod
    def start(cls, url=config["url"], desired_capabilities=config["desired_capabilities"]):
        """
        启动webdriver，并将webdriver对象返回
        :param url: appium_server的url
        :param desired_capabilities: 移动端连接的相应配置信息
        :return: webdriver对象
        """
        if cls.driver is None:
            cls.driver = webdriver.Remote(url, desired_capabilities)
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def wait_element_present(cls, prop, value, freq=0.5, timeout=5):
        """
        封装一个类方法，以显示等待的方式获取元素
        :param prop: 定位方法
        :param value: 定位方法对应的值
        :param freq: 搜索元素频率
        :param timeout: 超时等待时间
        :return: 元素成功定位返回元素对象，超时未找到则返回None
        """
        try:
            element = WebDriverWait(cls.driver, timeout, freq).until(ec.presence_of_element_located((prop, value)))
            cls.logger.info('元素定位成功')
            return element
        except TimeoutException:
            cls.logger.error('超时未找到元素')
            return None

    @classmethod
    def is_element_present(cls, prop, value, freq=0.5, timeout=5):
        """
        根据wait_element_present方法的返回值返回相应的布尔值,方便断言
        :param prop: 定位方法
        :param value: 定位方法对应的值
        :param freq: 搜索元素频率
        :param timeout: 超时等待时间
        :return: 元素成功定位则返回True，如果为None则返回False
        """
        element = cls.wait_element_present(prop, value, freq, timeout)
        if element is not None:
            return True
        return False

    @classmethod
    def tap_element(cls, element):
        """
        点击元素的中心坐标位置
        :param element: 元素对象
        :return:
        """
        try:
            myrect = element.rect
            x = int(myrect['x'] + myrect['width'] / 2)
            y = int(myrect['y'] - myrect['height'] / 2)
            actions = ActionChains(cls.driver)
            actions.w3c_actions.devices = []
            finger1 = actions.w3c_actions.add_pointer_input('touch','finger1')
            finger1.add_pointer_action('pointerMove', x=x, y=y)
            finger1.add_pointer_action('pointerDown')
            finger1.add_pointer_action('pointerUp')
            actions.perform()
            cls.logger.info('元素成功点击中心')
        except:
            cls.logger.error('元素中心点击异常')
            raise
