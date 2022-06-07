from .code_88 import *
from .code_88 import freq_count


def test():
    assert freq_count([1,2,3,4,3,2,4,1,3,1,4])==({1:3, 2:2,3:3,4:3}) 