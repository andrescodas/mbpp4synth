from .code_544 import *
from .code_544 import flatten_tuple


def test():
    assert flatten_tuple([('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]) == '1 4 6 5 8 2 9 1 10'