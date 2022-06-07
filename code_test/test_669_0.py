from .code_669 import *
from .code_669 import check_IP


def test():
    assert check_IP("192.168.0.1") == 'Valid IP address'