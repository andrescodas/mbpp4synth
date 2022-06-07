from .code_740 import *
from .code_740 import tuple_to_dict


def test():
    assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}