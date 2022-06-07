from .code_301 import *
from .code_301 import dict_depth


def test():
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3