from .code_161 import *
from .code_161 import remove_elements


def test():
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[5,7])==[1, 2, 3, 4, 6, 8, 9, 10]