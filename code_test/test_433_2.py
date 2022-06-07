from .code_433 import *
from .code_433 import check_greater


def test():
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == 'Yes, the entered number is greater than those in the array'