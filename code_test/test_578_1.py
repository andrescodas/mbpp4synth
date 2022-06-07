from .code_578 import *
from .code_578 import interleave_lists


def test():
    assert interleave_lists([10,20],[15,2],[5,10])==[10,15,5,20,2,10]