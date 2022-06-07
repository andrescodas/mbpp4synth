from .code_811 import *
from .code_811 import check_identical


def test():
    assert check_identical([(10, 4), (2, 5)], [(10, 4), (2, 5)]) == True