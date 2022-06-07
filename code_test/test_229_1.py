from .code_229 import *
from .code_229 import re_arrange_array


def test():
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]