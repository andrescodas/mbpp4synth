from .code_614 import *
from .code_614 import cummulative_sum


def test():
    assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30