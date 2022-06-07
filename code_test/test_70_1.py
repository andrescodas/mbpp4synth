from .code_70 import *
from .code_70 import get_equal


def test():
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)], 3) == 'All tuples do not have same length'