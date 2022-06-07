from .code_686 import *
from .code_686 import freq_element


def test():
    assert freq_element((4, 5, 4, 5, 6, 6, 5, 5, 4) ) == '{4: 3, 5: 4, 6: 2}'