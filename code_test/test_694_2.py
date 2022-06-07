from .code_694 import *
from .code_694 import extract_unique


def test():
    assert extract_unique({'F' : [11, 13, 14, 17],'A' : [12, 11, 15, 18],'N' : [19, 21, 15, 36],'G' : [37, 36, 35]}) == [11, 12, 13, 14, 15, 17, 18, 19, 21, 35, 36, 37]