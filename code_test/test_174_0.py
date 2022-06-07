from .code_174 import *
from .code_174 import group_keyvalue


def test():
    assert group_keyvalue([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])=={'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}