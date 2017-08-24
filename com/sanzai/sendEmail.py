from email.mime.text import MIMEText
from email.header import Header
from com.sanzai.testDemo import _format_addr
from com.sanzai.testOne import from_addr, smtp_server
import smtplib


def _sendaTextMsgToEmail(to_addr, msg, hint):

    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['From'] = _format_addr(from_addr)
    msg['To'] = _format_addr(to_addr)
    msg['Subject'] = Header(hint, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    # server.set_debuglevel(1)  # 打印日志

    password = input('password:')
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


_sendaTextMsgToEmail('525599972@qq.com', '自定义的内容', '自定义的标题')