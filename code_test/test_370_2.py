from .code_370 import *
from .code_370 import float_sort


def test():
    assert float_sort([('item1', '5'), ('item2', '10'), ('item3', '14')])==[('item3', '14'), ('item2', '10'), ('item1', '5')] 