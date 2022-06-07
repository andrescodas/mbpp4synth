from .code_97 import *
from .code_97 import frequency_lists


def test():
    assert frequency_lists([[20,30,40,17],[18,16,14,13],[10,20,30,40]])=={20:2,30:2,40:2,17: 1,18:1, 16: 1,14: 1,13: 1, 10: 1}