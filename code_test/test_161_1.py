from .code_161 import *
from .code_161 import remove_elements


def test():
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 3, 5, 7])==[2, 4, 6, 8, 9, 10]