from .code_854 import *
from .code_854 import raw_heap


def test():
    assert raw_heap([25, 35, 22, 85, 14, 65, 75, 25, 58])== [14, 25, 22, 25, 35, 65, 75, 85, 58]