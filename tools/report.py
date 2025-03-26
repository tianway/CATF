import os
import smtplib
import zipfile
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Report:

    def __init__(self, version):
        self.version = version

    # 打包压缩:明确要打包压缩的内容，明确压缩文件的位置和名字，执行打包压缩动作
    def compress_file(self, dirpath='../test_report'):

        # 要压缩的文件夹的父目录和压缩文件所在的目录
        zipfile_root = dirpath
        zip_file = os.path.join(os.getcwd(), f'ITF_report_{self.version}.rar')
        # 构造zip压缩文件对象
        zip = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_LZMA)

        filelist = []

        # 利用python自带的os.walk方法来实现遍历文件夹的操作
        # root代表每一级文件夹的根目录，folders代表这一级目录下的目录集合，filename代表这一级目录下的文件集合
        for root, folders, filenames in os.walk(zipfile_root):
            for folder in folders:
                filelist.append(os.path.join(root, folder))
            for filename in filenames:
                filelist.append(os.path.join(root, filename))

        for file in filelist:
            print(file)
            zip.write(file, os.path.basename(file))

        zip.close()

    # 使用递归方式对文件夹进行遍历
    def find_file(self, folder):
        filelist = []
        for item in os.listdir(folder):
            path = os.path.join(folder, item)
            filelist.append(path)
            if os.path.isdir(path):
                self.find_file(path)
        return filelist

    # 邮件发送.attachment附件
    def send_mail(self, content, head, attachment, sender=None, receivers=None):
        # 定义收件人（多个）和发件人
        if receivers is None:
            receivers = ['312458641@qq.com']
        if sender is None:
            sender = "tianyuanliu111@126.com"
        # MIMEText用于构造邮件正文，有3个参数
        # 第一个参数用于正文内容，第二个参数是说明正文的类型比如纯文本或者html，第3个参数是编码类型
        content = MIMEText(content, 'text', 'utf-8')
        header = Header(head, 'utf-8')

        # 带附件的邮件处理方式
        message = MIMEMultipart()
        message.attach(content)
        message['Subject'] = header

        # 使用open读取附件文件的内容
        with open(attachment, 'rb') as file:
            # 使用MIMEApplication(file.read())
            attach = MIMEApplication(file.read())
            attach.add_header('Content-Dispositon', 'attachment', filename=os.path.basename(attachment))
        message.attach(attach)

        try:
            smtp = smtplib.SMTP()
            # 如果有SSL加密协议的邮件网站发送
            # smtp = smtplib.SMTP_SSL()
            # 和发件人邮件建立连接
            smtp.connect('smtp.126.com', 25)
            # 输入发件人的邮箱的账号密码
            smtp.login(sender, '15806978725asd!')
            # 将发送的内容转成字符串
            smtp.sendmail(sender, receivers, message.as_string())
            print('发送邮件成功')
        except smtplib.SMTPException:
            print('发送邮件失败')


if __name__ == '__main__':
    Report('v1').compress_file()
    Report('v1').send_mail('测试报告见附件', '测试报告发送', './ITF_report_v1.rar')
