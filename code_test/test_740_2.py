from .code_740 import *
from .code_740 import tuple_to_dict


def test():
    assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}