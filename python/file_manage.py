"""
文件管理

提供与文件相关的方法
"""
import os
from pathlib import Path


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


def create_file(url: str) -> None:
    """
    创建文件
    创建文件时如果路径不存在会创建这个路径
    :param url: 文件路径
    """
    os.makedirs(url)