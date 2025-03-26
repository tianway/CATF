from tools.image_match import ImageMatch
from tools.logger import Logger
import os
import time


class ImageTestAPP:
    def __init__(self):
        self.image_match = ImageMatch()
        self.logger = Logger.get_logger()

    def start_app(self, cmd):
        """
        通过命令方式启动应用程序
        :param cmd: 打开程序的命令字符串
        :return:
        """
        try:
            os.system(f'start /b {cmd}')
            self.logger.info('应用程序启动成功')
            time.sleep(2)
        except Exception:
            self.logger.error("应用程序启动出现异常")
            raise

    def calc_mult(self, cmd):
        self.start_app(cmd)
        self.image_match.input('num1.png', '1')
        self.image_match.input('num2.png', '2')
        self.image_match.select('select.png', 2)
        self.image_match.click('calc.png')
        if self.image_match.check_img_exists('result.png'):
            print('ok')
        self.image_match.click('close.png')


if __name__ == '__main__':
    ImageTestAPP().calc_mult('java -jar JavaSwingCalc.jar')
