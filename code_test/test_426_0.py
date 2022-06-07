from .code_426 import *
from .code_426 import filter_oddnumbers


def test():
    assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]