class Logger:
    # 日志生成器作为类属性
    logger = None

    @classmethod
    def get_logger(cls):
        """
            返回规定格式的日志生成器对象
        :return: 日志生成器对象
        """
        if cls.logger is None:
            import logging
            # 得到生成器对象
            cls.logger = logging.getLogger()
            # 定义该logger所支持的日志级别
            cls.logger.setLevel(level=logging.INFO)
            # 创建logger的文件句柄与规定的文件关联
            handler = logging.FileHandler('..\\logs\\' + cls.get_ctime_str() + '.log', encoding='utf8')
            # 定义信息的格式
            formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls.logger.addHandler(handler)
            cls.logger.info('******************************************************')
        return cls.logger

    @classmethod
    def get_ctime_str(cls):
        """
            返回规定格式的时间字符串
        :param : 无
        :return: 时间字符串
        """
        import time
        return time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())


if __name__ == '__main__':
    print(Logger.get_ctime_str())
