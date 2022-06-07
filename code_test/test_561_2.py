from .code_561 import *
from .code_561 import assign_elements


def test():
    assert assign_elements([(6, 2), (6, 8), (4, 9), (4, 9), (3, 7)] ) == {2: [], 6: [2, 8], 8: [], 9: [], 4: [9, 9], 7: [], 3: [7]}