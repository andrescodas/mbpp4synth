from .code_229 import *
from .code_229 import re_arrange_array


def test():
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]