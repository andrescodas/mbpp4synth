from .code_662 import *
from .code_662 import sorted_dict


def test():
    assert sorted_dict({'n1': [58,44,56], 'n2': [91,34,58], 'n3': [100,200,300]})=={'n1': [44, 56, 58], 'n2': [34, 58, 91], 'n3': [100, 200, 300]}