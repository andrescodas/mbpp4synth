from .code_945 import *
from .code_945 import tuple_to_set


def test():
    assert tuple_to_set(('z', 'd', 'e') ) == {'d', 'e', 'z'}