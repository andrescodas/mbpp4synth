from .code_426 import *
from .code_426 import filter_oddnumbers


def test():
    assert filter_oddnumbers([10,20,45,67,84,93])==[45,67,93]