from .code_174 import *
from .code_174 import group_keyvalue


def test():
    assert group_keyvalue([('python', 1), ('python', 2), ('python', 3), ('python', 4), ('python', 5)])=={'python': [1,2,3,4,5]}