"""
加密工具

提供一些加密的方法
"""
import hashlib
import hmac


class Encryption:
    """
    加密
    """

    @staticmethod
    def encode_md5(s):
        """
        md5加密
        MD5消息摘要算法
        不可逆
        :param s: 字符串
        """
        return hashlib.md5(s.encode()).hexdigest()

    @staticmethod
    def encode_sha1(s):
        """
        sha1加密
        安全哈希算法
        不可逆，比 md5 安全性强
        :param s: 字符串
        """
        sha1 = hashlib.sha1()
        sha1.update(s.encode('utf-8'))
        return sha1.hexdigest()

    @staticmethod
    def encode_hmac(s, key, digestmod):
        """
        hmac加密
        三列消息鉴别码
        """
        mac = hmac.new(key.encode(), s.encode(), digestmod)
        mac.digest()
        return mac.hexdigest()


if __name__ == '__main__':
    ss = "asc"
    print(Encryption().encode_md5(ss))
    # print(Encryption().encode_sha1(ss))
    print(Encryption().encode_hmac(ss, "asc", hashlib.md5))
