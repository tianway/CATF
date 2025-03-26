import pymysql
from tools.read_yaml import ReadYaml
from tools.logger import Logger


class EasyMysql:
    # 读取配置文件信息
    db_info = ReadYaml.read_yaml()['mysql']
    logger = Logger.get_logger()

    @classmethod
    def _get_connection(cls):
        """
        获取数据库连接
        :return: 数据库连接对象
        """
        try:
            conn = pymysql.connect(
                host=cls.db_info['ip'],
                user=cls.db_info['user'],
                password=cls.db_info['password'],
                database=cls.db_info['dbname'],
                charset=cls.db_info['encode']
            )
            cls.logger.info('数据库连接成功')
            return conn
        except Exception as e:
            cls.logger.error(f'数据库连接失败，错误信息: {e}')
            raise

    @classmethod
    def query_one(cls, sql):
        """
        连接数据库查询并返回一条查询记录，异常时返回None
        :param sql: sql语句
        :return: 一条查询结果的元组或None
        """
        cls.logger.info(f'执行SQL查询: {sql}')
        try:
            with cls._get_connection() as conn, conn.cursor() as cursor:
                cursor.execute(sql)
                query_result = cursor.fetchone()
                cls.logger.info('数据查询完成')
                return query_result
        except Exception as e:
            cls.logger.error(f'查询出现异常，错误信息: {e}')
            raise

    @classmethod
    def query_all(cls, sql):
        """
        连接数据库查询返回全部查询记录，异常时返回None
        :param sql: sql语句
        :return: 所有查询结果的元组或None
        """
        cls.logger.info(f'执行SQL查询: {sql}')
        try:
            with cls._get_connection() as conn, conn.cursor() as cursor:
                cursor.execute(sql)
                query_result = cursor.fetchall()
                cls.logger.info('数据查询完成')
                return query_result
        except Exception as e:
            cls.logger.error(f'查询出现异常，错误信息: {e}')
            raise

    @classmethod
    def update(cls, sql):
        """
        连接数据库执行更新数据库语句，成功返回True，出现异常返回False
        :param sql: sql语句
        :return: True或False
        """
        cls.logger.info(f'执行SQL更新: {sql}')
        try:
            with cls._get_connection() as conn, conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
                cls.logger.info('数据更新完成')
                return True
        except Exception as e:
            cls.logger.error(f'更新出现异常，错误信息: {e}')
            raise


if __name__ == '__main__':
    result = EasyMysql.query_all('select * from user')
    print(result)
    result1 = EasyMysql.query_one('select * from user')
    print(result1)
