from .code_908 import *
from .code_908 import find_fixed_point


def test():
    assert find_fixed_point([-10, -1, 0, 3, 10, 11, 30, 50, 100],9) == 3