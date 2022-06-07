from .code_345 import *
from .code_345 import diff_consecutivenums


def test():
    assert diff_consecutivenums([1, 1, 3, 4, 4, 5, 6, 7])==[0, 2, 1, 0, 1, 1, 1]