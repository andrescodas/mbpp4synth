from .code_328 import *
from .code_328 import rotate_left


def test():
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2]