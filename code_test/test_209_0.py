from .code_209 import *
from .code_209 import heap_replace


def test():
    assert heap_replace( [25, 44, 68, 21, 39, 23, 89],21)==[21, 25, 23, 44, 39, 68, 89]