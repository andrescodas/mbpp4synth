from .code_330 import *
from .code_330 import find_char


def test():
    assert find_char('Certain service are subject to change MSR') == ['are', 'MSR']