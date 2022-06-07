from .code_200 import *
from .code_200 import position_max


def test():
    assert position_max([1,2,2,2,4,4,4,5,5,5,5])==[7,8,9,10]