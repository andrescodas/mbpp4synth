from .code_551 import *
from .code_551 import extract_column


def test():
    assert extract_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[1, 2, 1]