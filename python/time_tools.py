import time


def _timestamp_in_time(timestamp: float, time_format: str = '%Y-%m-%d %H:%M:%S'):
    """
    时间戳转时间
    :param timestamp: 时间戳 （单位：秒）
    :param time_format: 格式
    """
    return time.strftime(time_format, time.localtime(timestamp))


def _time_in_timestamp(time_str: str, time_format: str = '%Y-%m-%d %H:%M:%S'):
    """
    时间转时间戳
    :param time_str: 时间
    :param time_format: 格式
    """
    return time.mktime(time.strptime(time_str, time_format))
