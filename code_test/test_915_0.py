from .code_915 import *
from .code_915 import rearrange_numbs


def test():
    assert rearrange_numbs([-1, 2, -3, 5, 7, 8, 9, -10])==[2, 5, 7, 8, 9, -10, -3, -1]