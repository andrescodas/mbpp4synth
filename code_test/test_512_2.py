from .code_512 import *
from .code_512 import count_element_freq


def test():
    assert count_element_freq((7, 8, (7, 8), 9, (10, 11), 11) ) == {7: 2, 8: 2, 9: 1, 10: 1, 11: 2}