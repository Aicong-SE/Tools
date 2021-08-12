"""
文件管理

提供与文件相关的方法
"""
import os
from pathlib import Path


# region 判断文件与目录是否存在
def file_exists(url: str) -> bool:
    """
    检查指定的文件是否存在
    :param url: 文件的路径
    :return: true 存在  false 不存在
    """
    return Path(url).is_file()


def directory_exists(url: str) -> bool:
    """
    检查指定的目录是否存在
    :param url: 目录的路径
    :return: true 存在  false 不存在
    """
    return Path(url).is_dir()


def exists(url: str) -> bool:
    """
    检查指定的文件或目录是否存在
    :param url: 文件或目录的路径
    :return: true 存在  false 不存在
    """
    return Path(url).exists()


# endregion

# region 创建与删除文件与目录
def create_directory(url: str) -> None:
    """
    创建目录
    创建目录时如果路径不存在会创建这个路径
    :param url: 目录路径
    """
    os.makedirs(url)


def create_file(url: str) -> None:
    """
    创建文件
    创建文件时如果路径不存在会创建这个路径
    :param url: 文件路径
    """
    file = open(url, 'w')
    file.close()


def delete_file(url: str) -> None:
    """
    删除文件
    """
    os.remove(url)


# endregion

# region 读写文件
def write_file(url: str, mode: str, content: str) -> None:
    """
    将内容写入文件
    :param url: 文件路径
    :param mode: 文件打开类型  w 清空重写  a 不清空，增量写入
    :param content: 内容
    """
    if mode not in ["w", "a"]:
        raise Exception("请传入正确的 mode 值")
    with open(url, mode) as f:
        f.write(content)


def read_file(url: str) -> str:
    """
    读取文件全部内容
    :param url: 文件路径
    :return: 全部内容
    """
    with open(url, 'r') as f:
        return f.read()


def read_lines_file(url: str):
    """
    按行读取文件
    :param url: 文件路径
    :yield: 每行字符串  可迭代对象
    """
    with open(url, 'r') as f:
        for item in f.readline():
            yield item


# endregion

# region 文件名操作
def get_file_name(url: str) -> list:
    """
    获取文件名
    将指定目录路径下的所有 文件名与目录名 以列表形式返回
    :param url: 目录路径
    """
    return os.listdir(url)


def file_name_funcition():
    """
    关于文件名的一些方法
    """
    file_name = "E:/test/t.lib"
    print(os.path.splitext(file_name))  # ('E:/test/t', '.lib')  拆分 文件名 和 后缀
    print(os.path.split(file_name))  # ('E:/test', 't.lib')  拆分 路径 和 文件名


# endregion


if __name__ == '__main__':
    file_name_funcition()
