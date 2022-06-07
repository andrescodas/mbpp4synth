from .code_607 import *
from .code_607 import find_literals


def test():
    assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)