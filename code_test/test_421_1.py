from .code_421 import *
from .code_421 import concatenate_tuple


def test():
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'