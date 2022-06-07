from .code_174 import *
from .code_174 import group_keyvalue


def test():
    assert group_keyvalue([('yellow',100), ('blue', 200), ('yellow', 300), ('blue', 400), ('red', 100)])=={'yellow': [100, 300], 'blue': [200, 400], 'red': [100]}