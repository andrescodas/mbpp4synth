from .code_720 import *
from .code_720 import add_dict_to_tuple


def test():
    assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})