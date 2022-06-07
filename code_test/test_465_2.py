from .code_465 import *
from .code_465 import drop_empty


def test():
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}