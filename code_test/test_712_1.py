from .code_712 import *
from .code_712 import remove_duplicate


def test():
    assert remove_duplicate(["a", "b", "a", "c", "c"] )==["a", "b", "c"]