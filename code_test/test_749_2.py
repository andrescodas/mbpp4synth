from .code_749 import *
from .code_749 import sort_numeric_strings


def test():
    assert sort_numeric_strings(['1','3','5','7','1', '3','13', '15', '17','5', '7 ','9','1', '11'])==[1, 1, 1, 3, 3, 5, 5, 7, 7, 9, 11, 13, 15, 17]