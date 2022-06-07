from .code_662 import *
from .code_662 import sorted_dict


def test():
    assert sorted_dict({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]})=={'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}