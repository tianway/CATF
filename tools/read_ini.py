import configparser
from tools.logger import Logger
import os


class ReadINI:

    logger = Logger.get_logger()

    @classmethod
    def get_content(cls, filenames, section, option, encoding='utf8'):
        """
        读取ini文件中的配置内容并返回
        :param filenames: 配置文件名
        :param section: 节点名
        :param option: 配置项名
        :param encoding: 编码格式
        :return: 无异常返回配置内容，出现异常时返回None
        """
        try:
            cp = configparser.ConfigParser()
            cp.read(filenames, encoding=encoding)
            content = cp.get(section, option)
            cls.logger.info(f'成功读取{os.path.basename(filenames)}文件{section}节点中{option}的内容')
            return content
        except:
            cls.logger.error(f'读取{os.path.basename(filenames)}文件{section}节点中{option}的内容时出现异常')
            return None


if __name__ == '__main__':
    print(ReadINI.get_content('../config/base.ini', 'mysql', 'db_info'))
