from .code_70 import *
from .code_70 import get_equal


def test():
    assert get_equal([(1, 2), (3, 4)], 2) == 'All tuples have same length'