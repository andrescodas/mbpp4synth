from .code_512 import *
from .code_512 import count_element_freq


def test():
    assert count_element_freq((5, 6, (5, 6), 7, (8, 9), 9) ) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}