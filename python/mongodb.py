"""
mongo 数据库

建立使用 MongoDB 的类
"""

from pymongo import MongoClient


class MongoDb:
    """
    使用 mongo 数据库
    """

    def __init__(self, host, port, user_name, password, db):
        """
        :param host: 主机
        :param port: 端口
        :param user_name: 用户名
        :param password: 密码
        :param db: 数据库
        """
        self._host = host
        self._port = port
        self._user_name = user_name
        self._password = password
        self._db = db
        self._mongo_db = self._connect_mongo_db()

    def _connect_mongo_db(self):
        """
        连接 mongo 数据库
        """
        mongo_client = MongoClient(self._host, self._port)
        mongo_client[self._db].authenticate(self._user_name, self._password)
        mongo_db = mongo_client[self._db]
        return mongo_db

    def insert_one(self, collection_name, document):
        """
        向集合中插入一个文档
        :param collection_name: 集合名
        :param document: 文档
        """
        return self._mongo_db[collection_name].insert_one(document=document)

    def insert_many(self, collection_name, documents):
        """
        向集合中插入多个文档
        :param collection_name: 集合名
        :param documents: 多个文档
        """
        return self._mongo_db[collection_name].insert_one(document=documents)

    def find_one(self, collection_name, filter=None, projection=None):
        """
        从集合中获取单个文档，若查询到多个，则返回第一个
        :param collection_name: 集合名
        :param filter: 过滤器
        :param projection: 指定返回的字段，{"_id": False}
        """
        return self._mongo_db[collection_name].find_one(filter=filter, projection=projection)

    def find(self, collection_name, filter=None, projection=None, limit=0, sort=None):
        """
        从集合中获取所有文档
        :param collection_name: 集合名
        :param filter: 过滤器  {"_id": {"$regex": "^r", "$gt": "H"}}
        :param projection: 指定返回的字段，{"_id": False}
        :param limit: 返回数据条数
        :param sort: 排序
        """
        return self._mongo_db[collection_name].find(filter=filter, projection=projection, limit=limit, sort=sort)

    def update_one(self, collection_name, filter, update):
        """
        更新集合中单个文档，若得到多个文档，则修改第一个
        :param collection_name: 集合名
        :param filter: 过滤器
        :param update: 更新信息
        """
        return self._mongo_db[collection_name].update_one(filter=filter, update=update)

    def update_many(self, collection_name, filter, update):
        """
        更新集合中多个文档
        :param collection_name: 集合名
        :param filter: 过滤器
        :param update: 更新信息
        """
        return self._mongo_db[collection_name].update_one(filter=filter, update=update)

    def delete_one(self, collection_name, filter):
        """
        删除集合中单个文档
        :param collection_name: 集合名
        :param filter: 过滤器
        """
        return self._mongo_db[collection_name].delete_one(filter=filter)

    def delete_many(self, collection_name, filter):
        """
        删除集合中多个文档
        :param collection_name: 集合名
        :param filter: 过滤器
        """
        return self._mongo_db[collection_name].delete_many(filter=filter)

    def get_collections(self):
        """
        Get a list of all the collection names in this database.
        :return:
        """
        return self._mongo_db.list_collection_names()
