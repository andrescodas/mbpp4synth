from .code_749 import *
from .code_749 import sort_numeric_strings


def test():
    assert sort_numeric_strings(['2','3','8','4','7','9','8','2','6','5','1','6','1','2','3','4','6','9','1','2'])==[1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9, 9]