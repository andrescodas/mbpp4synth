from .code_610 import *
from .code_610 import remove_kth_element


def test():
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]