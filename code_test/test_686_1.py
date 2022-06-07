from .code_686 import *
from .code_686 import freq_element


def test():
    assert freq_element((7, 8, 8, 9, 4, 7, 6, 5, 4) ) == '{7: 2, 8: 2, 9: 1, 4: 2, 6: 1, 5: 1}'