from .code_370 import *
from .code_370 import float_sort


def test():
    assert float_sort([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])==[('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] 