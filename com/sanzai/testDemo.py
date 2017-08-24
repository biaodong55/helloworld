from email.utils import parseaddr, formataddr
from email.header import Header

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))