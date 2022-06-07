from .code_70 import *
from .code_70 import get_equal


def test():
    assert get_equal([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'