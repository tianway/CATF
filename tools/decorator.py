from functools import wraps


class Decorator:

    @classmethod
    def get_cost_time(cls, func):
        """
        打印函数运行时间功能的装饰器
        :param func: 被装饰函数对象
        :return: 装饰后的函数对象
        """
        import time

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            re = func(*args, **kwargs)
            end_time = time.time()
            cost_time = end_time - start_time
            print(f"{func.__name__}运行花费时间为{cost_time}")
            return re

        return wrapper

    @classmethod
    def highlight(cls, func):
        """
        高亮定位元素的装饰器
        :param func: 被装饰函数对象
        :return: 装饰后的函数对象
        """
        from driver.web_driver import MyWebDriver

        def apply_style(element):
            js = "arguments[0].style.border='6px solid red'"
            # 定位到元素后，执行js样式
            MyWebDriver.driver.execute_script(js, element)

        @wraps(func)
        def wrapper(*args, **kwargs):
            element = func(*args, **kwargs)
            apply_style(element)
            return element

        return wrapper
