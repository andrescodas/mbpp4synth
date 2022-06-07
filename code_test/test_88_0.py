from .code_88 import *
from .code_88 import freq_count


def test():
    assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1}) 