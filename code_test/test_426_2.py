from .code_426 import *
from .code_426 import filter_oddnumbers


def test():
    assert filter_oddnumbers([5,7,9,8,6,4,3])==[5,7,9,3]