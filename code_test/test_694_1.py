from .code_694 import *
from .code_694 import extract_unique


def test():
    assert extract_unique({'Built' : [7, 1, 9, 4],'for' : [11, 21, 36, 14, 9],'ISP' : [4, 1, 21, 39, 47],'TV' : [1, 32, 38]} ) == [1, 4, 7, 9, 11, 14, 21, 32, 36, 38, 39, 47]