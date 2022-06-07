from .code_740 import *
from .code_740 import tuple_to_dict


def test():
    assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}