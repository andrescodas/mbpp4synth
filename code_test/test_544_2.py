from .code_544 import *
from .code_544 import flatten_tuple


def test():
    assert flatten_tuple([('14', '21', '9'), ('24', '19'), ('12', '29'), ('23', '17')]) == '14 21 9 24 19 12 29 23 17'