from .code_662 import *
from .code_662 import sorted_dict


def test():
    assert sorted_dict({'n1': [25,37,41], 'n2': [41,54,63], 'n3': [29,38,93]})=={'n1': [25, 37, 41], 'n2': [41, 54, 63], 'n3': [29, 38, 93]}