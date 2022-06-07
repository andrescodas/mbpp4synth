from .code_915 import *
from .code_915 import rearrange_numbs


def test():
    assert rearrange_numbs([-20,20,-10,10,-30,30])==[10, 20, 30, -30, -20, -10]