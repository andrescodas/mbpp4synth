from .code_811 import *
from .code_811 import check_identical


def test():
    assert check_identical([(2, 14), (12, 25)], [(2, 14), (12, 25)]) == True