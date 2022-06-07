from .code_421 import *
from .code_421 import concatenate_tuple


def test():
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'