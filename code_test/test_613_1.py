from .code_613 import *
from .code_613 import maximum_value


def test():
    assert maximum_value([('key1', [4, 5, 6]), ('key2', [2, 5, 3]), ('key3', [10, 4])]) == [('key1', 6), ('key2', 5), ('key3', 10)]