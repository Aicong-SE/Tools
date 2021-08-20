"""
加密工具

提供一些加密的方法
"""
import hashlib
import hmac
import base64

from Crypto.Cipher import AES

import rsa


class Encryption:
    """
    加密
    """

    @staticmethod
    def encode_md5(s):
        """
        md5加密
        MD5消息摘要算法
        哈希算法，不可逆
        :param s: 字符串
        """
        return hashlib.md5(s.encode()).hexdigest()

    @staticmethod
    def encode_sha1(s):
        """
        sha1加密
        安全哈希算法
        哈希算法，不可逆，比 md5 安全性强
        :param s: 字符串
        """
        sha1 = hashlib.sha1()
        sha1.update(s.encode('utf-8'))
        return sha1.hexdigest()

    @staticmethod
    def encode_hmac(s, key, digestmod):
        """
        hmac加密
        散列消息鉴别码
        哈希算法， 不可逆
        :param s: 字符串
        :param key: 私钥
        :param digestmod: 加密方式
        """
        mac = hmac.new(key.encode(), s.encode(), digestmod)
        mac.digest()
        return mac.hexdigest()

    @staticmethod
    def _add_to_16(s):
        """
        若str不是16的倍数那就补足为16的倍数
        """
        while len(s) % 16 != 0:
            s += '\0'
        return str.encode(s)  # 返回bytes

    def encode_aes(self, s, key):
        """
        aes加密
        高级加密标准
        可逆
        :param s: 字符串
        :param key: 私钥
        """
        aes = AES.new(self._add_to_16(key), AES.MODE_ECB)  # 初始化加密器
        encrypt_aes = aes.encrypt(self._add_to_16(s))  # 先进行aes加密
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').replace('\n', '')  # 执行加密并转码返回bytes
        return encrypted_text

    def decode_aes(self, s, key):
        """
        aes解密
        高级加密标准
        可逆
        :param s: 字符串
        :param key: 私钥
        """
        aes = AES.new(self._add_to_16(key), AES.MODE_ECB)  # 初始化加密器
        base64_decrypted = base64.decodebytes(s.encode(encoding='utf-8'))  # 优先逆向解密base64成bytes
        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')  # 执行解密密并转码返回str
        return decrypted_text


class RSAEncryption:
    def __init__(self, public_key_url="./public_key.pem", private_key_url="./private_key.pem"):
        self._public_key_url = public_key_url
        self._private_key_url = private_key_url
        self._public_key, self._private_key = self._get_key()

    def _get_key(self):
        """
        根据 key_url 获取 key
        :return: 公钥， 私钥
        """
        with open(self._public_key_url, "r") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read().encode())
        with open(self._private_key_url, "r") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read().encode())
        return public_key, private_key

    def encode(self, s):
        return rsa.encrypt(s.encode(), self._public_key)

    def decode(self, s):
        return rsa.decrypt(s, self._private_key).decode()

    def generate_key(self):
        """
        生成公钥和私钥
        """
        public_key, private_key = rsa.newkeys(2048)
        with open(self._public_key_url, "wb") as f:
            f.write(public_key.save_pkcs1())
        with open(self._private_key_url, "wb") as f:
            f.write(private_key.save_pkcs1())


if __name__ == '__main__':
    ss = "123"
    # print(Encryption().encode_md5(ss))
    # print(Encryption().encode_sha1(ss))
    # print(Encryption().encode_hmac(ss, "asc", hashlib.md5))
    # print(Encryption().encode_aes(ss, "asc"))
    # print(Encryption().decode_aes("LUmJgR533AfCKw8S7yNQ9A==", "asc"))

    r = RSAEncryption()
    # r.generate_key()
    res = r.encode(ss)
    print(res)
    print(r.decode(res))
