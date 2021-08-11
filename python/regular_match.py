"""
正则匹配

提供与正则相关的方法
"""
import re


def re_funcition():
    """
    正则相关的内置方法
    """
    pattern = "(.*?) .*"  # 正则表达式
    string = "Hello World"  # 字符串
    re_res = re.match(pattern, string, flags=re.M | re.I)
    # region flags 标志位
    # re.I 使匹配对大小写不敏感
    # re.L 做本地化识别（locale-aware）匹配
    # re.M 多行匹配，影响 ^ 和 $
    # re.S 使 . 匹配包括换行在内的所有字符
    # re.U 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    # re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
    # endregion
    print(re_res.group())  # 获取匹配到的字符串
    print(re_res.group(1))  # 获取组 1 匹配到的字符串


if __name__ == '__main__':
    re_funcition()
