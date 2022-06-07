from .code_698 import *
from .code_698 import sort_dict_item


def test():
    assert sort_dict_item({(7, 8) : 5, (4, 5) : 11, (10, 6): 12, (8, 6): 14} ) == {(4, 5): 11, (8, 6): 14, (7, 8): 5, (10, 6): 12}