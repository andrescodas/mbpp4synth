from .code_698 import *
from .code_698 import sort_dict_item


def test():
    assert sort_dict_item({(6, 7) : 4, (3, 4) : 10, (9, 5): 11, (7, 5): 13} ) == {(3, 4): 10, (7, 5): 13, (6, 7): 4, (9, 5): 11}