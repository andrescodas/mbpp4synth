from .code_653 import *
from .code_653 import grouping_dictionary


def test():
    assert grouping_dictionary([('yellow', 10), ('blue', 20), ('yellow', 30), ('blue', 40), ('red', 10)])== ({'yellow': [10, 30], 'blue': [20, 40], 'red': [10]})