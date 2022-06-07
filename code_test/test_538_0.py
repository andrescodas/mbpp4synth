from .code_538 import *
from .code_538 import string_list_to_tuple


def test():
    assert string_list_to_tuple(("python 3.0")) == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')