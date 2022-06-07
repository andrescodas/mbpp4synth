from .code_421 import *
from .code_421 import concatenate_tuple


def test():
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'