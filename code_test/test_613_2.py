from .code_613 import *
from .code_613 import maximum_value


def test():
    assert maximum_value([('key1', [5, 6, 7]), ('key2', [3, 6, 4]), ('key3', [11, 5])]) == [('key1', 7), ('key2', 6), ('key3', 11)]