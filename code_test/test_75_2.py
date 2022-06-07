from .code_75 import *
from .code_75 import find_tuples


def test():
    assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == '[(8, 16, 4)]'