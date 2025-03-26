import json5
import os
from tools.logger import Logger


class ReadJson:

    logger = Logger.get_logger()

    @classmethod
    def read_json(cls, jsonpath):
        """
        用于读取json格式文件数据，正常返回值为包含json文件数据的python对象，出现异常返回None
        :param jsonpath: json格式文件路径
        :return: python对象或None
        """
        try:
            # 使用with open以只读模式，utf8编码格式打开json文件
            with open(jsonpath, encoding='utf8') as f:
                # load(loads)读取文件(json格式字符串)得到python对象
                # dump(dumps)字典转化写入json文件（转化为json字符串）
                contents = json5.load(f)
            cls.logger.info(f'{os.path.basename(jsonpath)}读取成功')
            return contents
        except:
            cls.logger.error(f'{os.path.basename(jsonpath)}读取出现异常')
            return None


if __name__ == '__main__':
    content = ReadJson.read_json('../config/ele.conf')
    print(content)
