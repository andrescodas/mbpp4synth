from .code_117 import *
from .code_117 import list_to_float


def test():
    assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == '[(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]'