from .code_433 import *
from .code_433 import check_greater


def test():
    assert check_greater([1, 2, 3, 4, 5], 4) == 'No, entered number is less than those in the array'