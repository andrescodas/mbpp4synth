from .code_117 import *
from .code_117 import list_to_float


def test():
    assert list_to_float( [("4", "4"), ("2", "27"), ("4.12", "9"), ("7", "11")] ) == '[(4.0, 4.0), (2.0, 27.0), (4.12, 9.0), (7.0, 11.0)]'