from .code_811 import *
from .code_811 import check_identical


def test():
    assert check_identical([(1, 2), (3, 7)], [(12, 14), (12, 45)]) == False