import requests
from tools.read_yaml import ReadYaml
from tools.logger import Logger


class TestAPI:
    session = requests.session()
    baseURL = ReadYaml.read_yaml()['requests']['baseURL']
    logger = Logger.get_logger()

    @classmethod
    def post(cls, data):
        """
        以post方法发送接口测试请求
        :param data: 接口测试数据
        :return: 正常返回响应对象，异常返回None
        """
        try:
            url = cls.baseURL + data['uri']
            headers = data['headers']
            data = data['data']
            resp = cls.session.post(url=url, headers=headers, data=data)
            cls.logger.info("post请求发送成功")
            return resp
        except:
            cls.logger.error('post请求发送失败')
            raise

    @classmethod
    def get(cls, data):
        """
        以get方法发送接口测试请求
        :param data: 接口测试数据
        :return: 正常返回响应对象，异常返回None
        """
        try:
            url = cls.baseURL + data['uri']
            resp = cls.session.get(url=url)
            cls.logger.info("get请求发送成功")
            return resp
        except:
            cls.logger.error('get请求发送失败')
            raise
