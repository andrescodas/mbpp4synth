from .code_758 import *
from .code_758 import unique_sublists


def test():
    assert unique_sublists([[10, 20, 30, 40], [60, 70, 50, 50], [90, 100, 200]])=={(10, 20, 30, 40): 1, (60, 70, 50, 50): 1, (90, 100, 200): 1}