from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header

from_addr = 'biaodong55@126.com'
password = 'WO158369'
smtp_server = 'smtp.126.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def _sendaTextMsgToEmail(receive, msg, hint):

    to_addr = receive

    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['From'] = _format_addr(from_addr)
    msg['To'] = _format_addr(to_addr)
    msg['Subject'] = Header(hint, 'utf-8').encode()

    import smtplib

    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    # server.set_debuglevel(1)  # 打印日志
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


_sendaTextMsgToEmail('525599972@qq.com', '自定义的内容', '自定义的标题')
