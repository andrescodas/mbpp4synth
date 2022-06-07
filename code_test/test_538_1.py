from .code_538 import *
from .code_538 import string_list_to_tuple


def test():
    assert string_list_to_tuple(("bigdata")) == ('b', 'i', 'g', 'd', 'a', 't', 'a')