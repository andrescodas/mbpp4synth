from .code_686 import *
from .code_686 import freq_element


def test():
    assert freq_element((1, 4, 3, 1, 4, 5, 2, 6, 2, 7) ) == '{1: 2, 4: 2, 3: 1, 5: 1, 2: 2, 6: 1, 7: 1}'