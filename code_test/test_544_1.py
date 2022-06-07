from .code_544 import *
from .code_544 import flatten_tuple


def test():
    assert flatten_tuple([('2', '3', '4'), ('6', '9'), ('3', '2'), ('2', '11')]) == '2 3 4 6 9 3 2 2 11'