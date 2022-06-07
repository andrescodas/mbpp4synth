from .code_301 import *
from .code_301 import dict_depth


def test():
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4