from .code_310 import *
from .code_310 import string_to_tuple


def test():
    assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')