from .code_561 import *
from .code_561 import assign_elements


def test():
    assert assign_elements([(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)] ) == {3: [8], 5: [3], 7: [5], 2: [7], 8: [4], 4: []}