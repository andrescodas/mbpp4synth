from .code_749 import *
from .code_749 import sort_numeric_strings


def test():
    assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]