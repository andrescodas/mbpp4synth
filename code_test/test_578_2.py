from .code_578 import *
from .code_578 import interleave_lists


def test():
    assert interleave_lists([11,44], [10,15], [20,5])==[11,10,20,44,15,5]