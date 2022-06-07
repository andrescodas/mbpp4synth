from .code_874 import *
from .code_874 import check_Concat


def test():
    assert check_Concat("abcabcabc","abc") == True