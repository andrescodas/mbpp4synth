from .code_613 import *
from .code_613 import maximum_value


def test():
    assert maximum_value([('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]) == [('key1', 5), ('key2', 4), ('key3', 9)]