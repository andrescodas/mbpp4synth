from .code_88 import *
from .code_88 import freq_count


def test():
    assert freq_count([5,6,7,4,9,10,4,5,6,7,9,5])==({10:1,5:3,6:2,7:2,4:2,9:2}) 