from .code_433 import *
from .code_433 import check_greater


def test():
    assert check_greater([2, 3, 4, 5, 6], 8) == 'Yes, the entered number is greater than those in the array'