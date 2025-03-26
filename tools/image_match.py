import cv2
import os
import time
from PIL import ImageGrab
from tools.read_yaml import ReadYaml
from tools.logger import Logger
from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.keyboard import Key


class ImageMatch:

    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        self.logger = Logger.get_logger()
        self.similarity = float(ReadYaml.read_yaml()['imageMatch']['similarity'])

    def find_image(self, target):
        """
        通过OpenCV进行模板匹配，返回匹配的坐标，未找到返回(-1,-1),异常返回-1
        :param target: 模板图片的名称
        :return: 坐标元组
        """
        images_path = '../tools/images'
        screen_path = os.path.join(images_path, 'screen_shot.png')
        try:
            ImageGrab.grab().save(screen_path)
            # 大图对象
            screen = cv2.imread(screen_path)
            # 小图对象
            template = cv2.imread(os.path.join(images_path, target))
            # 进行模板匹配
            result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
            # 获取匹配的结果
            min, max, min_loc, max_loc = cv2.minMaxLoc(result)
            # 使用max和相似度similarity进行检查
            if max < self.similarity:
                self.logger.error(f'{target}匹配失败')
                return -1, -1
            x = max_loc[0] + int(template.shape[1] / 2)
            y = max_loc[1] + int(template.shape[0] / 2)
            self.logger.info(f'{target}匹配成功，坐标为({x},{y})')
            return x, y
        except:
            self.logger.error('模板匹配出现异常，请检查模板图片路径是否正确')
            raise

    def check_img_exists(self, target):
        """
        检查一个模板照片是否存在，存在返回True否则返回False
        :param target: 模板图片的名称
        :return: True或False
        """
        try:
            x, y = self.find_image(target)
            return x != -1 and y != -1
        except:
            raise

    def click(self, target):
        """
        在模板匹配到的位置进行鼠标左键单击操作
        :param target: 模板图片的名称
        :return: 成功返回1，失败返回0
        """
        try:
            x, y = self.find_image(target)
            if x != -1 and y != -1:
                self.mouse.position = (x, y)
                time.sleep(1)
                self.mouse.click(Button.left, 1)
                self.logger.info(f'在({x},{y})位置左键单击了{target}')
                time.sleep(0.5)
                return 1
            self.logger.info(f'{target}未匹配到，左键单击失败')
            return 0
        except:
            self.logger.error(f'{target}匹配出现异常，左键单击失败')
            raise

    def double_click(self, target):
        """
        在模板匹配到的位置进行鼠标左键双击操作
        :param target: 模板图片的名称
        :return: 成功返回1，失败返回0
        """
        try:
            x, y = self.find_image(target)
            if x != -1 and y != -1:
                self.mouse.position = (x, y)
                time.sleep(1)
                self.mouse.click(Button.left, 2)
                self.logger.info(f'在({x},{y})位置左键双击了{target}')
                time.sleep(0.5)
                return 1
            self.logger.info(f'{target}未匹配到，左键双击失败')
            return 0
        except:
            self.logger.error(f'{target}匹配出现异常，左键双击失败')
            raise

    def right_click(self, target):
        """
        在模板匹配到的位置进行鼠标右键单击操作
        :param target: 模板图片的名称
        :return: 成功返回1，失败返回0
        """
        try:
            x, y = self.find_image(target)
            if x != -1 and y != -1:
                self.mouse.position = (x, y)
                time.sleep(1)
                self.mouse.click(Button.right, 1)
                self.logger.info(f'在({x},{y})位置右键单击了{target}')
                time.sleep(0.5)
                return 1
            self.logger.info(f'{target}未匹配到，右键单击失败')
            return 0
        except:
            self.logger.error(f'{target}匹配出现异常，右键单击失败')
            raise

    def input(self, target, content):
        """
        对图片执行输入操作
        :param target: 模板图片文件的名称
        :param content: 是要输入的内容
        :return: 成功返回1，失败返回0
        """
        try:
            if self.double_click(target) == 1:
                self.keyboard.type(content)
                self.logger.info(f'在{target}所在位置输入了{content}')
                time.sleep(0.5)
                return 1
            self.logger.info(f'{target}未匹配到，对图片执行输入失败')
            return 0
        except:
            self.logger.error(f'{target}匹配出现异常，对图片执行输入失败')
            raise

    def select(self, target, count):
        """
        选择下拉框的某一项
        :param target: 模板图片文件的名称
        :param count: 按向下键的次数
        :return: 成功返回1，失败返回0
        """
        try:
            if self.click(target) == 1:
                for i in range(count):
                    self.keyboard.press(Key.down)
                    time.sleep(0.5)
                self.keyboard.press(Key.enter)  # 回车
                self.logger.info(f'{target}所在位置的下拉框选择了第{count + 1}项')
                time.sleep(0.5)
                return 1
            self.logger.info(f'{target}未匹配到，对下拉框选择操作失败')
            return 0
        except:
            self.logger.error(f'{target}匹配出现异常，对下拉框选择操作失败')
            raise
