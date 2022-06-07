from .code_512 import *
from .code_512 import count_element_freq


def test():
    assert count_element_freq((6, 7, (6, 7), 8, (9, 10), 10) ) == {6: 2, 7: 2, 8: 1, 9: 1, 10: 2}