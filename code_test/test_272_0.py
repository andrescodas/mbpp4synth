from .code_272 import *
from .code_272 import rear_extract


def test():
    assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]