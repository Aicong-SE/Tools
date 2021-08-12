import redis


class RedisTools:
    """
    redis 数据库工具
    """

    def __init__(self, host, port, password, db=0):
        """
        :param host: 主机
        :param port: 端口
        :param password: 密码
        :param db: 数据库
        """
        self._host = host
        self._port = port
        self._password = password
        self._db = db
        self._redis_db = self._connect_redis_db()

    def _connect_redis_db(self):
        """
        连接 redis 数据库
        """
        redis_db = redis.StrictRedis(host=self._host, port=self._port, password=self._password, db=self._db, decode_responses=True)
        return redis_db

    def set(self, key, value, ex=None, px=None, nx=False, xx=False):
        """
        将键值对存入 redis
        :param key: 键
        :param value: 值
        :param ex: 过期时间 （单位：秒）
        :param px: 过期时间 （单位：毫秒）
        :param nx: 若为 True 当键不存在时执行
        :param xx: 若为 True 当键存在时执行
        """
        self._redis_db.set(key, value, ex=ex, px=px, nx=nx, xx=xx)

    def get(self, key):
        """
        获取指定键的值
        :param key: 键
        """
        return self._redis_db.get(key)

    def incr(self, key):
        """
        指定鍵的值+1
        :param key: 键
        """
        return self._redis_db.incr(key)

    def incrbyfloat(self, key, amount: float):
        """
        指定鍵的值加指定数值
        :param key: 键
        :param amount: 数值 浮点数
        """
        return self._redis_db.incrbyfloat(key, amount)

    def decr(self, key, amount: int):
        """
        指定键的值减指定数值
        :param key: 键
        :param amount: 数值
        """
        return self._redis_db.decr(key, amount)

    def append(self, key, value: str):
        """
        指定键的值后面增加指定字符串
        :param key: 键
        :param value: 值
        """
        return self._redis_db.append(key, value)
