from .code_249 import *
from .code_249 import intersection_array


def test():
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]