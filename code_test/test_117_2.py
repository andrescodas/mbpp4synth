from .code_117 import *
from .code_117 import list_to_float


def test():
    assert list_to_float( [("6", "78"), ("5", "26.45"), ("1.33", "4"), ("82", "13")] ) == '[(6.0, 78.0), (5.0, 26.45), (1.33, 4.0), (82.0, 13.0)]'