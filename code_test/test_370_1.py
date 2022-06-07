from .code_370 import *
from .code_370 import float_sort


def test():
    assert float_sort([('item1', '15'), ('item2', '10'), ('item3', '20')])==[('item3', '20'), ('item1', '15'), ('item2', '10')] 