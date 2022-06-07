from .code_465 import *
from .code_465 import drop_empty


def test():
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}