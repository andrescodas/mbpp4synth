from .code_209 import *
from .code_209 import heap_replace


def test():
    assert heap_replace([25, 44, 68, 21, 39, 23, 89],500)==[23, 25, 68, 44, 39, 500, 89]