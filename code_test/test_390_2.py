from .code_390 import *
from .code_390 import add_string


def test():
    assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8']