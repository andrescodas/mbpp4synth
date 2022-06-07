from .code_915 import *
from .code_915 import rearrange_numbs


def test():
    assert rearrange_numbs([10,15,14,13,-18,12,-20])==[10, 12, 13, 14, 15, -20, -18]