from .code_607 import *
from .code_607 import find_literals


def test():
    assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)