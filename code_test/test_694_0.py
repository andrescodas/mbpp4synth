from .code_694 import *
from .code_694 import extract_unique


def test():
    assert extract_unique({'msm' : [5, 6, 7, 8],'is' : [10, 11, 7, 5],'best' : [6, 12, 10, 8],'for' : [1, 2, 5]} ) == [1, 2, 5, 6, 7, 8, 10, 11, 12]