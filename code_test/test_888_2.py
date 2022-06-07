from .code_888 import *
from .code_888 import substract_elements


def test():
    assert substract_elements(((19, 5), (18, 7), (19, 11), (17, 12)), ((12, 9), (17, 11), (13, 3), (19, 5))) == ((7, -4), (1, -4), (6, 8), (-2, 7))