from .code_310 import *
from .code_310 import string_to_tuple


def test():
    assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')