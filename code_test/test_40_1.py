from .code_40 import *
from .code_40 import freq_element


def test():
    assert freq_element([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1})