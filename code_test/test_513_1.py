from .code_513 import *
from .code_513 import add_str


def test():
    assert add_str((7, 8, 9, 10) , "PF") == [7, 'PF', 8, 'PF', 9, 'PF', 10, 'PF']