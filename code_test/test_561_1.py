from .code_561 import *
from .code_561 import assign_elements


def test():
    assert assign_elements([(6, 4), (9, 4), (3, 8), (4, 9), (9, 5)] ) == {4: [9], 6: [4], 9: [4, 5], 8: [], 3: [8], 5: []}