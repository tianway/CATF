from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
from tools.logger import Logger
from tools.read_yaml import ReadYaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


# 定义返回单例模式中driver的类
class MyWebDriver:
    # 定义类属性，在整个生命周期中将会保持地址的唯一性
    # driver默认值定为none，为了判断里边是否有driver
    driver = None

    logger = Logger.get_logger()
    config = ReadYaml.read_yaml()

    @classmethod
    def start(cls,
              browser=config['webdriver']['browser'],
              url=config['webdriver']['url']):
        """
        启动webdriver，并将webdriver对象返回
        :param browser: 浏览器名称
        :param url: 初始打开的网页
        :return: webdriver对象
        """
        try:
            # 判断webdriver是否存在，存在则直接返回，不存在就执行实例化driver的操作
            if cls.driver is None:
                cls.driver = getattr(webdriver, browser)()
                cls.logger.info('webdriver正常启动')
                # 和浏览器相关的操作实例化
                cls.driver.maximize_window()  # 最大化
                cls.driver.implicitly_wait(5)  # 隐式等待
                cls.driver.get(url)  # 打开url（项目主页面）
                cls.logger.info('打开初始网页成功')
            return cls.driver
        except:
            cls.logger.error('webdriver启动异常')
            raise

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
    def input(cls, elem, value):
        """
        输入框输入的操作的封装
        :param elem: 元素对象
        :param value: 要输入的文本
        :return: 无
        """
        try:
            elem.click()
            elem.clear()
            elem.send_keys(value)
            cls.logger.info(f'元素成功输入{value}')
        except:
            cls.logger.error('元素输入失败')
            raise

    @classmethod
    def select_rand(cls, elem):
        """
        下拉框随机选择操作的封装
        :param elem: 元素对象
        :return: 无
        """
        try:
            s1 = Select(elem)
            s1.select_by_index(random.randint(0, len(s1.options) - 1))
            cls.logger.info('下拉框随机选择成功')
        except:
            cls.logger.error('下拉框随机选择失败')
            raise

    @classmethod
    def scroll_top(cls, elem, distance=10000):
        """
        滚动条垂直滚动控制方法
        :param elem:元素对象
        :param distance:垂直滚动距离
        :return:无
        """
        try:
            dr = cls.start()
            dr.execute_script(f"arguments[0].scrollTop={distance};", elem)
            cls.logger.info(f'滚动条垂直滚动{distance}')
        except:
            cls.logger.error('滚动条垂直滚动失败')
            raise


if __name__ == '__main__':
    driver = MyWebDriver.start()
    driver.quit()
