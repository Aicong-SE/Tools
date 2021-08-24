import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing import Process


class ToolMail:
    """
    邮件   asc版
    """

    def __init__(self, username: str, password: str):
        """
        初始化
        :param username: 用户名
        :param password: 密码
        """
        self._username = username
        self._password = password
        self._smtp_host, self._smtp_port = self._get_smtp_host_port()

    def _get_smtp_host_port(self) -> (str, int):
        """
        获取 SMTP 的 host 和 port
        :return: host, port
        """
        suffix = self._username.split("@")[-1]
        if suffix in ["mail.fgff.com"]:
            return "mx.fgff.com", 465

    @staticmethod
    def _map_mail(mail_list: list) -> list:
        """
        映射邮箱
        :param mail_list: 邮箱列表
        :return: 映射后邮箱列表
        """
        res = []
        for item in mail_list:
            if item.endswith("zmate.cn"):
                item = item.split("@")[0] + "@mail.fgff.com"
            res.append(item)
        return res

    def send_mail(self, mail_to: list, title: str, message: str, accessory: list = [], imgs: list = []):
        """
        发送邮件
        :param mail_to: 接受者
        :param title: 标题
        :param message: 内容
        :param accessory: 附件 [路径1，路径2...]
        :param imgs: 图片 [(id, url)]
        """
        mail_to = self._map_mail(mail_to)

        msg = MIMEMultipart()
        msg["Subject"] = Header(s=title, charset="utf-8")
        msg["From"] = Header(s=self._username)
        msg["To"] = Header(s="; ".join(mail_to))
        # 正文
        message = '<html><head><meta charset="UTF-8"></head><body>' + message + '</body></html>'
        msg.attach(payload=MIMEText(_text=message, _subtype="html", _charset="utf-8"))
        # 附件
        for file_path in accessory:
            att = MIMEText(_text=open(file_path, "rb").read(), _subtype="base64", _charset="utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = "attachment; filename=%s" % file_path
            msg.attach(payload=att)
        # 图片
        for img_id, img_url in imgs:
            msg_image = MIMEImage(open(img_url, "rb").read())
            msg_image.add_header('Content-ID', f'<{img_id}>')
            msg.attach(msg_image)

        smtp_obj = smtplib.SMTP_SSL(host=self._smtp_host, port=self._smtp_port, timeout=60 * 5)
        smtp_obj.login(user=self._username, password=self._password)
        smtp_obj.sendmail(from_addr=self._username, to_addrs=mail_to, msg=msg.as_string())
        smtp_obj.quit()
        print(f"已发送: {mail_to}")

    def send_mail_async(self, mail_to: list, title: str, message: str, accessory: list = [], imgs: list = []):
        """
        异步发送邮件
        :param mail_to: 接受者
        :param title: 标题
        :param message: 内容
        :param accessory: 附件 [路径1，路径2...]
        :param imgs: 图片 [(id, url)]
        """
        p = Process(target=self.send_mail, args=(mail_to, title, message, accessory, imgs))
        p.start()


if __name__ == '__main__':
    tm = ToolMail("mail", "pwd")
    tm.send_mail_async(
        mail_to=["mail"],
        title='test',
        message='<img src="cid: img1"><img src="cid:img2"><img src="cid:img3">',
        # accessory=[],
        imgs=[('img1', "./imgs/btc_usdt.jpg"), ('img2', "./imgs/eth_usdt.jpg"), ('img3', "./imgs/dot_usdt.jpg")],
    )
